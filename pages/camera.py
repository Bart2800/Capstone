import streamlit as st
from datetime import datetime
import os

# Streamlit UI
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

# Save the picture if taken
if picture:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"captured_image_{timestamp}.png"
    save_path = os.path.join(os.getcwd(), filename)

    with open(save_path, "wb") as file:
        file.write(picture.getvalue())

    st.success(f"Image saved as {filename}")
