from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import F, Value
from django.db.models.functions import Concat

from ..models import *
from ..serializers import *
    
class IngresoViewSet(viewsets.ModelViewSet):
    
    serializer_class = IngresoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        
        idUsuario = self.request.user.id

        fechaInicio = self.request.query_params.get("fechaInicio")
        fechaFinal = self.request.query_params.get("fechaFinal")

        lista_cuentas = Cuenta.objects.filter(usuario = idUsuario)
        lista_perfiles = Perfil.objects.filter(usuario = idUsuario)

        lista_ingresos = Transaccion.objects.filter(
            #   Validar que sean del usuario
            cuentaBeneficiaria__in = lista_cuentas,
            perfilBeneficiario__in = lista_perfiles,

            #   Validar que sea ingreso
            cuentaOrdenante__isnull = True,
            perfilOrdenante__isnull = True,

            #   Validar rango de fechas
            fecha__gte = fechaInicio,
            fecha__lte = fechaFinal
        )
        
        return lista_ingresos.annotate(
            nombre = Concat(
                F("cuentaBeneficiaria__nombre"),
                Value(" - "),
                F("perfilBeneficiario__nombre")
            )
        ).annotate(
            categoria_nombre = F("categoria__nombre")
        )
        return Transaccion.objects.raw("""
            SELECT 
                transaccion.id,
                transaccion.monto,
                transaccion.descripcion,
                transaccion.fecha,
                transaccion.categoria_id,
                categoria.nombre as categoria_nombre,
                transaccion.beneficiario_id as subcuenta,
                transaccion.ordenante_id,
                (cuenta.nombre || " - " || perfil.nombre) as subcuenta_nombre,
                transaccion.fechaCreacion 
            FROM MiBancoVirtual_transaccion transaccion
            INNER JOIN MiBancoVirtual_subcuenta subcuenta ON subcuenta.id = transaccion.beneficiario_id 
            INNER JOIN MiBancoVirtual_categoria categoria ON categoria.id  = transaccion.categoria_id
            INNER JOIN MiBancoVirtual_perfil perfil ON perfil.id = subcuenta.perfil_id 
            INNER JOIN MiBancoVirtual_cuenta cuenta on cuenta.id = subcuenta.cuenta_id 
            INNER JOIN auth_user usuario ON usuario.id = cuenta.usuario_id
            WHERE transaccion.ordenante_id IS NULL AND usuario.id = %s
            ORDER BY transaccion.fechaCreacion DESC, transaccion.fecha DESC 
            """, [idUsuario])