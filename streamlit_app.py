import streamlit as st
import pandas as pd

st.write(""" 
#My first app
""")

sysBP = st.number_input(label="systolic blood pressure",step=1.,format="%.2f")


