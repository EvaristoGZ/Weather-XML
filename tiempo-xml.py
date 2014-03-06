# -*- coding: utf-8 -*-
import requests
from lxml import etree
from jinja2 import Template
import webbrowser
print "Aplicación weather con entrada en XML y salida en HTML || OpenWeatherMap"
print ""

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
 	velocidad = cadena.find("wind/speed")
 	velocidad = velocidad.attrib["value"]
 	direccion = cadena[4][1].attrib["code"]
 	alltemp_max.append(temp_max)
 	alltemp_min.append(temp_min)
 	allvelocidad.append(velocidad)
 	allpuntocardinal.append(direccion)

html = Template(codigo)
html = html.render(provincias=prov, temp_max=alltemp_max, temp_min=alltemp_min, velocidad=allvelocidad, direccion=allpuntocardinal,)
fresultado.write(html)

webbrowser.open("resultado.html")