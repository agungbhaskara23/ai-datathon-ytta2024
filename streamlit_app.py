import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.title('Dashboard Indeks Kerentanan Penyakit Demam Berdarah Dengue (DBD)')

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")
