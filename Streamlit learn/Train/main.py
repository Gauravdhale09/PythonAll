import streamlit as st

from streamlit_option_menu import option_menu
import sqlite3

st.set_page_config(
    page_title="Pondering",
)


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        # app = st.sidebar(
        with st.sidebar:
            app = option_menu(
                menu_title='Pondering ',
                options=['Home', 'Account', 'Trending', 'Your Posts', 'about'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"}, }

            )


    run()



class Database:
    def __init__(self):
        self.db = sqlite3.connect('Database.sqlite3')
        self.cursor = self.db.cursor()

    def user_table(self, name, email, Phone, Profile, Password):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS User (
                                            id INTEGER PRIMARY KEY,
                                            username TEXT,
                                            email TEXT,
                                            PhoneNo TEXT,
                                            Profile BLOB,
                                            Password TEXT
                                        )''')
        self.cursor.execute("INSERT INTO User (username, email, PhoneNo, Profile, Password) "
                            "VALUES (?, ?, ?, ?, ?)", (name, email, Phone, Profile, Password))
        self.db.commit()

    def check_email(self, email, table_name, email_column):
        query = f"SELECT * FROM {table_name} WHERE {email_column} = ?"
        self.cursor.execute(query, (email,))
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False

    def check_present(self, email, password, table_name, email_column, password_column):
        query = f"SELECT * FROM {table_name} WHERE {email_column} = ? AND {password_column} = ?"
        self.cursor.execute(query, (email, password))
        if self.cursor.fetchone() is not None:
            return True
        else:
            return False
