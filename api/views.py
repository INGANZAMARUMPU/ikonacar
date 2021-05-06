from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import *

class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = AllowAny,

class VehiculeView(viewsets.ModelViewSet):
	queryset = Vehicule.objects.all()
	serializer_class = VehiculeSerializer
	permission_classes = AllowAny,

class PanneView(viewsets.ModelViewSet):
	queryset = Panne.objects.all()
	serializer_class = PanneSerializer
	permission_classes = AllowAny,

class LocationView(viewsets.ModelViewSet):
	queryset = Location.objects.all()
	serializer_class = LocationSerializer
	permission_classes = AllowAny,