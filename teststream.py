import streamlit as st
import pandas as pd
import datetime as dt

df = pd.read_csv("sensor.csv")

#df1 = df.drop(['unnamed'],axis=1)
 
st.write(" " "Manesh's Water Level Monitoring!" " ")

st.write("Water level chart")
st.line_chart(df['y'])
st.write("Entire HighLighted DB")
st.dataframe(df.style.highlight_max(axis=0))
l=[0,10,20,40,70,95]
st.write("You can check some border equal values using the frequently checked values below")
n=st.radio("frequently checked values",l)
if n in l:
    st.write("Your selected value list is here!")
    st.write(df.query("y==@n"))

min = st.sidebar.number_input("From level",min_value=10)
max = st.sidebar.number_input("To level",min_value=10,value=95)
if min>max:
    st.error("please enter a valid range")
else:
    st.write("Your range query result is here!")
    st.write(df.query("@min<=y<=@max"))

x = dt.datetime.now().strftime('%c')
df['z'] = pd.to_datetime(df['z'],format="%d-%m-%Y")

d3 = st.date_input("range",[dt.date(2021,1,9) , dt.date(2021,1,9)])
#st.write(d3)
min1 = d3[0]
max1 = d3[1]
if max1>=min1:
    st.write(df.query("@min1<=z<=@max1"))
else:
    st.write("To date is shorter than from date ")

pic ="PSX_20201122_184952.jpg"

st.image(pic)


st.write(" " " Designed and developed by lakshman_manesh" " ")
