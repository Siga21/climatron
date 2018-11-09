#!/usr/bin/python
# -*- coding: iso-8859-15

import sqlite3
#import requests  #es necesario instalar la libreria requests
from datetime import datetime


# ejecuta consultas sqlite3 sobre una base y devuelve array de registros 
# parametro : sentencia SQL SELECT
def run_query(query):

    conn = sqlite3.connect('../climatron/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


# ejecuta INSERT INTO o UPDATE sqlite3 sobre una base y devuelve Null
# parametro : sentencia SQL INSER o UPDATE 
def run_write(query):

    conn = sqlite3.connect('../climatron/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)

    conn.commit()

    conn.close()

    return None 

# actualiza la temperatura y fecha de lectura del sensor  
# parametros :  id del sensor y temperatura     
def actualizar_sensor(int_id, flt_grados):

	escritura = "update clima_sensor set ultima_temperatura = "  + str(flt_grados) + ", fecha_lectura = '" + str(datetime.now()) + "'   where id = " + str(int_id)
	run_write(escritura)    
    
	return None 

# añade un registro al historico de sensores  
# parametros :  id del sensor y temperatura     
def linea_historico_sensor(int_id, flt_grados):

	escritura = "insert into clima_historico (fecha, sensor_id, temperatura) values ('" + str(datetime.now()) + "', " + str(int_id) + ", " + str(flt_grados) + ")"
	run_write(escritura)    
    
	return None 

	    
	    
# lee un sensor y devuelve la temperatura 
# parametros : id del sensor     

#def leer_esp8266(ip):
#	camino = "http://" + ip  + "/Python"
#	response = requests.get(camino)
#	fvalor = float(response.text)      #convierto el valor de la temperatura a float otra vez

#	return fvalor
	

