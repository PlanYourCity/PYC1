from django.db import models

# Create your models here.

class Actividades(models.Model):
	Titulo=models.CharField(max_length=200)
	Direccion = models.CharField(max_length=200)
	Precio=models.CharField(max_length=800)	
	Aforo_Max = models.CharField(max_length=800)	
	Hora = models.CharField(max_length=800)	
	Imagen = models.CharField(max_length=800)
	Descripcion = models.CharField(max_length=800)	
	Categoria= models.CharField(max_length=200)
	Usuario_owner=models.CharField(max_length=200)
	Tipo_User=models.CharField(max_length=200)
