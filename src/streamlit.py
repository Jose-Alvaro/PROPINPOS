import streamlit as st
import pandas as pd
import numpy as np
import requests


url="http://127.0.0.1:5000/"
operacion="get"
query ="Island"
st.write("Pinguinos!")

islands = ["Torgersen","Biscoe","Dream"]
value = st.radio('Island of...', islands)

if value:
    res = requests.get(f"{url}{operacion}?{query}={value}")
    respuesta = res.json()
    dfp = pd.DataFrame(respuesta)

    dfp = dfp.drop(columns=["index","Sample Number","Individual ID", "Clutch Completion", "Date Egg", "studyName"])





    st.write(dfp)