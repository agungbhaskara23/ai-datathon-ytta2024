import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('IK DBD Dashboard Menu',
                           ['About', 'Learn about Data', 
                            'Indeks Kerentanan Penyakit DBD (IK DBD)','Prediksi Nilai IK DBD'],
                           menu_icon='hospital',
                           icons=['house', 'gear', 'person', 'app'],
                           default_index=0)

# About Page
if selected == 'About':
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
    
if selected == 'Learn about Data':
    # page title
    st.title('Learn More about Index Data')
    
    # import data
    df_2020 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2020.csv', delimiter=';', decimal=',', thousands='.')
    df_2021 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2021.csv', delimiter=';', decimal=',', thousands='.')
    df_2022 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2022.csv', delimiter=';', decimal=',', thousands='.')
    df_2023 = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/Dataset-Olah-2023.csv', delimiter=';', decimal=',', thousands='.')

    col1, col2 = st.columns(2)
    variable_option = col1.selectbox(
        "Option",("NDVI", "NDBI", "NDWI", "CO2", "CO", "Curah Hujan (BMKG)", "Temperature (BMKG)", "Kelembaban (BMKG)", "KEP. PENDUDUK", "PRESENTASE PENDUDUK MISKIN", "RASIO DOKTER"), index=None, placeholder="Pilih variabel", label_visibility="hidden"
    )
    year_option = col2.selectbox(
        "Option",("2020", "2021", "2022", "2023"), index=None, placeholder="Pilih tahun", label_visibility="hidden"
    )

    if variable_option == None:
        st.write("")

    if year_option == None:
        st.write("")
    
    if year_option == "2020" and variable_option != None:
        
        st.markdown('### Summary Statistics')
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Rata-rata", round(df_2020[variable_option].mean(),4), 0)
        col2.metric("Terendah", round(df_2020[variable_option].min(),4), 0)
        col3.metric("Median", round(df_2020[variable_option].median(),4), 0)
        col4.metric("Tertinggi", round(df_2020[variable_option].max(),4), 0)
        col5.metric("Standar Deviasi", round(df_2020[variable_option].std(),4), 0)

        st.write("")
        st.write("### Mapping of ",variable_option, " Areas in Pulau Jawa (", year_option, ")")
        json1 = f"data/shp_java_kabkota.geojson"
        map = folium.Map(location=[-7.576882, 111.819939], zoom_start=7, scrollWheelZoom=False, tiles='CartoDB positron')
        choropleth = folium.Choropleth(
                    geo_data=json1,
                    data=df_2022,
                    columns=('KAB/KOT', variable_option),
                    key_on='feature.properties.ADM2_EN',
                    line_opacity=0.8,
                    fill_opacity=0.8,
                    highlight=True,
                    legend_name=variable_option
        )
        choropleth.geojson.add_to(map)
        st_map = st_folium(map, width=1500, height=550) 

        # tooltip = folium.features.GeoJson(json1, name="ADM2_EN", popup=folium.features.GeoJsonPop(field=["ADM2_EN"]))
        # tooltip.geojson.add_to(map)

    if year_option == "2021" and variable_option != None:
        
        st.markdown('### Summary Statistics')
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Rata-rata", round(df_2021[variable_option].mean(),4), round((df_2021[variable_option].mean()) - (df_2020[variable_option].mean()),4))
        col2.metric("Terendah", round(df_2021[variable_option].min(),4), round((df_2021[variable_option].min()) - (df_2020[variable_option].min()),4))
        col3.metric("Median", round(df_2021[variable_option].median(),4), round((df_2021[variable_option].median()) - (df_2020[variable_option].median()),4))
        col4.metric("Tertinggi", round(df_2021[variable_option].max(),4), round((df_2021[variable_option].max()) - (df_2020[variable_option].max()),4))
        col5.metric("Standar Deviasi", round(df_2021[variable_option].std(),4), round((df_2021[variable_option].std()) - (df_2020[variable_option].std()),4))

        st.write("")
        st.write("### Mapping of ",variable_option, " Areas in Pulau Jawa (", year_option, ")")
        json1 = f"data/shp_java_kabkota.geojson"
        map = folium.Map(location=[-7.576882, 111.819939], zoom_start=7, scrollWheelZoom=False, tiles='CartoDB positron')
        choropleth = folium.Choropleth(
                    geo_data=json1,
                    data=df_2021,
                    columns=('KAB/KOT', variable_option),
                    key_on='feature.properties.ADM2_EN',
                    line_opacity=0.8,
                    fill_opacity=0.8,
                    highlight=True,
                    legend_name=variable_option
        )
        choropleth.geojson.add_to(map)
        st_map = st_folium(map, width=1500, height=550) 

        # tooltip = folium.features.GeoJson(json1, name="ADM2_EN", popup=folium.features.GeoJsonPop(field=["ADM2_EN"]))
        # tooltip.geojson.add_to(map)
    
    if year_option == "2022" and variable_option != None:
        
        data_used = "df_" + year_option
        st.markdown('### Summary Statistics')
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Rata-rata", round(df_2022[variable_option].mean(),4), round((df_2022[variable_option].mean()) - (df_2021[variable_option].mean()),4))
        col2.metric("Terendah", round(df_2022[variable_option].min(),4), round((df_2022[variable_option].min()) - (df_2021[variable_option].min()),4))
        col3.metric("Median", round(df_2022[variable_option].median(),4), round((df_2022[variable_option].median()) - (df_2021[variable_option].median()),4))
        col4.metric("Tertinggi", round(df_2022[variable_option].max(),4), round((df_2022[variable_option].max()) - (df_2021[variable_option].max()),4))
        col5.metric("Standar Deviasi", round(df_2022[variable_option].std(),4), round((df_2022[variable_option].std()) - (df_2021[variable_option].std()),4))

        st.write("")
        st.write("### Mapping of ",variable_option, " Areas in Pulau Jawa (", year_option, ")")
        json1 = f"data/shp_java_kabkota.geojson"
        map = folium.Map(location=[-7.576882, 111.819939], zoom_start=7, scrollWheelZoom=False, tiles='CartoDB positron')
        choropleth = folium.Choropleth(
                    geo_data=json1,
                    data=df_2022,
                    columns=('KAB/KOT', variable_option),
                    key_on='feature.properties.ADM2_EN',
                    line_opacity=0.8,
                    fill_opacity=0.8,
                    highlight=True,
                    legend_name=variable_option
        )
        choropleth.geojson.add_to(map)
        st_map = st_folium(map, width=1500, height=550) 

        # tooltip = folium.features.GeoJson(json1, name="ADM2_EN", popup=folium.features.GeoJsonPop(field=["ADM2_EN"]))
        # tooltip.geojson.add_to(map)
    
    if year_option == "2023" and variable_option != None:
        
        data_used = "df_" + year_option
        st.markdown('### Summary Statistics')
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Rata-rata", round(df_2023[variable_option].mean(),4), round((df_2023[variable_option].mean()) - (df_2022[variable_option].mean()),4))
        col2.metric("Terendah", round(df_2023[variable_option].min(),4), round((df_2023[variable_option].min()) - (df_2022[variable_option].min()),4))
        col3.metric("Median", round(df_2023[variable_option].median(),4), round((df_2023[variable_option].median()) - (df_2022[variable_option].median()),4))
        col4.metric("Tertinggi", round(df_2023[variable_option].max(),4), round((df_2023[variable_option].max()) - (df_2022[variable_option].max()),4))
        col5.metric("Standar Deviasi", round(df_2023[variable_option].std(),4), round((df_2023[variable_option].std()) - (df_2022[variable_option].std()),4))

        st.write("")
        st.write("### Mapping of ",variable_option, " Areas in Pulau Jawa (", year_option, ")")
        json1 = f"data/shp_java_kabkota.geojson"
        map = folium.Map(location=[-7.576882, 111.819939], zoom_start=7, scrollWheelZoom=False, tiles='CartoDB positron')
        choropleth = folium.Choropleth(
                    geo_data=json1,
                    data=df_2023,
                    columns=('KAB/KOT', variable_option),
                    key_on='feature.properties.ADM2_EN',
                    line_opacity=0.8,
                    fill_opacity=0.8,
                    highlight=True,
                    legend_name=variable_option
        )
        choropleth.geojson.add_to(map)
        st_map = st_folium(map, width=1500, height=550) 
   
    if variable_option == "NDVI":
        st.write("### Deskripsi Data") 
        st.write("NDVI merupakan indeks yang mampu memetakan vegetasi di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDVI tinggi**, maka terdapat '
        'banyak vegetasi lebat sehingga menjadi habitat yg baik untuk nyamuk.")

    if variable_option == "NDBI":
        st.write("### Deskripsi Data") 
        st.write("NDVI merupakan indeks yang mampu memetakan vegetasi di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDVI tinggi**, maka terdapat '
        'banyak vegetasi lebat sehingga menjadi habitat yg baik untuk nyamuk.")
    
    
