# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:30:53 2021

@author: rob
"""

import sqlite3
import pandas as pd

"""Test if the database was created and
see its content whenever is required"""

try:
    conn = sqlite3.connect('colores.db') 
    df = pd.read_sql_query("SELECT * FROM colores_api", conn)
    print(df)
    
    
    
    df2 = df[["id", "name", "color"]]
    colores = df2.apply(lambda x: x.to_json(), axis=1)
    
    
    response = []
    for x in range(len(colores)):
        response.append(colores[x])
    
    print(response)
        

except (Exception, sqlite3.Error) as error :
    if(conn):
        print("Failed in communication", error)
    else:
        print("No connection", error)
            
if(conn):

    conn.close()
    print("Connection is closed")

