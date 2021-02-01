# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:32:25 2021

@author: rob
"""

from flask import Flask, jsonify, render_template
from flask_restful import Api
from flask_cors import cross_origin

from Controllers import registro_color

import json
import sqlite3
import pandas as pd


app = Flask(__name__)
api = Api(app)
print('### Server Running ###')


@app.route('/')
def index():
    """
    Home page as reference.
    A button will show all the colors in json format.
    """
    return render_template('index.html')



@app.route('/colores', methods=['GET'])
@cross_origin()
def ShowColors():
    """
    Return a json of available colors with the following information 
    ID
    Name
    Color
    """
    
    try:
        #connect to database
        conn = sqlite3.connect('colores.db')
        #query all colors into a dataframe
        df = pd.read_sql_query("SELECT * FROM colores_api", conn)
        df2 = df[["id", "name", "color"]]
        #transform table format into json format
        colores = df2.apply(lambda x: x.to_json(), axis=1)
        response = {}
        for x in range(len(colores)):
            response[x] = colores[x]
            
        
    except (Exception, sqlite3.Error) as error :
        if(conn):
            print("Failed in communication", error)
        else:
            print("No connection", error)
            
    if(conn):
        conn.close()
        print("Connection is closed")
        
    response = jsonify(response)
    #add a header if cors
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/colores/<id>', methods=['GET'])
@cross_origin()
def ShowColorById(id):
    """
    Return on resource according to specified id in route
    """
    
    color_id = id #string
    
    try:
        #connect to database
        conn = sqlite3.connect('colores.db')
        cursor = conn.cursor()
        #query specified color
        select_query = "SELECT * FROM colores_api WHERE id = " + id
        cursor.execute(select_query)
        conn.commit()
        #save result
        result = cursor.fetchone()
        
        if result is not None:
                message = result
        else:
            return jsonify({"error": "color no existente"})
            
        
    except (Exception, sqlite3.Error) as error :
        if(conn):
            print("Failed in communication", error)
        else:
            print("No connection", error)
            
    if(conn):
        conn.close()
        print("Connection is closed")
    #present the result in required manner
    response = jsonify({"id": result[1], "name": result[2], 
                        "year": result[3], "color": result[4],
                        "pantone_value": result[5]})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


#route to register a new color
api.add_resource(registro_color.RegistroController, '/registro_color')


if __name__ == '__main__':
    #app.debug= True
    app.run(host='localhost')