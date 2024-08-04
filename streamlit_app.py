import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Dashboard Indeks Kerentanan Penyebaran Penyakit DBD (IK DBD)',
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
    st.write('Perubahan iklim merupakan fenomena global yang semakin nyata dirasakan di berbagai belahan dunia. Menurut PBB, **perubahan iklim mengacu pada perubahan atau pergeseran jangka panjang dalam suhu dan pola cuaca**. '
    'Perubahan iklim memiliki sejumlah dampak, seperti menurunnya kemampuan untuk menanam pangan, kesulitan pada sektor perumahan, keselamatan dan pekerjaan, hingga perubahan iklim mampu mempengaruhi kesehatan manusia (Susilawati, 2021). ' 
    'Dalam aspek kesehatan, perubahan iklim dapat meningkatkan risiko terhadap maraknya penyebaran penyakit menular. Salah satu penyakit menular tersebut adalah penyakit demam berdarah *dengue* (DBD) yang menular melalui vektor/media tertentu.')

    st.write('DBD merupakan penyakit menular yang disebabkan oleh virus *dengue* yang ditularkan melalui gigitan nyamuk *aedes aegypti* dan *aedes albopictus* (Soedarto, 2018). Pada tahun 2024, *World Health Organization* atau WHO memperkirakan setengah '
             'dari populasi dunia berisiko terkena virus *dengue*, dengan 100 - 400 juta infeksi setiap tahun. Penyakit DBD juga masih menjadi salah satu masalah utama dari kesehatan masyarakat di Indonesia (Kusumawardani & Achmadi, 2012). Pada tahun 2010, '
             'Indonesia pernah berada pada urutan kedua dengan jumlah kasus DBD terbanyak di Asia (Bhatt et al., 2013). Disamping itu, Kementerian Kesehatan RI (2021) melaporkan bahwa lebih dari 80% kabupaten/kota di setiap provinsinya terindikasi penyakit DBD.')

    st.write('Peningkatan akan ketahanan atau pengurangan kerentanan penyakit DBD dapat menjadi upaya mengurangi dampak infeksi virus *dengue* di semua tingkatan (Hagenlocher et al., 2013; Hanifah Septiani et al., 2021). Oleh karena itu, penting untuk mengukur tingkat kerentanan '
             'infeksi DBD di setiap wilayah sebagai upaya estimasi kewaspadaan pemerintah dan masyarakat terhadap DBD. Namun demikian, pengukuran tingkat kerentanan terhadap DBD saat ini masih jarang dilakukan, terlebih di wilayah Indonesia. Pemanfaatan kecerdasan buatan (*artificial intelegence*/AI) '
             'yang terus berkembang dapat dimanfaatkan sebagai salah satu metode inovatif dalam menyelesaikan masalah, tak terkecuali dalam upaya pencegahan dan penanggulangan DBD.')

    st.title("What's Inside?")
    st.write('Dalam dashboard ini tersedia empat menu utama, yaitu: ')

    st.write('**1. About Page**')
    st.write('Berisi tentang informasi dashboard mencakup latar belakang, fitur yang tersedia, dan cara penggunaan dashboard')

    st.write('**2. Analisis Deskriptif Variabel**')
    st.write('Berisi tentang informasi variabel secara deskriptif yang digunakan sebagai penyusun indeks. Informasi disajikan dalam bentuk visual')

    st.write('**3. Indeks Kerentanan Penyakit DBD (IK DBD)**')
    st.write('Berisi tentang hasil penghitungan IK DBD pada wilayah di Indonesia yang disajikan dalam bentuk visualisasi peta hasil cluster. Selain itu, tersedia juga interpretasi dari nilai IK DBD dan cluster yang terbentuk')

    st.write('**4. Prediksi Nilai IK DBD**')
    st.write('Berisi tentang simulasi hasil kluster nilai IK DBD yang dapat dilakukan dengan inputasi nilai manual pada masing-masing variabel penyusun indeks')

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
    
