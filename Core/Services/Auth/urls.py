from rest_framework import routers
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .ApiViews import *
from Core.Services.Auth.Viewsets import *

router = routers.DefaultRouter()

router.register(r"register", RegisterViewSet, basename="register")

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('login2/', IniciarSesionApiView.as_view(), name='login2'),
    path("", include(router.urls)),
]
