import streamlit as st

# Create a button to enable/disable another button using JavaScript
button_toggle_js = f"""
<script>
    function toggleButton() {{
        var button = document.getElementById("enable_disable_button");
        button.disabled = !button.disabled;
    }}
</script>
<button onclick="toggleButton()">Enable/Disable Button</button>
"""

# Display the HTML with the JavaScript button
st.markdown(button_toggle_js, unsafe_allow_html=True)

# Create the button that you want to enable/disable initially disabled
enable_disable_button = st.button("Button to Enable/Disable", key="enable_disable_button", disabled=True)

# Additional content can be added here based on the button state
