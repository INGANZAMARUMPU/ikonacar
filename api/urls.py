from django.urls import path, include, re_path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register("user", UserView)
router.register("vehicule", VehiculeView)
router.register("panne", PanneView)
router.register("location", LocationView)

urlpatterns = [
    path('', include(router.urls)),
]
