import streamlit as st
import sqlite3, datetime, time, os
from Train.main import Database


class Page1:
    def __init__(self):
        st.markdown("""
                                <h1 style='text-align: center;'><span style='color:red;'>OneSmarter</span>Booking.com</h1>
                                """, unsafe_allow_html=True)
        self.img = st.sidebar.image('3135715.png')
        self.user = st.sidebar.markdown("""
                                        <h1 style='text-align: center;'><span style='color:white;'>User</h1>
                                        """, unsafe_allow_html=True)
        self.page_selection = None
        self.db = Database()
        self.initialize()

    def initialize(self):
        col1, col2, col3, col4, col5 = st.columns(5)
        self.page_selection = col1.selectbox("", ["Login", "Register"])
        col3.button("Contact Us")
        current = datetime.datetime.now()
        col5.write(current.strftime('%d:%m:%Y'))
        if self.page_selection == "Login":
            self.login()
        elif self.page_selection == "Register":
            self.register()

    def login(self):
        st.markdown(''' 

            ### Login
            ''', True)
        log_email = st.text_input("Enter your email address")
        log_passw = st.text_input("Enter your password", type='password')
        print(log_email, log_passw)
        co1, co2 = st.columns(2)
        log_sub_button = co1.button('LOG-IN')
        if log_sub_button:
            email_exists = self.db.check_present(log_email, log_passw, 'User', 'email', 'Password')
            if email_exists:
                st.write('Login successfully👍')
                st.write('Redirecting to Hotel site')
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)
            else:
                st.write('Invalid username or password❌; new user? Go to Register')
        return log_passw, log_email

    def register(self):
        st.markdown(''' 
                    ### Register
                    ''', True)
        col1, col2 = st.columns(2)
        name = col1.text_input("Enter your name")
        email = col2.text_input("Enter you email address")
        phone = col1.text_input("Enter Phone Number")
        pass1 = col2.text_input("Enter one time password", type='password')
        pass2 = col1.text_input("Confirm password", type='password')
        upload = col2.file_uploader("Upload Profile Photo", type=('.png', '.jpg', '.jpeg'))
        if upload:
            col1.image(upload, caption='Uploaded Image')
            img_path = f"{name}.jpg"
            with open(img_path, "wb") as f:
                f.write(upload.read())
            st.success("Image has been saved to 'uploaded_image.jpg'")
        else:
            col1.image('3135715.png', caption='Default Image')
            img_path = '3135715.png'
        sub_button = col1.button('SIGN-UP')
        if sub_button:
            if name != '':
                email_exists = self.db.check_email(email, 'User', 'email')
                if str(email).endswith('@gmail.com') and not str(email).startswith('@gmail.com'):
                    if not email_exists:
                        if pass1 == pass2 and pass1 != '' and phone != '':
                            print(name, phone, email, pass2)
                            self.db.user_table(name, email, phone, img_path, pass2)
                            st.write("Your Account has been registered successfully👍")
                            if img_path != '3135715.png':
                                os.remove(img_path)
                            st.write('Redirecting to Hotel site')
                            progress_bar = st.progress(0)
                            for i in range(100):
                                time.sleep(0.05)
                                progress_bar.progress(i + 1)
                        else:
                            st.write('Password mismatch')
                    else:
                        st.write('User with this email already exists go to login')
                else:
                    st.write('Invalid email address')
            else:
                st.write("Invalid name")
        return name, phone, email, pass2


Page1()
