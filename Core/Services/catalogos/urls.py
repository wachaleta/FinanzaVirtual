from rest_framework import routers
from django.urls import path, include

from Core.Services.catalogos.viewsets import *

router = routers.DefaultRouter()

router.register(r"efectivo-moneda", EfectivoMonedaViewSet, basename="efectivo-moneda")

urlpatterns = [
    path("", include(router.urls)),
]
