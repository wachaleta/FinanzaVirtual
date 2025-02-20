from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q, F, Value
from django.db.models.functions import Concat

from ..models import *
from ..serializers import *

class GastoViewSet(viewsets.ModelViewSet):
    serializer_class = GastoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        idUsuario = self.request.user.id

        fechaInicio = self.request.query_params.get("fechaInicio")
        fechaFinal = self.request.query_params.get("fechaFinal")

        lista_cuentas = Cuenta.objects.filter(usuario = idUsuario)
        lista_perfiles = Perfil.objects.filter(usuario = idUsuario)

        lista_gastos = Transaccion.objects.filter(
            #   Validar que sean del usuario
            perfilOrdenante__in = lista_perfiles,
            cuentaOrdenante__in = lista_cuentas,

            #   Validar que sea Gasto
            cuentaBeneficiaria__isnull = True,
            perfilBeneficiario__isnull = True,

            #   Validar el rango de fechas
            fecha__gte = fechaInicio,
            fecha__lte = fechaFinal
        )

        return lista_gastos.annotate(
            nombre = Concat(
                F("cuentaOrdenante__nombre"),
                Value(" - "),
                F("perfilOrdenante__nombre")
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
                transaccion.ordenante_id as subcuenta,
                (cuenta.nombre || " - " || perfil.nombre) as subcuenta_nombre,
                transaccion.fechaCreacion 
            FROM MiBancoVirtual_transaccion transaccion
            INNER JOIN MiBancoVirtual_subcuenta subcuenta ON subcuenta.id = transaccion.ordenante_id 
            INNER JOIN MiBancoVirtual_categoria categoria ON categoria.id  = transaccion.categoria_id
            INNER JOIN MiBancoVirtual_perfil perfil ON perfil.id = subcuenta.perfil_id 
            INNER JOIN MiBancoVirtual_cuenta cuenta on cuenta.id = subcuenta.cuenta_id 
            INNER JOIN auth_user usuario ON usuario.id = cuenta.usuario_id 
            WHERE transaccion.beneficiario_id is NULL  AND usuario.id = %s
            ORDER BY transaccion.fechaCreacion DESC, transaccion.fecha DESC
            """, [idUsuario])
