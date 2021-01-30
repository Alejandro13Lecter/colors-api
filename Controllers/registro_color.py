from flask import Flask, request, jsonify
from flask_restful import Resource, Api

import json


class RegistroController(Resource):
    def post(self):

        msg_received = request.get_json()
        color_id = msg_received["id"]
        name = msg_received["name"]
        year = msg_received["year"]
        color = msg_received["color"]
        pantone = msg_received["pantone"]

        response = jsonify({'code': 200,
                        'tipo': "ok",
                        })
        # Enable Access-Control-Allow-Origin
        response.headers.add("Access-Control-Allow-Origin", "*")

        return response