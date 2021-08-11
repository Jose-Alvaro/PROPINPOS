from utils.handle_error import handle_error
from utils.json_response import json_response
from app import app
from flask import request
from sqlalchemy import create_engine
from bbdd import *


@app.route("/get")
@handle_error
def get():
    argu=dict(request.args)
    print (argu["index"])

    #postgres_url = f'postgresql+psycopg2://postgres:123@localhost:5432'
    #engine = create_engine(f"{postgres_url}/ProPinPos")
    #connection = engine.connect()
    #consulta = list(connection.execute(f'SELECT * FROM public."Pingu" WHERE "index"= {argu["index"]}'))

    sqlconsult = f'SELECT * FROM public."Pingu" WHERE "index"= {argu["index"]}'
    resconsulta = leer(sqlconsult)

    pingcont = ["index", "studyName", "Sample Number", "Species", "Island", "Individual ID", "Clutch Completion", "Date Egg", "Culmen Length (mm)", "Culmen Depth (mm)", "Flipper Length (mm)","Body Mass (g)", "Sex"]
    pinguino = {}

    for elemento in range(len(pingcont)):
        pinguino[pingcont[elemento]]=resconsulta[0][elemento]

    return json_response(pinguino)
    
    
@app.route("/post")
@handle_error
def post():
    pid = request.args.get("Individual ID")
