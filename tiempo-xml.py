# -*- coding: utf-8 -*-
import requests
from lxml import etree
from jinja2 import Template
import webbrowser
print "Aplicación weather con entrada en XML y salida en HTML || OpenWeatherMap"
print ""

def cardinal(direccion):
	if (direccion >= 337.5 and direccion <= 360) or (direccion >= 0 and direccion <= 22.5):
		return 'N' 
	if direccion >= 22.5 and direccion <= 67.5:
		return 'NE'
	if direccion > 67.5 and direccion <= 112.5:
		return 'SE'
	if direccion > 112.5 and direccion <= 157.5:
		return 'S'
	if direccion > 157.5 and direccion <= 202.5:
		return 'SO'
	if direccion > 202.5 and direccion <= 245.5:
		return 'O'
	if direccion > 245.5 and direccion <= 292.5:
		return 'E'
	if direccion > 292.5 and direccion < 337.5:
		return 'NO'

fplantilla = open('plantilla.html','r')
plantilla = fplantilla
fresultado = open('resultado.html','w')

codigo = ''
for linea in plantilla:
	codigo += linea

alltemp_max = []
alltemp_min = []
allvelocidad = []
alldireccion = []
allpuntocardinal = []

prov = ['Almeria', 'Cadiz', 'Cordoba', 'Huelva', 'Jaen', 'Malaga', 'Sevilla']
for elemento in prov:
 	datos = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Seville&mode=xml&units=metric&lang=es')
 	cadena = etree.fromstring(datos.text.encode("utf8"))
 	temp = cadena.find("temperature")
 	temp_max = int(temp.attrib["min"])
 	temp_min = int(temp.attrib["max"])
 	print temp_max,temp_min
 	#velocidad = int(valores['wind']['speed']*1.609)
 	#direccion = valores['wind']['deg']
 	#puntocardinal = cardinal(direccion)
 	#alltemp_max.append(temp_max)
 	#alltemp_min.append(temp_min)
 	#allvelocidad.append(velocidad)
 	#allpuntocardinal.append(puntocardinal)

html = Template(codigo)
html = html.render(provincias=prov, temp_max=alltemp_max, temp_min=alltemp_min, velocidad=allvelocidad, direccion=allpuntocardinal,)
fresultado.write(html)

#webbrowser.open("resultado.html")