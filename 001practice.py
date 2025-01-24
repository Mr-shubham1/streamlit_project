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


t = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", t)

st.number_input('Enter your marks', 0,100)
st.text_input('Enter Text')
st.date_input('Exam date')
st.time_input('Exam time')
st.text_area('Description')
st.file_uploader('Upload File')
st.color_picker('Choose a color')

st.success("Success")
st.error("Error")
st.warning("Warning")
st.info("Information")
st.exception(RuntimeError("RuntimeError exception"))

st.sidebar.title("5 Minutes Engineering")
st.sidebar.image("./myProfilephoto.jpg")

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df)


df = pd.DataFrame(
    np.random.randn(10, 5), columns=("col %d" % i for i in range(5))
)
st.table(df)

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
    
    

with st.status("Step 1"):
    st.write("Step 2")
    time.sleep(1)
    st.write("Step 3")
    time.sleep(1)
    st.write("Step 4")
    time.sleep(1)
st.button("Rerun")


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.area_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.bar_chart(chart_data)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

df = pd.DataFrame({
    "lat" : [123],
    "lon" : [456]
})
st.map(df)

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)

with st.chat_message("user"):
    st.write("Hello ji")
