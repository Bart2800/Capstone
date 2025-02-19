import streamlit as st
import pandas as pd

st.header("Capstone Dataset")

data = pd.read_csv("CAPSTONEDATA.csv")

# Display data in a responsive manner
st.dataframe(data, use_container_width=True)



# Footer
st.sidebar.markdown("---")
st.sidebar.text("© 2025 Simple Dashboard App")