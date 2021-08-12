import streamlit as st
import pandas as pd
import numpy as np
import requests

st.set_page_config(layout="wide")

url="http://127.0.0.1:5000/"
operacion="get"
query ="Island"
st.write("Pinguinos!")

value = st.text_input('Island...')

if value:
    res = requests.get(f"{url}{operacion}?{query}={value}")
    respuesta = res.json()
    dfp = pd.DataFrame(respuesta)

    dfp = dfp.drop(columns=["Sample Number","index","Individual ID", "Clutch Completion", "Date Egg", "Island", "studyName"])





    st.write(dfp)