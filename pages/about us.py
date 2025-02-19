import streamlit as st


def about_us():
    st.title("About Us")
    st.write("Welcome to our application! We are dedicated to providing the best services.")
    st.write("Our team consists of passionate developers and designers focused on creating amazing experiences.")

if __name__ == "__main__":
    about_us()



# Footer
st.sidebar.markdown("---")
st.sidebar.text("© 2025 Simple Dashboard App")