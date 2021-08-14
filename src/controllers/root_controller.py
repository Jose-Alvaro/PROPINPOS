from utils.handle_error import handle_error
from utils.json_response import json_response
from app import app
from flask import request
from sqlalchemy import create_engine
from bbdd import *

@app.route("/")
@handle_error
def saludo():
    return "Hola"

@app.route("/get")
@handle_error
def get():
    argu=dict(request.args)

    columnas= []
    values=[]

    for key, value in argu.items():
        columnas.append(key)
        values.append(value)

    sqlwhere = "WHERE "

    for pos in range(len(columnas)):
        if columnas[pos] in ["index" , "Sample Number" , "Culmen Length (mm)" , "Culmen Depth (mm)" , "Flipper Length (mm)" , "Body Mass (g)"]:
            sqlwhere += f' "{columnas[pos]}" = {values[pos]} or '
        else:
            sqlwhere += f' "{columnas[pos]}" = '+ f"'{values[pos]}' or "
    sqlwhere = sqlwhere[:-4]

    sqlconsult = f'SELECT * FROM public."Pingu" {sqlwhere}'
    print(sqlconsult)
    resconsulta = leer(sqlconsult)

    pingcont = ["index", "studyName", "Sample Number", "Species", "Island", "Individual ID", "Clutch Completion", "Date Egg", "Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)","Body Mass (g)", "Sex"]
    
    manada = []
    for pin in range(len(resconsulta)):
        pinguino = {}
        for elemento in range(len(pingcont)):
            pinguino[pingcont[elemento]]=resconsulta[pin][elemento]
        manada.append(pinguino)

    return json_response(manada)
    
@app.route("/post")
@handle_error
def post():
    argu=dict(request.args)
        
    sqlconsult = f'INSERT INTO public."Pingu" ({argu[""]}) VALUES ({argu[""]});'

    return json_response(pinguino)

@app.route("/update")
@handle_error
def update():
    argu=dict(request.args)

    sqlconsult = f'UPDATE public."Pingu" SET WHERE "{argu[""]}"= {argu[""]}'

    return json_response(pinguino)

@app.route("/delete")
@handle_error
def delete(): 
    argu=dict(request.args)

    sqlconsult = f'DELETE FROM public."Pingu" WHERE "{argu[""]}"= {argu["index"]}'

    return json_response(pinguino)


