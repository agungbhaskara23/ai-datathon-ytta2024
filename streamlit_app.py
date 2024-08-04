import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('IK DBD Dashboard Menu',
                           ['About', 'Learn about Data', 
                            'Indeks Kerentanan Penyakit DBD (IK DBD)','Prediksi Nilai IK DBD'],
                           menu_icon='hospital',
                           icons=['house', 'gear', 'person', 'app'],
                           default_index=0)

# About Page
if selected == 'About Page':
    # page title
    st.title('Welcome to Dashboard IK DBD!')
    
    # background story
    st.write('**Demam berdarah *dengue*** atau DBD merupakan penyakit menular yang disebabkan oleh virus *dengue* yang ditularkan melalui gigitan nyamuk *aedes aegypti* dan *aedes albopictus*. Pada tahun 2024, *World Health Organization* atau WHO memperkirakan setengah '
             'dari populasi dunia berisiko terkena virus *dengue*, dengan 100 - 400 juta infeksi setiap tahun. Penyakit DBD juga masih menjadi salah satu masalah utama dari kesehatan masyarakat di Indonesia karena pada tahun 2010, Indonesia pernah berada pada urutan '
             'kedua dengan jumlah kasus DBD terbanyak di Asia *(Bhatt et al., 2013)*. Disamping itu, Kementerian Kesehatan RI (2021) melaporkan bahwa lebih dari 80% kabupaten/kota di setiap provinsinya terindikasi penyakit DBD.')
    
    st.write('**Dashboard IK DBD** merupakan dashboard untuk pemetaan tingkat kerentanan penyakit demam berdarah *dengue* yang terjadi di masyarakat Indonesia. Saat ini, dashboard masih hanya berfokus pada pemetaan tingkat kerentanan di Pulau Jawa. Peningkatan akan ketahanan '
             'atau pengurangan kerentanan penyakit DBD dapat menjadi upaya mengurangi dampak infeksi virus *dengue* di semua tingkatan *(Hagenlocher et al., 2013; Hanifah Septiani et al., 2021)*. Adanya perubahan iklim sebagai salah satu fenomena global memberikan sejumlah dampak, '
             'seperti menurunnya kemampuan untuk menanam pangan, kesulitan pada sektor perumahan, keselamatan dan pekerjaan, hingga perubahan iklim mampu mempengaruhi kesehatan manusia *(Susilawati, 2021)*, salah satunya adalah penyebaran penyakit menular. '
             'Pemanfaatan kecerdasan buatan (*artificial intelegence*/AI) yang terus berkembang dapat dijadikan sebagai salah satu metode inovatif dalam menyelesaikan masalah, tak terkecuali dalam upaya pencegahan dan penanggulangan DBD.')

    st.title("What's Inside?")
    st.write('Tersedia empat menu utama dalam dashboard ini, yaitu: ')

    st.write('**1. About**')
    st.write('Informasi dashboard mencakup latar belakang, fitur yang tersedia, dan cara penggunaan dashboard')

    st.write('**2. Learn about Data**')
    st.write('Informasi variabel yang digunakan sebagai penyusun indeks secara deskriptif dan disajikan dalam sejumlah bentuk visual')

    st.write('**3. Indeks Kerentanan Penyakit DBD (IK DBD)**')
    st.write('Hasil penghitungan IK DBD pada wilayah Pulau Jawa, Indonesia pada tahun tertentu (2022). Hasil disajikan dalam berbagai visualisasi, seperti grafik dan peta hasil cluster. Interpretasi dari nilai IK DBD pada masing-masing cluster juga tersaji dalam bagian ini')

    st.write('**4. Prediksi Nilai IK DBD**')
    st.write('Simulasi nilai IK DBD dan kelas cluster yang diperoleh ketika dilakukan inputasi nilai seecara manual pada masing-masing variabel penyusun indeks')

    st.title("How to Use it?")
    st.write('Panduan atau tutorial penggunaan dashboard ini dapat dilihat pada video berikut.')
    
if selected == 'Analisis Deskriptif Variabel':
    # page title
    st.title('Variabel-variabel Penyusun Indeks')
    
    # import data
    df_2020 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2020.csv', delimiter=';', decimal=',', thousands='.')
    df_2021 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2021.csv', delimiter=';', decimal=',', thousands='.')
    df_2022 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2022.csv', delimiter=';', decimal=',', thousands='.')
    df_2023 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2023.csv', delimiter=';', decimal=',', thousands='.')

    variable_option = st.selectbox(
        "Option",("NDVI", "NDBI", "NDWI", "CO2", "CO", "Curah Hujan", "Suhu", "Kelembaban", "Kepadatan Penduduk", "Persentase Penduduk Miskin", "Rasio Dokter"), index=None, placeholder="Pilih variabel", label_visibility="hidden"
    )

    if variable_option == "NDVI":
        # Row A
        st.markdown('### Summary Statistics')
        col1, col2, col3 = st.columns(3)
        col1.metric("Tertinggi", round(df_2023[variable_option].max(),4), "1.2 °F")
        col2.metric("Terendah", round(df_2023[variable_option].min(),4), "-8%")
        col3.metric("Rata-rata", round(df_2023[variable_option].sum()/len(df_2020),4), "4%")

    if variable_option == "NDBI":
        st.write("Haloo NDBI")
    
