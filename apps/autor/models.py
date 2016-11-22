from django import forms
from django.db import models

# Create your models here.

class Autor(models.Model):
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	pais = models.CharField(max_length=30)
	descripcion = models.TextField(max_length=200)
	

	def __unicode__(self):
		return self.nombre
