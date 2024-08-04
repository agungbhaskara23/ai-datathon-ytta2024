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
    st.write('Perubahan iklim merupakan fenomena global yang semakin nyata dirasakan di berbagai belahan dunia. Menurut PBB, perubahan iklim mengacu pada perubahan atau pergeseran jangka panjang dalam suhu dan pola cuaca.')

if selected == 'Analisis Deskriptif Variabel':
    # page title
    st.title('Variabel-variabel Penyusun Indeks')
    
    # import data
    df_2020 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2020.csv', delimiter=';', decimal=',', thousands='.')
    df_2021 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2021.csv', delimiter=';', decimal=',', thousands='.')
    df_2022 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2022.csv', delimiter=';', decimal=',', thousands='.')
    df_2023 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2023.csv', delimiter=';', decimal=',', thousands='.')

    variable_option = st.selectbox(
        "Option",("NDVI", "NDBI", "NDWI", "ETC"), index=None, placeholder="Pilih variabel", label_visibility="hidden"
    )

    if variable_option == "NDVI":
        st.write("Haloo NDVI")

    if variable_option == "NDBI":
        st.write("Haloo NDBI")
    
