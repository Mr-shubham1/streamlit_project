import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("this is title")
st.header("this is header")
st.subheader("this is subheader")


st.write("this is text")
st.markdown("this is markdown")
st.caption("this is caption")

st.image("./myProfilephoto.jpg")


st.checkbox("checkbox")
st.button("click here")

st.radio("pick your city",["varanasi","prayagraj","Lucknow","Hyderabad"])
st.selectbox("pick your city",["varanasi","prayagraj","Lucknow","Hyderabad"])
st.multiselect("pick your city",["varanasi","prayagraj","Lucknow","Hyderabad"])

st.select_slider('Give a Remark', ['Bad', 'Good','better','best', 'Excellent'])
st.slider('Your Marks', 0,100)

toggle_on = st.toggle("activate shsfgs")
if toggle_on :
    st.write("shsfgs feature activated")

number = st.number_input("insert a number")
if number :
    st.write("entered number is ",number)

dob = st.date_input("enter your birthday")
if dob :
    st.write("your birthday is ", dob)

