import streamlit as st


def login():
    st.markdown(''' 

        ### Login
        ''', True)
    log_email = st.text_input("Enter your email address")
    log_passw = st.text_input("Enter your password", type='password')
    log_sub_button = st.button('LOG-IN')
