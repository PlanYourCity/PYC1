from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template.loader import get_template
from core.models import ActOcio
from core.models import ActVivienda
from core.models import ActEmpleo
from django.template import Context

from django.views.generic.list import ListView

import urllib2
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string
import xml.sax
import json

# Create your views here.
#def Detalles(request):


def inicio(request):
	template = get_template("base.html")				
	return HttpResponse(template.render(Context()))	

def lista_eventos(request):

	if request.method == "GET":
		lista_actividades=[]
		
		record=ActOcio.objects.all()
		#record.delete()
		template = get_template("listado.html")		
		diccionario = {'record':record}		
		return HttpResponse(template.render(Context(diccionario)))
	else:
		return ("no es GET")

def detalle(request, titulo):

	print(titulo)
	if request.method == "GET":
		record=ActOcio.objects.all()
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


def ofertar(request,categoria):


	if request.method=="GET":		
										
		template = get_template("form_ofertar.html")		
		diccionario = {'categoria':categoria}		
		return HttpResponse(template.render(Context(diccionario)))

	elif request.method == "POST":
		#respuesta = {}			
		ciuda=request.POST['Ciudad']
		direccio=request.POST['Direccion']
		titul=request.POST['Titulo']
		descripcio=request.POST['Descripcion']	
		
		if categoria=="ocio":
				
			image=request.POST['Imagen']
			#ruta_imga="../../static/images/"

			preci=request.POST['Precio']
			fech=request.POST['Fecha']	
			hor=request.POST['Hora']	
			aforo_ma=request.POST['Aforo_Max']	
			propietari='Youssef'

			try:
				record=ActOcio.objects.get(Titulo=titul)
			except:
				Nueva_actividad_ocio=ActOcio(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Imagen=image,Precio=preci,Fecha=fech,Hora=hor,Aforo_Max=aforo_ma,Usuario_owner=propietari)
				Nueva_actividad_ocio.save()			
			return HttpResponseRedirect("/ofertar/ocio")
		elif categoria=="vivienda":
			imagen=request.POST['Imagen']
			precio=request.POST['Precio']
			nhabit=request.POST['NumHab']	
			toferta=request.POST['TipoOferta']		
			propietario='Fabio'
			try:
				record=ActVivienda.objects.get(Titulo=titul)
				#response = {'message': False}
			except:
				Nueva_vivienda=ActVivienda(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Imagen=imagen,Precio=precio,NumHab=nhabit,TipoOferta=toferta,Usuario_owner=propietario)
				Nueva_vivienda.save()
				#response = {'message': True}
			return HttpResponseRedirect("/ofertar/vivienda")

			#return HttpResponse(json.dumps(response), content_type="application/json")

		elif categoria=="empleo":
			sueldo=request.POST["Sueldo"]
			periodo=request.POST["Periodo"]	
			plazas=request.POST["Plazas"]	
			propietario="Juanpe"

			try:
				record=ActEmpleo.objects.get(Titulo=titul)
			except:
				Nueva_Empleo=ActEmpleo(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Sueldo=sueldo,Periodo=periodo,Plazas=plazas)
				Nueva_Empleo.save()			
			return HttpResponseRedirect("/ofertar/empleo")
		#else
			#except:
			#canal="<h1> la url del canal introducido no es valida</h1>"
			#template = get_template("configurar_canales.html")
			#diccionario = {'css_user':css,'usuario':enlace,'canal':canal}
			#return HttpResponse(template.render(Context(diccionario)))


def buscar(request,categoria):

	if request.method=="GET":		
									
		template = get_template("busqueda.html")		
		diccionario = {'categ':categoria}		
		return HttpResponse(template.render(Context(diccionario)))


	elif request.method == "POST":			
					
		ciudad=str(request.POST['provincia'])
		titulo=str(request.POST['titulo'])

		if categoria=="ocio":	
			precio=str(request.POST['precio'])
			fechaDesde=str(request.POST['fDesde'])
			fechaHasta=str(request.POST['fHasta'])
			aforo=str(request.POST['aMax'])
			direc= str(request.POST['direccion'])
			record=ActOcio.objects.all()
			
			if titulo!="":
				record=record.filter(Titulo__contains = titulo)
			if ciudad != "":
				record=record.filter(Ciudad=ciudad)
			if precio != "":
				record=record.filter(Precio=precio)
			if fechaDesde != "":
				record=record.filter(Fecha__gt=fechaDesde)
			if fechaHasta != "":
				record=record.filter(Fecha__lt=fechaHasta)
			if aforo != "":
				record=record.filter(Aforo_Max=aforo)
			if direc != "":
				record=record.filter(Direccion__contains=direc)

			if record != []:
				template = get_template("listado.html")		
				diccionario = {'record':record,'categoria':categoria}	
				return HttpResponse(template.render(Context(diccionario)))

			else:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))


		if categoria=="vivienda":	
			record=""
			precio=str(request.POST['precio'])
			numHab=str(request.POST['nHabit'])
			tipoOfer=str(request.POST["tipo"])
			direc= str(request.POST['direccion'])
			record=ActVivienda.objects.all()
			
			if titulo != "":
				record=record.filter(Titulo__contains = titulo)
			if ciudad != "":
				record=record.filter(Ciudad=ciudad)
			if precio != "":
				record=record.filter(Precio=precio)
			if tipoOfer != "":
				record=record.filter(TipoOferta=tipoOfer)
			if numHab != "":
				record=record.filter(NumHab=numHab)
			if direc != "":
				record=record.filter(Direccion__contains=direc)
	
			if record != []:
				template = get_template("listado.html")		
				print(categoria)
				diccionario = {'record':record,'categoria':categoria}	
				return HttpResponse(template.render(Context(diccionario)))

			else:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))


		if categoria=="empleo":	
			sueldo=str(request.POST['sueldo'])
			periodo=str(request.POST['periodo'])
			record=ActEmpleo.objects.all()
			
			if titulo != "":
				record=record.filter(Titulo__contains=titulo)
			if ciudad != "":
				record=record.filter(Ciudad=ciudad)
			if sueldo != "":
				record=record.filter(Sueldo=sueldo)
			if periodo != "":
				record=record.filter(Periodo=periodo)
		
			if record != []:
				template = get_template("listado.html")		
				diccionario = {'record':record,'categoria':categoria}	
				return HttpResponse(template.render(Context(diccionario)))

			else:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))




def calendario(request):
	if request.method == "GET":
		titulo="Calendario"
		template = get_template("enConstruccion.html")
		diccionario = {'titulo':titulo}
		
		return HttpResponse(template.render(Context(diccionario)))
