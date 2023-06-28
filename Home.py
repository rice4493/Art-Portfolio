import streamlit as st
import base64

st.title("The Easel Gap")
# st.image('images/pexels-cottonbro-studio-7885582.jpg')


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
       <style>
       .stApp {
       background-image: url("data:image/png;base64,%s");
       background-size: cover;
       }
       </style>
       ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)


filepath = 'images/pexels-cottonbro-studio-7885582.jpg'
set_background(filepath)


intro = '''
Hi! Welcome to my little corner of the internet where I share my artistic journey.
'''
st.subheader(intro)

st.header("About me")

about = '''
I'm Yukta Noela, a self-taught artist based in Bangalore, India, 
with a deep-rooted passion for art that has persisted since my childhood.
Over the years, this passion has evolved and grown, becoming an integral part of my identity. 
In 2017, during my summer holidays when i found myself with ample free time, I embarked on an artistic journey,
delving into the world of painting. 
Initially i started with watercolour paints as a beginner, I gradually honed my skills and progressed as an artist,
transitioning into working with oil paints. \n\n
Art has become not just a pastime but a profound purpose in my life, fundamentally shaping the way I perceive the world.
It has empowered me to express my emotions, thoughts, and observations in a visual language that transcends barriers.
Through dedication, continuous learning, and an unwavering commitment to my craft, I strive to push the boundaries 
of my artistic capabilities and leave a lasting impression on those who engage with my work.
'''

st.write(about)

col1, col2 = st.columns(2)

with col1:
    gallery = st.button("View Gallery")

with col2:
    contact = st.button("Contact Me")

st.header("The Easel Gap")
st.title("Store Coming Soon!")
