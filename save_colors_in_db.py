# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:12:46 2021

@author: rob
"""

import pandas as pd
from sqlalchemy import create_engine


"""Read the given csv and transform it
into a sql database.
In this case it will be local.
In order to do it to a global database,
credentials and hosting will be needed""" 

df = pd.read_csv('colors.csv')
print(df)

engine = create_engine('sqlite:///colores.db', echo=True)
conn = engine.connect()

table_name = "colores_api"
df.to_sql(table_name, conn, if_exists='fail')
conn.close()


