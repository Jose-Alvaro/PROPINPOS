from utils.handle_error import handle_error
from utils.json_response import json_response
from app import app
from flask import request

# Función controladora
@app.route("/")
@handle_error
def ejemplo():
    alumno = {
        "name":"pepe22"
    }
    return json_response(alumno)


@app.route("/saludo")
@handle_error
def saludo_fn():
    print("terminal")
    print(request.args)
    name = request.args.get("name")
    surname = request.args.get("surname")
    #raise ValueError("MEC")
    return {
        "name":"EMOJI" + name,
        "surname":surname,
    }
