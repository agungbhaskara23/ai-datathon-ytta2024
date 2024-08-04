import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Dashboard Indeks Kerentanan Penyebaran Penyakit DBD (IK-DBD)',
                           ['About Page', 'Analisis Deskriptif Variabel', 
                            'Indeks Kerentanan Penyakit DBD (IK DBD)','Prediksi Nilai IK DBD'],
                           menu_icon='hospital',
                           icons=['house', 'gear', 'person', 'app'],
                           default_index=0)

# About Page
if selected == 'About Page':
    # page title
    st.title('Introduction')
    
    # background story
    

if selected == 'Analisis Deskriptif Variabel':
    # page title
    st.title('Variabel-variabel Penyusun Indeks')
    
    # import data
    dataset = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2023.csv', delimiter=';', decimal=',', thousands='.')
    dataset
