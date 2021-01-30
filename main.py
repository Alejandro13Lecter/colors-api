# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:32:25 2021

@author: rob
"""

from flask import Flask, jsonify, render_template
from flask_restful import Resource, Api
from flask_cors import cross_origin


from Controllers import registro_color


import sys
import json
import sqlite3


app = Flask(__name__)
api = Api(app)
print('### Server Running ###')
app.config['SECRET_KEY'] = 'multiplica'


@app.route('/')
def index():
    """Home page as reference"""
    return render_template('index.html')
    #return jsonify({'code': 200, "data": "servidor correctamente"})


@app.route('/colores', methods=['GET'])
@cross_origin()
def ShowColors():
    """Regresa la colección de colores disponibles con la siguiente información
    ID
    Name
    Color"""
    
    #Do database stuff to show all
    try:
        conn = sqlite3.connect('colores.db')
        c = conn.cursor()
        colores_query = "SELECT ID, Name, Color FROM colores"
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
    
    response = jsonify({'code': 200})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



api.add_resource(registro_color.RegistroController, '/registro_color')


if __name__ == '__main__':
	app.run(host="192.168.0.23", port=5000, threaded=True)