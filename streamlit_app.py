import streamlit as st
import pandas as pd

st.write(""" 
#My first app
""")

num_1 = st.number_input(label="Enter number#1",step=1.,format="%.2f")
num_2 = st.number_input(label="Enter number#2",step=1.,format="%.2f")


