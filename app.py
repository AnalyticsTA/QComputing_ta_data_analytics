import streamlit as st

main_page = st.Page("views/main.py",title="Principal",icon="🏢")

pg = st.navigation([main_page])

pg.run()