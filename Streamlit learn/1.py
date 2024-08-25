import time

import streamlit as st


# Function to read the image file and serve it for download
def download_image():
    with open('enterprise/Pages/in.png', 'rb') as f:
        image_data = f.read()
    return image_data


# Create a download button
if st.button('Download Image'):
    image_data = download_image()
    st.download_button(
        label='Click to download',
        data=image_data,
        key='download_button'
    )
if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"


def change_state():
    st.session_state["photo"] = "done"


col1, col2 = st.columns(2)
upload = col2.file_uploader("Upload a file", type=('.png', '.jpg', '.jpeg'), on_change=change_state)
camera = col1.camera_input("Take photo", on_change=change_state)
if st.session_state["photo"] == "done":
    progress_bar = col2.progress(0)
    for i in range(100):
        time.sleep(0.05)
        progress_bar.progress(i+1)
    success = col1.success("Photo successfully uploaded!")
    col2.metric(label="Temperature", value="60 C", delta="3 C")
    with st.expander("Click to read more!"):
        st.write("Expanded")
        if upload is not None:
            st.image(upload)
        else:
            st.image(camera)
