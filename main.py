# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:32:25 2021

@author: rob
"""

from flask import Flask, jsonify, render_template
from flask_restful import Api
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
    """Return collection of available colors with the following information 
    ID
    Name
    Color"""
    
    #Do database stuff to show all
    try:
        conn = sqlite3.connect('colores.db')
        df = pd.read_sql_query("SELECT * FROM colores_api", conn)
        df2 = df[["id", "name", "color"]]
        
        colores = df2.apply(lambda x: x.to_json(), axis=1)
        
    except (Exception, sqlite3.Error) as error :
        if(conn):
            print("Failed in communication", error)
        else:
            print("No connection", error)
            
    if(conn):
        conn.close()
        print("Connection is closed")
    
    response = colores
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response



api.add_resource(registro_color.RegistroController, '/registro_color')


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5005, threaded=True)