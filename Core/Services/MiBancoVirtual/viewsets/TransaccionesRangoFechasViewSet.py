from datetime import date
from decimal import Decimal

from django.db.models import Q, Value, F, Case, When, Value, BooleanField, CharField
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransaccionesRangoFechasSerializer

class TransaccionesRangoFechasViewSet(FinanzasModelViewSet):
    serializer_class = TransaccionesRangoFechasSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id
        fechaInicial = self.request.query_params.get("fechaInicial", date.today())
        fechaFinal = self.request.query_params.get("fechaFinal", date.today())
        IdPerfiles = self.request.query_params.getlist("IdPerfiles", [])
        IdCuentas = self.request.query_params.getlist("IdCuentas", [])
        IdCategorias = self.request.query_params.getlist("IdCategorias", [])

        filtros = Q(
            Q(
                IdPerfilOrdenante__IdUsuario = idUsuario
            ) | Q(
                IdPerfilBeneficiario__IdUsuario = idUsuario
            ) | Q(
                IdCuentaOrdenante__IdUsuario = idUsuario
            ) | Q(
                IdCuentaBeneficiaria__IdUsuario = idUsuario
            ), 
            Q(Fecha__gte = fechaInicial),
            Q(Fecha__lte = fechaFinal)
        )

        filtrosExtra = Q()
        filtrosCategorias = Q()

        if IdPerfiles != []:
            filtrosExtra |= Q(IdPerfilOrdenante__IdPerfil__in = IdPerfiles) | Q(IdPerfilBeneficiario__IdPerfil__in = IdPerfiles)
            

        if IdCuentas != []:
            filtrosExtra |= Q(IdCuentaOrdenante__IdCuenta__in = IdCuentas) | Q(IdCuentaBeneficiaria__IdCuenta__in = IdCuentas)
        

        if IdCategorias != []:
            filtrosCategorias |= Q(IdCategoria__in = IdCategorias)

        listaTransacciones = Transaccion.objects.filter(filtros, filtrosExtra, filtrosCategorias)
        
        return listaTransacciones.annotate(
            EsTransferencia = Case(
                When(
                    Q(IdPerfilOrdenante__isnull = False, IdPerfilBeneficiario__isnull = False)
                    | Q(IdCuentaOrdenante__isnull = False, IdCuentaBeneficiaria__isnull = False),
                    then=True
                ),
                default=Value(False),
                output_field=BooleanField()
            )
        ).annotate(
            EsIngreso = Case(
                When(
                    Q(IdPerfilBeneficiario__isnull=False, IdCuentaBeneficiaria__isnull=False),
                    then=True
                ),
                default=Value(False),
                output_field=BooleanField()
            )
        ).annotate(
            EsGasto = Case(
                When(
                    Q(IdPerfilOrdenante__isnull=False, IdCuentaOrdenante__isnull=False),
                    then=True
                ),
                default=Value(False),
                output_field=BooleanField()
            )
        ).annotate(
            Nombre = Case(
                When(
                    Q(EsGasto=True),
                    then=Concat(
                        F("IdCuentaOrdenante__Nombre"),
                        Value(" - "),
                        F("IdPerfilOrdenante__Nombre")
                    )
                ),
                When(
                    Q(EsIngreso=True),
                    then=Concat(
                        F("IdCuentaBeneficiaria__Nombre"),
                        Value(" - "),
                        F("IdPerfilBeneficiario__Nombre")
                    )
                ),
                When(
                    Q(EsTransferencia=True, IdPerfilOrdenante__isnull=False),
                    then=Concat(
                        F("IdPerfilOrdenante__Nombre"),
                        Value(" -> "),
                        F("IdPerfilBeneficiario__Nombre")
                    )
                ),
                default=Concat(
                        F("IdCuentaOrdenante__Nombre"),
                        Value(" -> "),
                        F("IdCuentaBeneficiaria__Nombre")
                    ),
                output_field=CharField()
            )
        ).annotate(
            CategoriaNombre = F("IdCategoria__Nombre")
        ).order_by("-Fecha").order_by("-FechaCreacion")
    
    def list(self, request, *args, **kwargs):
        
        queryset = self.filter_queryset(self.get_queryset())
        IdPerfiles = request.query_params.getlist("IdPerfiles", [])
        IdCuentas = request.query_params.getlist("IdCuentas", [])

        filtrosSalidas = Q(IdPerfilOrdenante__isnull=False) | Q(IdCuentaOrdenante__isnull=False)
        filtrosEntradas = Q(IdPerfilBeneficiario__isnull=False) | Q(IdCuentaBeneficiaria__isnull=False)
        filtrosExclude = Q(IdPerfilOrdenante__in=IdPerfiles, IdPerfilBeneficiario__in=IdPerfiles) | Q(IdCuentaOrdenante__in=IdCuentas, IdCuentaBeneficiaria__in=IdCuentas)

        filtrosExtra = Q()

        if(IdPerfiles == [] and IdCuentas == []):
            filtrosExtra |= Q(EsTransferencia=False)

        filtrosExtraSalidas = filtrosExtra
        filtrosExtraEntradas = filtrosExtra
        
        if(IdPerfiles != []):
            filtrosExtraSalidas |= Q(IdPerfilOrdenante__in=IdPerfiles)
            filtrosExtraEntradas |= Q(IdPerfilBeneficiario__in=IdPerfiles)

        if(IdCuentas != []):
            filtrosExtraSalidas |= Q(IdCuentaOrdenante__in=IdCuentas)
            filtrosExtraEntradas |= Q(IdCuentaBeneficiaria__in=IdCuentas)

        listaSalidas = queryset.filter(
                filtrosSalidas,
                filtrosExtraSalidas
            ).exclude(
                filtrosExclude
            )

        listaEntradas = queryset.filter(
                filtrosEntradas,
                filtrosExtraEntradas
            ).exclude(
                filtrosExclude
            )

        totalSalidas = sum(list(map(lambda x: x.Monto, listaSalidas)))
        totalEntradas = sum(list(map(lambda x: x.Monto, listaEntradas)))

        serializer = self.get_serializer(queryset, many=True)

        return Response({
            'TotalSalidas': Decimal(totalSalidas),
            'TotalEntradas': Decimal(totalEntradas),
            'TotalBalance': Decimal(totalEntradas - totalSalidas),
            'Items': serializer.data
        })
    
    def get_create_validated_data(self, data):
        if data["TipoTransaccion"] == "Gasto":
            return {
                "Monto": data.get("Monto", 0),
                "Fecha": data.get("Fecha", ""),
                "IdCuentaOrdenante": data.get("IdCuentaOrdenante", ""),
                "IdPerfilOrdenante": data.get("IdPerfilOrdenante", ""),
                "IdCategoria": data.get("IdCategoria", ""),
                "Descripcion": data.get("Descripcion", ""),
            }
        
        if data["TipoTransaccion"] == "Ingreso":
            return {
                "Monto": data.get("Monto", 0),
                "Fecha": data.get("Fecha", ""),
                "IdCuentaBeneficiaria": data.get("IdCuentaOrdenante", ""),
                "IdPerfilBeneficiario": data.get("IdPerfilOrdenante", ""),
                "IdCategoria": data.get("IdCategoria", ""),
                "Descripcion": data.get("Descripcion", ""),
            }