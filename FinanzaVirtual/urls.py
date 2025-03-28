"""FinanzaVirtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from MiBancoVirtual.viewsets import *

router = routers.DefaultRouter()
router.register(r"perfil", PerfilViewSet, basename="perfil")
router.register(r"total-saldo-perfiles", ObtenerSaldoTotalPerfilesViewSet, basename="total-saldo-perfiles")

router.register(r"cuenta", CuentaViewSet, basename="cuenta")

router.register(r"transaccion", TransaccionViewSet, basename="transaccion")
router.register(r"transaccion-crear", TransaccionCrearViewSet, basename="transaccion-crear")
router.register(r"transaccion-por-id", TransaccionPorIdViewSet, basename="transaccion-por-id")

router.register(r"transacciones-programadas", TransaccionProgramadaViewSet, basename="transacciones-programadas")
router.register(r"transaccion-programada-por-id", TransaccionProgramadaPorIdViewSet, basename="transaccion-programada-por-id")

router.register(r"transaccion-programada-detalle", TransaccionProgramadaDetallePorIdTransaccionProgramadaViewSet, basename="transaccion-programada-detalle")
router.register(r"transaccion-programada-detalle-por-id", TransaccionProgramadaDetallePorIdViewSet, basename="transaccion-programada-detalle-por-id")

router.register(r"categoria", CategoriaViewSet, basename="categoria")
router.register(r"gasto", GastoViewSet, basename="gasto")
router.register(r"ingreso", IngresoViewSet, basename="ingresos")
router.register(r"transferencia", TransferenciaViewSet, basename="transferencia")

urlpatterns = [
    path("api/", include(router.urls),),
    path('admin/', admin.site.urls),
    path('', include("MiBancoVirtual.urls")),
    path('api-auth/', include('rest_framework.urls'))
]