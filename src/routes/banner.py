import streamlit as st

from src.config import config

# Define function for initialising banner
def banner(pages):
    logo_px = max(75, min(config.logo_size, 225))
    logo_rt = max(1, min(logo_px / 75, 3))
    col_1, col_2, col_3, col_4 = st.columns(
        [logo_rt, 8, 1, 1]
        )
    with col_1:
        st.markdown("<div style='margin-top: 0px;'></div>", unsafe_allow_html=True)
        st.image(config.logo_path, width=logo_px)
    with col_2:
        margin_px = logo_px * (((logo_px - 75) / 150) ** 0.2) * 0.4
        st.markdown(f"<div style='margin-top: {margin_px}px;'></div>", unsafe_allow_html=True)
        st.header(config.title)
    with col_3:
        st.markdown("<div style='margin-top: 0px;'></div>", unsafe_allow_html=True)
        if st.button("Back"):
            st.write("test")
    with col_4:
        st.markdown("<div style='margin-top: 0px;'></div>", unsafe_allow_html=True)
        if st.button("Next"):
            st.write("test")
    st.divider()