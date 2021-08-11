import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import numpy as np

postgres_url = f'postgresql+psycopg2://postgres:123@localhost:5432'
engine = create_engine(f"{postgres_url}/ProPinPos")
engine.connect()

st.text('This is a text')
pingu=pd.read_sql("SELECT * FROM Pingu",engine)