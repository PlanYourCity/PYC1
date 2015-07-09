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

# Create your views here.
#def Detalles(request):
def lista_eventos(request):

	if request.method == "GET":
		lista_actividades=[]
		#event= ActOcio(Titulo="Concierto",Direccion="puerta del sol",Precio="30 $",Aforo_Max="completo",Hora="15:00",Imagen="../../static/images/imagen.png",Descripcion="lssdfsdf",Categoria="dsadas",Usuario_owner="ffsd",Tipo_User="E")	
		#event.save()
		#event1= ActOcio(Ciudad="Madrid", Titulo="Ruta Retiro",Direccion="Parque Retiro, Madrid",Precio="30")	
		#event1.save()
		
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
<<<<<<< HEAD
=======
		#try:			
		nom=request.POST['nombre']			
		act=request.POST['activ']
			
		try:
			record=ActOcio.objects.get(Titulo=nom,Direccion=act)
		except:
			Nueva_actividad=ActOcio(Titulo=nom,Direccion=act)
			Nueva_actividad.save()			
		return HttpResponseRedirect('/ofertar')		
		#except:
			#canal="<h1> la url del canal introducido no es valida</h1>"
			#template = get_template("configurar_canales.html")
			#diccionario = {'css_user':css,'usuario':enlace,'canal':canal}
			#return HttpResponse(template.render(Context(diccionario)))

def buscar(request):
	if request.method == "GET":
		titulo="Buscar"
		template = get_template("busqueda.html")
		diccionario = {'titulo':titulo}
>>>>>>> 4ebf52830926bb48d9267e9837558823ef291b9f
		
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
			return HttpResponseRedirect('/ofertar/ocio')
		elif categoria=="vivienda":
			imagen=request.POST['Imagen']
			precio=request.POST['Precio']
			nhabit=request.POST['NumHab']	
			toferta=request.POST['TipoOferta']		
			propietario='Fabio'
			try:
				record=ActVivienda.objects.get(Titulo=titulo)
			except:
				Nueva_vivienda=ActVivienda(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Imagen=imagen,Precio=precio,NumHab=nhabit,Usuario_owner=propietario)
				Nueva_vivienda.save()			
			return HttpResponseRedirect('/ofertar/vivienda')

		elif categoria=="empleo":
			sueldo=request.POST["Sueldo"]
			periodo=request.POST["Periodo"]	
			plazas=request.POST["Plazas"]	
			propietario="Juanpe"

			try:
				record=ActEmpleo.objects.get(Titulo=titulo)
			except:
				Nueva_Empleo=ActEmpleo(Ciudad=ciuda,Direccion=direccio,Titulo=titul,Descripcion=descripcio,Sueldo=sueldo,Periodo=periodo,Plazas=plazas)
				Nueva_Empleo.save()			
			return HttpResponseRedirect('/ofertar/empleo')


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
			record=ActOcio.objects.all()
			try:
				if titulo != "":
					record=record.objects.filter(Titulo=titulo)
				if ciudad != "":
					record=record.objects.filter(Ciudad=ciudad)
				if precio != "":
					record=record.objects.filter(Precio=precio)
				if fechaDesde != "":
					record=record.objects.filter(Fecha__gt=fechaDesde)
				if fechaHasta != "":
					record=record.objects.filter(Fecha__lt=fechaHasta)
				if aforo != "":
					record=record.objects.filter(Aforo_Max=aforo)
		
				template = get_template("listado.html")		
				diccionario = {'record':record}	
				return HttpResponse(template.render(Context(diccionario)))

			except:
				print("estoy aqui")
				template = get_template("listado.html")		
				return HttpResponse(template.render(Context("No existe actividad que cumpla los requisitos")))

		elif categoria=="vivienda":	
			try:
				record=ActOcio.objects.get(Titulo=nom)
			except:
				Nueva_actividad=ActOcio(Titulo=nom,Direccion=act)
				Nueva_actividad.save()			
			return HttpResponseRedirect('/ofertar')	

		elif categoria=="empleo":	
			try:
				record=ActOcio.objects.get(Titulo=nom)
			except:
				Nueva_actividad=ActOcio(Titulo=nom,Direccion=act)
				Nueva_actividad.save()			
			return HttpResponseRedirect('/ofertar')


def calendario(request):
	if request.method == "GET":
		titulo="Calendario"
		template = get_template("enConstruccion.html")
		diccionario = {'titulo':titulo}
		
		return HttpResponse(template.render(Context(diccionario)))
