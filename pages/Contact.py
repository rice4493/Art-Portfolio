import streamlit as st

st.title("The Easel Gap")
st.header("Contact Me")

with st.form(key='email'):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    if button:
        st.info("Your email was sent successfully. Thank you for reaching out!")
