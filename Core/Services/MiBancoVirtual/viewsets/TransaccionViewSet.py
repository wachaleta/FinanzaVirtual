from datetime import date
from decimal import Decimal

from django.db.models import Q, Value, F
from django.db.models.functions import Concat

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ....Application.Behaviours import FinanzasModelViewSet
from ..models import *
from ..serializers import TransaccionSerializer
from ..validators import GastoCrearValidator

class TransaccionViewSet(FinanzasModelViewSet):
    serializer_class = TransaccionSerializer
    create_validator = GastoCrearValidator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id
        fechaInicial = self.request.query_params.get("fechaInicial", date.today())
        fechaFinal = self.request.query_params.get("fechaFinal", date.today())
        IdPerfiles = self.request.query_params.getlist("IdPerfiles", [])
        IdCuentas = self.request.query_params.getlist("IdCuentas", [])
        IdCategorias = self.request.query_params.getlist("IdCategorias", [])

        lista_transacciones = Transaccion.objects.filter(
                Q(IdPerfilOrdenante__IdUsuario = idUsuario) | Q(IdPerfilBeneficiario__IdUsuario = idUsuario) |
                Q(IdCuentaOrdenante__IdUsuario = idUsuario) | Q(IdCuentaBeneficiaria__IdUsuario = idUsuario) 
            ).filter(Fecha__gte = fechaInicial).filter(Fecha__lte = fechaFinal)
        
        if IdPerfiles != []:
            lista_transacciones = lista_transacciones.filter(
                Q(IdPerfilOrdenante__IdPerfil__in = IdPerfiles) | Q(IdPerfilBeneficiario__IdPerfil__in = IdPerfiles)
            )

        if IdCuentas != []:
            lista_transacciones = lista_transacciones.filter(
                Q(IdCuentaOrdenante__IdCuenta__in = IdCuentas) | Q(IdCuentaBeneficiaria__IdCuenta__in = IdCuentas)
            )

        if IdCategorias != []:
            lista_transacciones = lista_transacciones.filter(IdCategoria__in = IdCategorias)
        
        return lista_transacciones.annotate(
            ordenante_nombre = Concat(
                F("IdCuentaOrdenante__Nombre"), 
                Value(" - "),
                F("IdPerfilOrdenante__Nombre")
            )
        ).annotate(
            beneficiario_nombre = Concat(
                F("IdCuentaBeneficiaria__Nombre"), 
                Value(" - "),
                F("IdPerfilBeneficiario__Nombre")
            )
        ).order_by("-Fecha").order_by("-FechaCreacion")
    
    def list(self, request, *args, **kwargs):
        
        queryset = self.filter_queryset(self.get_queryset())
        IdPerfiles = request.query_params.getlist("IdPerfiles", [])
        IdCuentas = request.query_params.getlist("IdCuentas", [])

        query = {
            "IdPerfilOrdenante": None,
            "IdCuentaOrdenante": None,
        }
        listaSalidas = queryset.exclude(**query)

        query = {
            "IdPerfilBeneficiario": None,
            "IdCuentaBeneficiaria": None,
        }
        listaEntradas = queryset.exclude(**query)

        if IdPerfiles != []:
            query = {
                "IdPerfilOrdenante__in": IdPerfiles,
            }
            listaSalidas = listaSalidas.filter(**query)

            query = {
                "IdPerfilBeneficiario__in": IdPerfiles,
            }
            listaEntradas = listaEntradas.filter(**query)

        if IdCuentas != []:
            query = {
                "IdCuentaOrdenante__in": IdCuentas,
            }
            listaSalidas = listaSalidas.filter(**query)

            query = {
                "IdCuentaBeneficiaria__in": IdCuentas,
            }
            listaEntradas = listaEntradas.filter(**query)
            
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