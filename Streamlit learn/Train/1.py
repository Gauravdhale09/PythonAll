import streamlit as st
import datetime, time
import sqlite3, os
from PIL import Image
import math
from streamlit_searchbar import streamlit_searchbar


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
        self.db_path = 'Database.sqlite3'
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                                    id INTEGER PRIMARY KEY,
                                    username TEXT,
                                    email TEXT,
                                    PhoneNo TEXT,
                                    Profile BLOB,
                                    Password TEXT
                                )''')
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

    def check_present(self, email, password, table_name, email_column, password_column):
        query = f"SELECT * FROM {table_name} WHERE {email_column} = ? AND {password_column} = ?"
        self.cursor.execute(query, (email, password))
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

    def login(self):
        global email_main
        st.markdown(''' 

            ### Login
            ''', True)
        log_email = st.text_input("Enter your email address")
        log_passw = st.text_input("Enter your password", type='password')
        print(log_email, log_passw)
        co1, co2 = st.columns(2)
        log_sub_button = co1.button('LOG-IN')
        if log_sub_button:
            email_exists = self.check_present(log_email, log_passw, 'User', 'email', 'Password')
            if email_exists:
                st.write('Login successfully👍')
                email_main = log_email
                st.write('Redirecting to Hotel site')
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.05)
                    progress_bar.progress(i + 1)

                result = Page2(log_email).profile(log_email, 'User', 'email', 'Profile')
                self.user = result[0]
                self.img = result[1]
            else:
                st.write('Invalid username or password❌; new user? Go to Register')
        return log_passw, log_email

    def check_email(self, email, table_name, email_column):
        query = f"SELECT * FROM {table_name} WHERE {email_column} = ?"
        self.cursor.execute(query, (email,))
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

    def register(self):
        global email_main
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
                email_exists = self.check_email(email, 'User', 'email')
                if str(email).endswith('@gmail.com') and not str(email).startswith('@gmail.com'):
                    if not email_exists:
                        if pass1 == pass2 and pass1 != '' and phone != '':
                            print(name, phone, email, pass2)
                            self.cursor.execute(
                                "INSERT INTO User (username, email, PhoneNo, Profile, Password) VALUES (?, ?, ?, ?, ?)",
                                (name, email, phone, img_path, pass2))
                            self.connection.commit()
                            st.write("Your Account has been registered successfully👍")
                            if img_path != '3135715.png':
                                os.remove(img_path)
                            st.write('Redirecting to Hotel site')
                            progress_bar = st.progress(0)
                            for i in range(100):
                                time.sleep(0.05)
                                progress_bar.progress(i + 1)
                            result = Page2(email).profile(email, 'User', 'email', 'Profile')
                            self.user = result[0]
                            self.img = result[1]
                        else:
                            st.write('Password mismatch')
                    else:
                        st.write('User with this email already exists go to login')
                else:
                    st.write('Invalid email address')
            else:
                st.write("Invalid name")
        return name, phone, email, pass2


class Page2:
    def __init__(self, email):
        st.markdown("""
                                        <h1 style='text-align: center;'><span style='color:red;'>OneSmarter</span>Booking.com</h1>
                                        """, unsafe_allow_html=True)
        st.markdown("""<h2 style='text-align: left;'>Search Location</h2>
                                        """, unsafe_allow_html=True)
        self.email = email

        self.db_path = 'Database.sqlite3'
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()
        self.room = 1
        result = self.profile(self.email, 'User', 'email', 'Profile')
        self.img = result[1]
        self.user = result[0]
        self.book()

    def profile(self, email, table_name, email_column, image_column):
        query = f"SELECT {email_column}, {image_column} FROM {table_name} WHERE {email_column} = ?"
        self.cursor.execute(query, (email,))
        result = self.cursor.fetchone()
        if result is not None:
            return result
        return None

    def book(self):
        value = streamlit_searchbar("Where are you going?")
        today = datetime.datetime.now()
        print(today)
        col1, col2 = st.columns(2)
        date_in = col1.date_input(
            "Select Date of CheckIn",
            min_value=today,
            format="DD.MM.YYYY",
        )
        date_out = col2.date_input(
            "Select Date of CheckOut",
            min_value=today,
            format="DD.MM.YYYY",
        )
        col1, col2 = st.columns(2)
        adults = col1.selectbox('Number of Adults', list(range(1, 11)))
        child = col2.selectbox('Number of Children', list(range(0, 6)))
        print(adults, child)
        btn_ok = col1.button("Search")
        with st.expander("Click to see nearby Hotels"):
            st.write("Here are some hotels found near your chosen location")
        directory = 'tourist_places'
        files = os.listdir(directory)
        c1, c2 = st.columns(2)
        current_col = c1
        for j, file in enumerate(files):
            file_path = os.path.join(directory, file)
            current_col.image(file_path, caption=str(file).replace('.jpg', '').replace('.png', '').replace('.jpeg', ''))
            if current_col == c1:
                current_col = c2
            elif current_col == c2:
                current_col = c1
