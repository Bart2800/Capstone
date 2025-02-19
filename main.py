import streamlit as st

st.set_page_config(page_title="Simple Dashboard", layout="wide")

st.title("📊 Simple Web Dashboard")
st.image("img_1.jpg", use_column_width=True)

st.markdown("""
### Welcome to this simple dashboard!
Use the sidebar to navigate between different sections.
""")

# Sidebar Navigation
st.sidebar.header("Navigation")
st.sidebar.button("Home")
st.sidebar.button("Analytics")
st.sidebar.button("Reports")

# Main Content
st.subheader("Dashboard Overview")
st.write("This is a simple web dashboard where you can analyze data and generate reports.")

# Footer
st.sidebar.markdown("---")
st.sidebar.text("© 2025 Simple Dashboard App")
