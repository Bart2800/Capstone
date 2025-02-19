import streamlit as st
import pandas as pd

# Set page layout to wide mode for better responsiveness
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data efficiently with caching
@st.cache_data
def load_data():
    return pd.read_csv("CAPSTONEDATA.csv")

data = load_data()

# Check if required columns exist
if "COUNTRY" in data.columns and "NETSALES" in data.columns:
    st.write("### Sales Data by Country")

    # Group and sort data for better visualization
    grouped_data = data.groupby("COUNTRY")["NETSALES"].sum().reset_index()
    grouped_data = grouped_data.sort_values(by="NETSALES", ascending=False)

    # Display line chart
    st.line_chart(grouped_data, x="COUNTRY", y="NETSALES", use_container_width=True)
else:
    st.error("Columns 'COUNTRY' and 'NETSALES' are missing from the dataset.")


st.divider()


# Footer
st.sidebar.markdown("---")
st.sidebar.text("© 2025 Simple Dashboard App")