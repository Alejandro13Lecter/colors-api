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
app.config['SECRET_KEY'] = 'multiplica'


@app.route('/')
def index():
    """
    Home page as reference
    """
    return jsonify({'code': 200, "data": "servidor correctamente"})



@app.route('/colores', methods=['GET'])
@cross_origin()
def ShowColors():
    """
    Return collection of available colors with the following information 
    ID
    Name
    Color
    """
    
    #Do database stuff to show all
    try:
        conn = sqlite3.connect('colores.db')
        df = pd.read_sql_query("SELECT * FROM colores_api", conn)
        df2 = df[["id", "name", "color"]]
        
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
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route('/colores/<id>', methods=['GET'])
@cross_origin()
def ShowColorById(id):
    """
    Return on resource according to specified id 
    """
    
    color_id = id #string
    
    #Do database stuff to show all
    try:
        conn = sqlite3.connect('colores.db')
        cursor = conn.cursor()

        select_query = "SELECT * FROM colores_api WHERE id = " + id
        cursor.execute(select_query)
        conn.commit()
        result = cursor.fetchone()
        
        if result is not None:
                print(result)
                message = result
        else:
            response = jsonify({"error": "color no existente"})
            response.headers.add("Access-Control-Allow-Origin", "*")
            return response
            
        
    except (Exception, sqlite3.Error) as error :
        if(conn):
            print("Failed in communication", error)
        else:
            print("No connection", error)
            
    if(conn):
        conn.close()
        print("Connection is closed")
    response = jsonify({"id": result[1], "name": result[2], 
                        "year": result[3], "color": result[4],
                        "pantone_value": result[5]})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



api.add_resource(registro_color.RegistroController, '/registro_color')


if __name__ == '__main__':
    app.debug= True
    app.run(host='localhost')