import streamlit as st
import pickle 

st.title("Weather prediction app..")
pn=st.number_input("enter precitipitation")
maxt=st.number_input("enter max ")
mint=st.number_input("enter min ")
wind=st.number_input("enter wind speed ")
button=st.button("predict")
if button:
    lr=pickle.load(open("wp.pkl","rb"))
    res=lr.predict([[pn,maxt,mint,wind]])[0]
    st.markdown(f"today weather situation:(res)")