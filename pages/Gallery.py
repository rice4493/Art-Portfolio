import streamlit as st
import pandas as pd
import os

st.title("The Easel Gap")
st.header("Gallery")
st.subheader("A quick look into my previous work...")

csv_path = os.path.join(os.path.dirname(__file__), 'images.csv')
df = pd.read_csv(csv_path)

image_folder = os.path.join(os.path.dirname(__file__), 'D:\Art Portfolio-web', 'images')

rows_with_zero_image = df[df['image'] == '0']

for index, row in df.iterrows():
    st.caption(row['title'])
    st.write(row['description'])
    image_path = os.path.join(image_folder, row['image'])
    st.image(image_path)
