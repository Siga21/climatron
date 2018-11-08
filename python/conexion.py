#!/usr/bin/python
# -*- coding: iso-8859-15

import sqlite3
from datetime import datetime
from libreria import * 

texto = """select nombre_sensor, clima_planta.nombre_planta 
           from clima_sensor 
           inner join clima_planta 
           on clima_sensor.planta_id = clima_planta.id 
           order by clima_sensor.planta_id"""
registros = run_query(texto)

for i in range(len(registros)):
    nombre = registros[i][0]
    planta = registros[i][1]
    print "El sensor es  : " +  nombre + " Planta: " + planta 


grados = 25.72

escritura = "update clima_sensor set ultima_temperatura = "  + str(grados) + ", fecha_lectura = '" + str(datetime.now()) + "'   where id = 1"
run_write(escritura)

print "fin"
               
               





