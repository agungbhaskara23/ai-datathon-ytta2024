import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import plost
import branca
import geopandas

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
   
    if variable_option == "NDVI" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('NDVI merupakan indeks dari cita satelit yang mampu memetakan daerah vegetasi di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDVI tinggi**, maka terdapat '
        'banyak vegetasi lebat sehingga menjadi habitat yg baik untuk nyamuk.')

    if variable_option == "NDBI" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('NDBI merupakan indeks dari citra satelit yang mampu memetakan daerah lahan terbangun di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDBI tinggi**, maka terdapat '
        'banyak pemukiman yang mengakibatkan penduduk makin padat dan potensi penyebaran nyamuk DBD makin tinggi')

    if variable_option == "NDWI" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('NDWI merupakan indeks dari citra satelit yang mampu memetakan daerah perairan di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDBI tinggi**, maka terdapat '
        'cukup banyak wilayah yang menjadi genangan air sebagai tempat perkembangbiak nyamuk')

# IK DBD
if selected == 'Indeks Kerentanan Penyakit DBD (IK DBD)':
    # page title
    st.title('Indeks Kerentanan DBD / IK DBD')

    st.write('Dalam dashboard ini, penghitungan IK DBD dilakukan hanya pada tahun 2022 saja dengan menyesuaikan ketersediaan data kasus penderita DBD oleh Kementerian Kesehatan. Model penghitungan indeks kerentanan DBD '
            '(IK DBD) dibangun dengan menggunakan dataset pada tahun 2020, 2021, dan 2023. Bobot dihitung dengan menggunakan metode PCA')
    st.write('Hasil perolehan nilai indeks kemudian dilanjutkan dengan proses *clustering* atau pengelompokkan untuk melihat pola kedekatan atau pengelompokkan antarnilai indeks.')

    df_final = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/df_final_with_cluster.csv')
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Tertinggi", df_final['Index'].max())
    col2.metric("Terendah", df_final['Index'].min())
    col3.metric("Rata-rata",df_final['Index'].mean())
    
    # Mapping Indeks  
    import geopandas as gpd
    import json

    with open("data/shp_java_kabkota.geojson") as f:
        data = json.load(f)
    
    # Convert JSON data to GeoDataFrame
    gdf = gpd.GeoDataFrame.from_features(data['features'], crs="EPSG:4326")

    df_cut = df_final.copy()
    df_cut = df_cut.iloc[:,18:20]
    df_cut['ADM2_EN'] = df_final['KAB/KOT']
    json_merge = gdf.merge(df_cut, how="left", left_on="ADM2_EN", right_on="ADM2_EN")

    colormap = branca.colormap.LinearColormap(
        vmin=json_merge["Index"].quantile(0.0),
        vmax=json_merge["Index"].quantile(1),
        colors=["darkgreen", "green", "lightblue", "orange", "red"],
        caption="IK DBD",
    )

    m = folium.Map(location=[-7.576882, 111.819939], zoom_start=7)

    popup = folium.GeoJsonPopup(
        fields=["ADM2_EN", "Index"],
        aliases=["Kab/Kota", "IK DBD"],
        localize=True,
        labels=True,
        style="background-color: yellow;",
    )

    tooltip = folium.GeoJsonTooltip(
        fields=["ADM2_EN", "Index", "Cluster"],
        aliases=["Kab/Kota:", "IK DBD:", "Cluster IK DBD:"],
        localize=True,
        sticky=False,
        labels=True,
        style="""
            background-color: #F0EFEF;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=800,
    )

    g = folium.GeoJson(
        json_merge,
        style_function=lambda x: {
            "fillColor": colormap(x["properties"]["Index"])
            if x["properties"]["Index"] is not None
            else "transparent",
            "color": "black",
            "fillOpacity": 0.8,
        },
        tooltip=tooltip,
        popup=popup,
    ).add_to(m)
    
    st.write("### Cluster and Index Calculation Mapping")
    st_map = folium_static(m, width=900, height=550)

# Simulasi IK DBD
if selected == 'Prediksi Nilai IK DBD':
    # page title
    st.title('Prediksi Nilai IK DBD')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        ndbi_value = st.text_input('NDBI Index Value')
    with col2:
        ndvi_value = st.text_input('NDVI Index Value')
    with col3:
        ndwi_value = st.text_input('NDWI Index Value')
    with col4:
        co2_value = st.text_input('CO2 Value')

    st.write("")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        co_value = st.text_input('CO Value')
    with col2:
        curah_hujan = st.text_input('Curah Hujan (mm/day)')
    with col3:
        suhu = st.text_input('Suhu (C)')     
    with col4:
        kelembaban = st.text_input('Kelembaban (%)')

    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        kep_pend = st.text_input('Kepadatan penduduk (jiwa/km2)')
    with col2:
        persen_miskin = st.text_input('Persentase penduduk miskin (%)')
    with col3:
        rasio_dokter = st.text_input('Rasio dokter (per 1.000 penduduk)')

    
