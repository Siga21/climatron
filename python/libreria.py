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


# ejecuta INSERT INTO o ADD sqlite3 sobre una base y devuelve Null
def run_write(query):

    conn = sqlite3.connect('../climatron/db.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)

    conn.commit()

    conn.close()

    return None 
    
    
    


