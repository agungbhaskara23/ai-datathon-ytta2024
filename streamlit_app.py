import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.title('Dashboard Indeks Kerentanan Penyakit Demam Berdarah Dengue (DBD)')

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Dashboard Indeks Kerentanan Penyebaran Penyakit DBD (IK-DBD)',
                           ['About Page', 'Analisis Deskriptif Variabel', 
                            'Indeks Kerentanan Penyakit DBD (IK-DBD)','Prediksi Nilai IK-DBD'],
                           menu_icon='hospital',
                           icons=['house', 'gear', 'person', 'app'],
                           default_index=0)


