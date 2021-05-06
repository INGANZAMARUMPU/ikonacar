from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"

class VehiculeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vehicule
		fields = "__all__"

class PanneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Panne
		fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = "__all__"
