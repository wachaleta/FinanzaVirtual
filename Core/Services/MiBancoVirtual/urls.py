from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from Core.Services.MiBancoVirtual.viewsets import *
from .views import *

router = routers.DefaultRouter()

router.register(r"perfil", PerfilViewSet, basename="perfil")
router.register(r"total-saldo-perfiles", ObtenerSaldoTotalPerfilesViewSet, basename="total-saldo-perfiles")

router.register(r"cuenta", CuentaViewSet, basename="cuenta")

router.register(r"transaccion", TransaccionViewSet, basename="transaccion")
router.register(r"transacciones-rango-fechas", TransaccionesRangoFechasViewSet, basename="transacciones-rango-fechas")
router.register(r"gasto", GastoViewSet, basename="gasto")
router.register(r"ingreso", IngresoViewSet, basename="ingreso")
router.register(r"transferencia", TransferenciaViewSet, basename="transferencia")

router.register(r"categoria", CategoriaViewSet, basename="categoria")

urlpatterns = [
    # path("", home, name="home"),
    path('login/', Login.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('logout/', Logout.as_view(), name='logout'),
    path("Crear_Transaccion/<id>/", transacciones, name="crear_transaccion"),
    path("Modificar_Transaccion/<transaccion>/<id>/", modificar_transacciones, name="modificar_transaccion"),
    path("Modificar_Transferencia/<id>/", modificar_transferencia, name="modificar_transferencia"),
    path("Ver_Transacciones/<id>/", ver_transacciones, name="ver_transacciones"),
    path("perfiles/", perfiles, name="perfiles"),
    path("cuentas/", cuentas, name="cuentas"),
    path("categorias/", categorias, name="categorias"),
    path("prueba/", prueba, name="prueba"),
    path("transaccion/programada", transacciones_programadas, name="transaccion-programada"),
    path("prueba-vue", vue, name="vue"),

    # Nuevas Apis
    path("", include(router.urls)),
]
