from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template.loader import get_template
from core.models import Actividades
from django.template import Context

from django.views.generic.list import ListView

import urllib2
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
import xml.sax

# Create your views here.
#def Detalles(request):
def lista_eventos(request):

	if request.method == "GET":
		lista_actividades=[]
		event= Actividades(Titulo="Concierto",Direccion="puerta del sol",Precio="30 $",Aforo_Max="completo",Hora="15:00",Imagen="../../static/images/imagen.png",Descripcion="lssdfsdf",Categoria="dsadas",Usuario_owner="ffsd",Tipo_User="E")	
		event.save()
		event1= Actividades(Titulo="300",Direccion="bambu",Precio="50 $",Aforo_Max="limitado",Hora="15:00",Imagen="../../static/images/imagen.png",Descripcion="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris interdum posuere dolor, tempor pulvinar nisi interdum eget. Aliquam dui arcu, ornare vitae eros sed, hendrerit maximus mi. Cras feugiat auctor nisl, eu placerat enim. Aliquam sit amet libero tellus. Donec quis posuere sem. Aenean pellentesque eleifend lacus, quis ultrices urna placerat vel. Duis tempor purus eget felis luctus pharetra vitae vitae velit. Praesent erat ex, molestie id faucibus vel, aliquam aliquam lectus. Donec pharetra maximus turpis dictum tincidunt. Suspendisse fermentum orci ut placerat placerat. Praesent tincidunt augue lectus, quis mollis orci hendrerit ac. Donec imperdiet est a ultrices luctus.",Categoria="dsadas",Usuario_owner="ffsd",Tipo_User="E")	
	
		event1.save()
		
		record=Actividades.objects.all()
		#record.delete()
		template = get_template("listado.html")		
		diccionario = {'record':record}		
		return HttpResponse(template.render(Context(diccionario)))
	else:
		return ("no es GET")

def detalle(request, titulo):

	print(titulo)
	if request.method == "GET":
		record=Actividades.objects.all()
		for i in record:
			if i.Titulo==titulo:
				Tit=i.Titulo
				Imag=i.Imagen
				Prec=i.Precio
				Dirr=i.Direccion
				Hour=i.Hora
				Descri=i.Descripcion
				Afor=i.Aforo_Max

			else:
				print("ERROR")
		titulo=""
		template = get_template("detalle.html")		
		diccionario = {'titulo':Tit,'imagen':Imag,'precio':Prec,'direccion':Dirr,'hora':Hour,'descripcion':Descri,'aforo':Afor}		
		
		return HttpResponse(template.render(Context(diccionario)))

def ofertar(request):
	if request.method == "GET":
		titulo="Ofertar"
		template = get_template("enConstruccion.html")
		diccionario = {'titulo':titulo}
		
		return HttpResponse(template.render(Context(diccionario)))

def buscar(request):
	if request.method == "GET":
		titulo="Buscar"
		template = get_template("enConstruccion.html")
		diccionario = {'titulo':titulo}
		
		return HttpResponse(template.render(Context(diccionario)))

def calendario(request):
	if request.method == "GET":
		titulo="Calendario"
		template = get_template("enConstruccion.html")
		diccionario = {'titulo':titulo}
		
		return HttpResponse(template.render(Context(diccionario)))