import streamlit as st
import datetime
import math
from PIL import Image

st.markdown("""
                        <h1 style='text-align: center;'>Hotel <span style='color:red;'>OneSmarter</span></h1>
                        """, unsafe_allow_html=True)


class Calendar:
    def __init__(self):
        st.markdown("""
                                <h2 style='text-align: left;'>Search Rooms</h2>
                                """, unsafe_allow_html=True)
        self.room = 1
        self.booking()

    def booking(self):
        today = datetime.datetime.now()
        print(today)
        date_in = st.date_input(
            "Select Date of CheckIn",
            min_value=today,
            format="DD.MM.YYYY",
        )
        print(date_in)
        col1, col2 = st.columns(2)
        adults = col1.selectbox('Number of Adults', list(range(1, 11)))
        child = col2.selectbox('Number of Children', list(range(0, 6)))
        print(adults, child)
        st.markdown("""
            <style> 
                #s-text{
                    text-align: center;
                    font-size:20px,
                }
            </style>
            <p id='s-text'>Capacity of one room is 2 Adults and 2 children Max</p>
            """, unsafe_allow_html=True)
        btn_ok = st.button("OK")
        total = adults + child
        if total > 4:
            self.room = total / 4
        if btn_ok:
            st.text(f"You choose {adults} Adults and {child} children for date {date_in} and {math.ceil(self.room)} "
                    f"room/s")
            self.payment()

    def payment(self):
        st.markdown("""<h2 style='text-align: left;'>Make Payment</h2>""", unsafe_allow_html=True)
        options = ['select', 'UPI', 'Credit Card', 'Account']
        option = st.selectbox('Choose Payment Method', options,)
        if option == 'UPI':
            image = Image.open('in.jpg')
            st.image(image, caption="ScanQR to pay")


Calendar()
