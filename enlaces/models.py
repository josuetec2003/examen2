#encoding: utf-8

from django.db import models

class Enlace(models.Model):
	url = models.CharField(max_length=300)
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()
	imagen = models.ImageField(upload_to='imagenes', verbose_name='Subir imagen', blank=True)
	fecha = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.nombre