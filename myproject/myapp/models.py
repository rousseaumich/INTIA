
# Create your models here.
# models.py
from django.db import models

class Direction(models.Model):
    nom = models.CharField(max_length=100)

class Succursale(models.Model):
    nom = models.CharField(max_length=100)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='succursales')

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    succursale = models.ForeignKey(Succursale, on_delete=models.CASCADE, related_name='clients')

class Assurance(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='assurances')





