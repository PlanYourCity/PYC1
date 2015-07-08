from django.db import models

# Create your models here.

class ActOcio(models.Model):
	Ciudad=models.CharField(max_length=50)
	Direccion = models.CharField(max_length=200)
	Titulo=models.CharField(max_length=200)
	Descripcion = models.CharField(max_length=800)	
	Imagen = models.CharField(max_length=800)
	Precio=models.CharField(max_length=800)
	Fecha=models.CharField(max_length=60)	
	Hora = models.CharField(max_length=800)	
	Aforo_Max = models.CharField(max_length=800)	
	Usuario_owner=models.CharField(max_length=200)


class ActVivienda(models.Model):
	Ciudad=models.CharField(max_length=50)
	Direccion = models.CharField(max_length=200)
	Titulo=models.CharField(max_length=200)
	Descripcion=models.CharField(max_length=800)	
	Imagen=models.CharField(max_length=800)
	Precio=models.CharField(max_length=800)
	NumHab=models.CharField(max_length=10)	
	TipoOferta=models.CharField(max_length=15)		
	Usuario_owner=models.CharField(max_length=200)


class ActEmpleo(models.Model):
	Ciudad=models.CharField(max_length=50)
	Direccion = models.CharField(max_length=200)
	Titulo=models.CharField(max_length=200)
	Descripcion = models.CharField(max_length=800)	
	Sueldo=models.CharField(max_length=10)
	Periodo=models.CharField(max_length=50)	
	Plazas = models.CharField(max_length=800)	
	Usuario_owner=models.CharField(max_length=200)

