from django.db import models

class User(models.Model):
	nom_user = models.CharField(max_length=64)
	pass_user = models.CharField(max_length=64)
	type_user = models.CharField(max_length=16)

class Vehicule(models.Model):
	nom = models.CharField(max_length=32)
	marque = models.CharField(max_length=16)
	model = models.CharField(max_length=32)
	plaque = models.CharField(max_length=16)
	etat = models.CharField(max_length=16)

class Panne(models.Model):
	cout = models.IntegerField(max_length=10)
	nom_cas = models.CharField(max_length=32)
	nom_panne = models.CharField(max_length=32)
	type = models.CharField(max_length=32)
	garage = models.CharField(max_length=32)
	contact = models.CharField(max_length=32)
	date = models.CharField(max_length=16)

class Location(models.Model):
	cout_location = models.IntegerField(max_length=10)
	type_location = models.CharField(max_length=10)
	nom_cas = models.CharField(max_length=32)
	nom_client = models.CharField(max_length=32)
	date_debut = models.CharField(max_length=16)
	date_fin = models.CharField(max_length=16)
	date = models.CharField(max_length=16)
