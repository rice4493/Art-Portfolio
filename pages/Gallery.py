import streamlit as st
import pandas

st.title("The Easel Gap")
st.header("Gallery")
st.subheader("A quick look into my previous work...")

df = pandas.read_csv('images.csv')

for index, row in df.iterrows():
    st.caption(row['title'])
    st.write(row['description'])
    st.image(row['image'])
