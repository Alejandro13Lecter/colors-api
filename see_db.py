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
    #connect to database
    conn = sqlite3.connect('colores.db')
    #convert the table of the db to a dataframe for easier manipulation
    df = pd.read_sql_query("SELECT * FROM colores_api", conn)
    #show it in console
    print(df)
    
        

except (Exception, sqlite3.Error) as error :
    if(conn):
        print("Failed in communication", error)
    else:
        print("No connection", error)
            
if(conn):

    conn.close()
    print("Connection is closed")