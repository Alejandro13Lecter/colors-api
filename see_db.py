# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:30:53 2021

@author: rob
"""

import sqlite3
import pandas as pd


try:
    conn = sqlite3.connect('colores.db')
    c = conn.cursor()
    colores_query = "SELECT * FROM colores_api"
    c.execute(colores_query)
    conn.commit()
    result = c.fetchall()
    print(result)

except (Exception, sqlite3.Error) as error :
    if(conn):
        print("Failed in communication", error)
    else:
        print("No connection", error)
            
if(conn):
    print ("Data processed and saved")
    print("Commit done........")

    c.close()
    conn.close()
    print("Connection is closed")

