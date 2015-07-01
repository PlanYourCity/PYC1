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
		event= Actividades(Titulo="Concie fff",Direccion="Yousf",Precio="27 $",Aforo_Max="",Hora="15:00",Imagen="static/images/imagen.png",Descripcion="lssdfsdf",Categoria="dsadas",Usuario_owner="ffsd",Tipo_User="E")	
		event.save()	
		print(lista_actividades)	
		record=Actividades.objects.all()
					
		template = get_template("listado.html")		
		diccionario = {'record':record}		
		return HttpResponse(template.render(Context(diccionario)))
	else:
		return ("no es GET")

#def Detalles(request):

	

