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
                perfil_ordenante__usuario = idUsuario
            ) | Q(
                perfil_beneficiario__usuario = idUsuario
            ) | Q(
                cuenta_ordenante__usuario = idUsuario
            ) | Q(
                cuenta_beneficiaria__usuario = idUsuario
            ), 
            Q(fecha__gte = fechaInicial),
            Q(fecha__lte = fechaFinal)
        )

        filtrosExtra = Q()
        filtrosCategorias = Q()

        if IdPerfiles != []:
            filtrosExtra |= Q(perfil_ordenante__id__in = IdPerfiles) | Q(perfil_beneficiario__id__in = IdPerfiles)
            

        if IdCuentas != []:
            filtrosExtra |= Q(cuenta_ordenante__id__in = IdCuentas) | Q(cuenta_beneficiaria__id__in = IdCuentas)
        

        if IdCategorias != []:
            filtrosCategorias |= Q(categoria__in = IdCategorias)

        listaTransacciones = Transaccion.objects.filter(filtros, filtrosExtra, filtrosCategorias)
        
        return listaTransacciones.annotate(
            EsTransferencia = Case(
                When(
                    Q(perfil_ordenante__isnull = False, perfil_beneficiario__isnull = False)
                    | Q(cuenta_ordenante__isnull = False, cuenta_beneficiaria__isnull = False),
                    then=True
                ),
                default=Value(False),
                output_field=BooleanField()
            )
        ).annotate(
            EsIngreso = Case(
                When(
                    Q(perfil_beneficiario__isnull=False, cuenta_beneficiaria__isnull=False),
                    then=True
                ),
                default=Value(False),
                output_field=BooleanField()
            )
        ).annotate(
            EsGasto = Case(
                When(
                    Q(perfil_ordenante__isnull=False, cuenta_ordenante__isnull=False),
                    then=True
                ),
                default=Value(False),
                output_field=BooleanField()
            )
        ).annotate(
            nombre = Case(
                When(
                    Q(EsGasto=True),
                    then=Concat(
                        F("cuenta_ordenante__nombre"),
                        Value(" - "),
                        F("perfil_ordenante__nombre")
                    )
                ),
                When(
                    Q(EsIngreso=True),
                    then=Concat(
                        F("cuenta_beneficiaria__nombre"),
                        Value(" - "),
                        F("perfil_beneficiario__nombre")
                    )
                ),
                When(
                    Q(EsTransferencia=True, perfil_ordenante__isnull=False),
                    then=Concat(
                        F("perfil_ordenante__nombre"),
                        Value(" -> "),
                        F("perfil_beneficiario__nombre")
                    )
                ),
                default=Concat(
                        F("cuenta_ordenante__nombre"),
                        Value(" -> "),
                        F("cuenta_beneficiaria__nombre")
                    ),
                output_field=CharField()
            )
        ).annotate(
            categoria_nombre = F("categoria__nombre")
        ).order_by("-fecha", "-fecha_creacion")
    
    def list(self, request, *args, **kwargs):
        
        queryset = self.filter_queryset(self.get_queryset())
        IdPerfiles = request.query_params.getlist("IdPerfiles", [])
        IdCuentas = request.query_params.getlist("IdCuentas", [])

        filtrosSalidas = Q(perfil_ordenante__isnull=False) | Q(cuenta_ordenante__isnull=False)
        filtrosEntradas = Q(perfil_beneficiario__isnull=False) | Q(cuenta_beneficiaria__isnull=False)
        filtrosExclude = Q(perfil_ordenante__in=IdPerfiles, perfil_beneficiario__in=IdPerfiles) | Q(cuenta_ordenante__in=IdCuentas, cuenta_beneficiaria__in=IdCuentas)

        filtrosExtra = Q()

        if(IdPerfiles == [] and IdCuentas == []):
            filtrosExtra |= Q(EsTransferencia=False)

        filtrosExtraSalidas = filtrosExtra
        filtrosExtraEntradas = filtrosExtra
        
        if(IdPerfiles != []):
            filtrosExtraSalidas |= Q(perfil_ordenante__in=IdPerfiles)
            filtrosExtraEntradas |= Q(perfil_beneficiario__in=IdPerfiles)

        if(IdCuentas != []):
            filtrosExtraSalidas |= Q(cuenta_ordenante__in=IdCuentas)
            filtrosExtraEntradas |= Q(cuenta_beneficiaria__in=IdCuentas)

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

        totalSalidas = sum(list(map(lambda x: x.monto, listaSalidas)))
        totalEntradas = sum(list(map(lambda x: x.monto, listaEntradas)))

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
                "cuenta_ordenante": data.get("cuenta_ordenante", ""),
                "perfil_ordenante": data.get("perfil_ordenante", ""),
                "IdCategoria": data.get("IdCategoria", ""),
                "Descripcion": data.get("Descripcion", ""),
            }
        
        if data["TipoTransaccion"] == "Ingreso":
            return {
                "Monto": data.get("Monto", 0),
                "Fecha": data.get("Fecha", ""),
                "cuenta_beneficiaria": data.get("cuenta_ordenante", ""),
                "perfil_beneficiario": data.get("perfil_ordenante", ""),
                "IdCategoria": data.get("IdCategoria", ""),
                "Descripcion": data.get("Descripcion", ""),
            }