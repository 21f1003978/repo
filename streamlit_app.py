import streamlit as st
import pandas as pd

st.write(""" 
#My first app
""")

sysnum1 = st.number_input(label=""“
                          Provide first number”,step=1.,format="%.2f
                          """)
sysnum2 = st.number_input(label=""“
                          Provied second number ”,step=1.,format="%.2f
                          """)


