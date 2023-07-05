import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
hide_github_icon = """

.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{ display: none; } #MainMenu{ visibility: hidden; } footer { visibility: hidden; } header { visibility: hidden; }
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)
page = st.sidebar.selectbox("Predict/Contributors", ("Predict", "Contributors"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()
