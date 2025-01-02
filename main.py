import streamlit as st
from streamlit_option_menu import option_menu


st.title('Vinsup Project')
with st.sidebar:
    selected = option_menu(
        menu_title='Project Title',
        options=['Abstract','Task','System Requirements','Modules']
    )
