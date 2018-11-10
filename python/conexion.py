#!/usr/bin/python
# -*- coding: iso-8859-15

import sqlite3
from libreria import * 

# bucle de los sensores de temperatura 
texto = """select id, ip 
           from clima_sensor 
           order by planta_id"""
registros = run_query(texto)
for i in range(len(registros)):
	ide = registros[i][0]
	ip = registros[i][1]
    #con la ip vamos a leer el sensor y recogemos la temperatura 
	grados = leer_esp8266(ip)
	#grados = 19.12  # fijo mientras no se lean sensores de verdad  			
	actualizar_sensor(ide, grados)
	print "Actualizado sensor : " + str(ide)
	#grabamos registro en historico de sensores 
	linea_historico_sensor(ide, grados)
	print "Añadido a historico sensor : " + str(ide)	

	
print "fin de programa..."
               
               





