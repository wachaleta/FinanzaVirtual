from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import *
from .viewsApi import *

urlpatterns = [
    path("", home, name="home"),
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
    path("perfil-crear", PerfilCrearApiView.as_view(), name="perfil-crear"),
    path("perfil/<int:pk>/editar", PerfilEditarApiView.as_view(), name="perfil-editar"),
    path("perfil/<int:pk>/eliminar", PerfilEliminarApiView.as_view(), name="perfil-eliminar"),
]
