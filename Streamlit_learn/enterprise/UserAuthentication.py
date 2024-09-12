import time

import streamlit as st
import sqlite3
import log


class Login:

    def __init__(self):

        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                            id INTEGER PRIMARY KEY,
                            username TEXT,
                            email TEXT,
                            PhoneNo TEXT,
                            Password TEXT
                        )''')

    def general(self):
        st.markdown(''' 
        <!DOCTYPE html>
        <html>
        <head>
            <title>Hotel Home Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                }
                .header {
                    text-align: center;
                    padding: 10px;
                    background-color: #f8f9fa;
                }
                .content {
                    margin: 20px;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Welcome to Our Hotel</h1>
            </div>
            <div class="content">
                <h2>About Us</h2>
                <p>We offer the best services for your comfort and satisfaction.</p>
                <h2>Our Rooms</h2>
                <p>We have a variety of rooms to suit your needs and preferences.</p>
                <h2>Contact Us</h2>
                <p>For any inquiries or reservations, please contact us at <span style='font-style:italic; color:red'><a href="">HotelOneSmarter.com</a></span>.</p>
            </div>
        </body>
        </html>
        ''', True)
        pass

    def register(self):
        st.markdown('''
                        ### Register
                        ''', True
                    )
        col1, col2 = st.columns(2)
        name = col1.text_input("Enter your name")
        email = col2.text_input("Enter you email address")
        phone = col1.text_input("Enter Phone Number")
        pass1 = col2.text_input("Enter one time password", type='password')
        pass2 = col1.text_input("Confirm password", type='password')
        sub_button = col1.button('SIGN-UP')
        if sub_button:
            if name != '':
                if '@gmail.com' in email:
                    if pass1 == pass2 and pass1 != '' and phone != '':
                        print(name, phone, email, pass2)
                        self.cursor.execute("INSERT INTO User (username, email, PhoneNo, Password) VALUES (?, ?, ?, ?)",
                                            (name, email, phone, pass2))
                        self.connection.commit()
                    else:
                        st.write('Password mismatch')
                else:
                    st.write('Invalid email address')
            else:
                st.write("Invalid name")


st.markdown("""
                        <h1 style='text-align: center;'>Hotel <span style='color:red;'>OneSmarter</span></h1>
                        """, unsafe_allow_html=True)
Login().general()
btn1 = st.sidebar.button("Login")
btn2 = st.sidebar.button("Register")

if btn1:
    log.login()
elif btn2:
    Login().register()
