import streamlit as st

from src.config import config

# Define function for initialising banner
def banner(logo_path, pages):
    b_col1, b_col2, b_col3, b_col4, b_col5 = st.columns([1, 5, 2, 1, 1])
    with b_col1:
        st.image(logo_path, width=75)
    with b_col2:
        st.header(config.title)
    st.divider()