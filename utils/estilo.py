import streamlit as st


def estilizar_inputs():
    st.markdown("""
    <style>
    div[data-testid="InputInstructions"] {
        visibility: hidden;
    }
    </style>
    """, unsafe_allow_html=True)
