from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = "id", "nom_user", "pass_user", "type_user"

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
	list_display = "id","nom", "marque", "model", "plaque", "etat"

@admin.register(Panne)
class PanneAdmin(admin.ModelAdmin):
	list_display = "id","cout", "nom_cas", "nom_panne", "type", "garage", "contact", "date"

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
	list_display = "id","cout_location", "type_location", "nom_cas", "nom_client", "date_debut", "date_fin", "date"
