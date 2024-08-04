import streamlit as st

# Set page configuration
st.set_page_config(page_title="Dashboard IK-DBD",
                   layout="wide",
                   page_icon="📙")

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Dashboard Indeks Kerentanan Penyebaran Penyakit DBD (IK-DBD)',
                           ['About Page',
                            'Analisis Deskriptif Variabel',
                            'Indeks Kerentanan Penyakit DBD (IK-DBD)',
                            'Prediksi Nilai IK-DBD'],
                           menu_icon='hospital',
                           icons=['house', 'gear', 'person', 'app'],
                           default_index=0)


# About Page
if selected == 'About Page':

    # page title
    st.title('Introduction')

    #

# Analisis Deskriptif Variabel
else if selected == 'Analisis Deskriptif Variabel':

  # page title


else if selected == 'Indeks Kerentanan Penyakit DBD (IK-DBD)':

  # page title


else if selected == 'Prediksi Nilai IK-DBDl':

  # page title

st.title('🎈 App Name')

st.write('Hello world!')
