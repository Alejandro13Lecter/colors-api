from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json



class RegistroController(Resource):
    def get(self):

        response = jsonify({'code': 200,
                        'tipo': "ok",
                        })
        # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response