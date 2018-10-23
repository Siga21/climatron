#!/usr/bin/python
# -*- coding: iso-8859-15

import sqlite3
from libreria import * 


texto = "select nombre, apellidos from clinica_clientes"
registros = run_query(texto)

for i in range(len(registros)):
    nombre = registros[i][0]
    apellidos = registros[i][1]
    print 'El cliente es  : ' +  concatena(apellidos, nombre)






