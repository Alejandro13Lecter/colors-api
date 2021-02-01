from flask import Flask, request, jsonify
from flask_restful import Resource, Api

import json
import sqlite3


class RegistroController(Resource):
    """
    Register a new color by a POST method.
    It requires a json with fields
    name string, 
    year int, 
    color string,
    pantone string
    """
    def get(self):
        #verifies that the route exists
        return jsonify({'code': 200, "data": "servidor correctamente"})

    def post(self):
        #request json
        msg_received = request.get_json()
        name = msg_received["name"]
        year = msg_received["year"]
        color = msg_received["color"]
        pantone = msg_received["pantone"]


        try:
            #connect to database
            conn = sqlite3.connect('colores.db')
            cursor = conn.cursor()
            #query to know if the color exists or is a valid register 
            cursor.execute("SELECT * FROM colores_api where name = ?",  (name,))
            result = cursor.fetchone()
            if result is not None:
                validation = False
                message = "El color ya existe"
            else:
                #color doesn't exists so follow the rgister process
                cursor.execute(''' SELECT MAX(id) FROM colores_api''')
                result = cursor.fetchone()
                new_color_id = 1 + int(result[0])
                #add new color to database
                insert_query = ''' INSERT INTO colores_api ("index", id, "name", "year", color, pantone_value)
                                    VALUES (?, ?, ?, ?, ?, ?) '''
                data = [result[0], new_color_id, name, year, color, pantone]
                data = tuple(data)
                cursor.execute(insert_query, data)
                conn.commit()
                validation = True
                message = "Registro de color exitoso"
            
        
        except (Exception, sqlite3.Error) as error :
            if(conn):
                print("Failed in communication", error)
            else:
                print("No connection", error)
            
        if(conn):
            conn.close()
            print("Connection is closed")
        
        response = jsonify({'validation': validation, "message": message})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response