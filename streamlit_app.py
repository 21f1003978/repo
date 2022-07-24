import streamlit as st

st.write(""" 
#My first app
""")

num_1 = st.number_input(label="Enter number#1",step=1.,format="%.2f")
num_2 = st.number_input(label="Enter number#2",step=1.,format="%.2f")

num_3 = num_1 + num_2
st.metric(label="Addition is", value=num_3,delta_color="inverse")

