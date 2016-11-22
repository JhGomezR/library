from django.db import models
from apps.autor.models import Autor

class Libro(models.Model):
	autor = models.ManyToManyField(Autor)
	nombre = models.CharField(max_length=50)
	resumen = models.TextField(max_length=300)

	def __unicode__(self):
		return self.nombre

