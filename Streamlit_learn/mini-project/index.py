import streamlit as st
import qrcode, os
from PIL import Image
import pyshorteners
import sqlite3, socket

class Image:
    def __init__(self):
        st.markdown('''
        # QR-Generator
        ''',True
        )
        self.link = None
        self.name = None
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()
        self.path = None
        self.sb_button = None
        self.sh_button = None
        self.do_button = None

    def get_ip_address(self):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    def code(self, link, location):
        if 'http' not in link:
            self.path = None
        else:
            y = qrcode.make(link)
            file_location = 'output_images/' + location + '.png'
            y.save(file_location)
            self.path = file_location
            print("qrcode png location", file_location)
            print(self.get_ip_address())
        return self.path
    
    def save(self):
        self.link = st.text_input("Enter your name...")
        self.name = st.text_input("Enter your email address...")
        self.sb_button = st.button('Submit')
        if self.sb_button:
            response = self.code(self.link, self.name)
            if response != None:
                st.write(f"QR is generated for link {self.link} with name '{self.name}'")
                col1, col2= st.columns([1,1])
                self.sh_button = col1.button('Show_QR')
                self.do_button = col2.button('Download QR')
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS QR_codes (
                    id INTEGER PRIMARY KEY,
                    Link TEXT,
                    Image_name TEXT,
                    QR_image BLOB
                )''')
                self.insert_to_db(self.link, self.name, self.path)
                
            else:
                st.write(f"Invalid link: {self.link}")
        if self.sh_button:
            print(self.sh_button)
            st.image(self.path)
    def insert_to_db(self, link, im_name, image):
        with open(image, 'rb') as image_file:
            image_data = image_file.read()
            self.cursor.execute("INSERT INTO QR_codes (Link, Image_name, QR_image) VALUES (?, ?, ?)", (link, im_name, image_data))
            self.connection.commit()
image = Image()
image.save()
