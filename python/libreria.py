#!/usr/bin/python
# -*- coding: iso-8859-15

import sqlite3

# ejecuta consultas sqlite3 sobre una base y devuelve array de registros 
def run_query(query):

    conn = sqlite3.connect('../climatron/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data

#funcion chorra para hacer prubas    
def concatena(nombre_1, nombre_2):
	data = nombre_1 + ',' + nombre_2
	
	return data
	    
