import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import folium
from streamlit_folium import st_folium
from streamlit_folium import folium_static
import plost
import branca
import geopandas
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np
import streamlit.components.v1 as components

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
        st_map = folium_static(map, width=1100, height=550) 

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
        st_map = folium_static(map, width=1100, height=550) 

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
        st_map = folium_static(map, width=1100, height=550)  

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
        st_map = folium_static(map, width=1100, height=550) 
   
    if variable_option == "NDVI" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('NDVI merupakan indeks dari cita satelit Sentinel 2 yang mampu memetakan daerah vegetasi di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDVI tinggi**, maka terdapat '
        'banyak vegetasi lebat sehingga menjadi habitat yg baik untuk nyamuk.')

    if variable_option == "NDBI" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('NDBI merupakan indeks dari citra satelit Sentinel 2 yang mampu memetakan daerah lahan terbangun di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDBI tinggi**, maka terdapat '
        'banyak pemukiman yang mengakibatkan penduduk makin padat dan potensi penyebaran nyamuk DBD makin tinggi')

    if variable_option == "NDWI" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('NDWI merupakan indeks dari citra satelit Sentinel 2 yang mampu memetakan daerah perairan di suatu wilayah. Dalam hal kaitannya dengan tingkat kerentanan DBD, Ketika nilai **NDBI tinggi**, maka terdapat '
        'cukup banyak wilayah yang menjadi genangan air sebagai tempat perkembangbiak nyamuk')

    if variable_option == "CO2" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('CO2 merupakan indeks dari citra satelit Sentinel 5P yang mampu memetakan kandungan gas CO2 di udara. Dalam hal kaitannya dengan tingkat kerentanan DBD, '
        'kandungan CO2 pada udara bersifat atraktan yang mampu menarik nyamuk untuk berdekatan pada manusia sehingga berpotensi menularkan virus dengue ke manusia')

    if variable_option == "CO" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('CO merupakan indeks dari citra satelit Sentinel 5P yang mampu memetakan kandungan gas karbon monoksida di udara. Dalam hal kaitannya dengan tingkat kerentanan DBD, '
        'CO merupakan bahan kimia yang ada dalam cairan pemberantasan nyamuk (fogging). Dengan demikian, keberadaan CO yang semakin tinggi di udara menyebabkan habitat nyamuk DBD menjadi berkurang')

    if variable_option == "Curah Hujan (BMKG)" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('Curah hujan merupakan tingkat intensitas air jatuh ke bumi dalam bentuk hujan. Data yang disediakan oleh BMKG adalah dalam bentuk harian. Pada dashboard ini, digunakan '
        'rata rata curah hujan harian per tahun. Dalam kaitannya dengan tingkat kerentanan DBD, ketika **curah hujan** tinggi, terdapat dua kemungkinan. Jika frekuensi hujan lebat dan terus menerus, hal ini dapat berpotensi menghilangkan tempat perkembangbiakan nyamuk. '
        'Di sisi lain, jika frekuensi singkat, maka berpotensi menimbulkan genangan air')

    if variable_option == "Kelembaban (BMKG)" and year_option != None:
        st.write("### Deskripsi Data") 
        st.write('Ketika **kelembaban** tinggi, maka tingkat kerentanan DBD tinggi. Hal ini disebabkan karena nyamuk semakin leluasa, lingkungan lembab membantu nyamuk berkembang biak dan meningkatkan aktivitas nyamuk. Kelembaban yang bernilai rendah mengakibatkan cairan tubuh nyamuk kering akibat terjadinya penguapan')

# IK DBD
if selected == 'Indeks Kerentanan Penyakit DBD (IK DBD)':
    # page title
    st.title('Indeks Kerentanan DBD / IK DBD')

    st.write('Dalam dashboard ini, penghitungan IK DBD dilakukan hanya pada tahun 2022 saja dengan menyesuaikan ketersediaan data kasus penderita DBD oleh Kementerian Kesehatan. Model penghitungan indeks kerentanan DBD '
            '(IK DBD) dibangun dengan menggunakan dataset pada tahun 2020, 2021, dan 2023. Bobot dihitung dengan menggunakan metode PCA')
    st.write('Hasil perolehan nilai indeks kemudian dilanjutkan dengan proses *clustering* atau pengelompokkan untuk melihat pola kedekatan atau pengelompokkan antarnilai indeks.')

    df_final = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/df_final_with_cluster.csv')
    clust_1 = df_final[df_final['Cluster'] == 1]['Index']
    clust_2 = df_final[df_final['Cluster'] == 2]['Index']
    clust_3 = df_final[df_final['Cluster'] == 3]['Index']
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.metric("Rata-rata Indeks Cluster 1", round(clust_1.mean(),4))
    col2.metric("Banyak Kab/Kota Cluster 1", len(clust_1))
    col3.metric("Rata-rata Indeks Cluster 2", round(clust_2.mean(),4))
    col4.metric("Banyak Kab/Kota Cluster 2", len(clust_2))
    col5.metric("Rata-rata Indeks Cluster 3", round(clust_3.mean(),4))
    col6.metric("Banyak Kab/Kota Cluster 3", len(clust_3))
    
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

    colormap = branca.colormap.StepColormap(
        colors=['lightgreen', 'white', 'green'],
        index=[1, 2, 3],
        vmin=json_merge["Cluster"].min(),
        vmax=json_merge["Cluster"].max(),
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
            "fillColor": colormap(x["properties"]["Cluster"])
            if x["properties"]["Cluster"] is not None
            else "transparent",
            "color": "black",
            "fillOpacity": 0.8,
        },
        tooltip=tooltip,
        popup=popup,
    ).add_to(m)
    
    st.write("### Cluster and Index Calculation Mapping")
    st_map = folium_static(m, width=1100, height=550)

# Simulasi IK DBD
if selected == 'Prediksi Nilai IK DBD':
    # page title
    st.title('Prediksi Nilai IK DBD')

# Define columns
columns = ['ndbi_value', 'ndvi_value', 'ndwi_value', 'co2_value', 'co_value', 'curah_hujan', 'suhu', 'kelembaban', 'kep_pend', 'persen_miskin', 'rasio_dokter']

# Initialize the DataFrame in session state if it doesn't exist
if 'df_input' not in st.session_state:
    st.session_state.df_input = pd.DataFrame(columns=columns)

# Validation function
def validate_number(value):
    try:
        return float(value)
    except ValueError:
        return None

# Streamlit form
with st.form(key='form-index', clear_on_submit=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        ndbi_value = st.text_input('NDBI Index Value', value='', key='ndbi_value')
    with col2:
        ndvi_value = st.text_input('NDVI Index Value', value='', key='ndvi_value')
    with col3:
        ndwi_value = st.text_input('NDWI Index Value', value='', key='ndwi_value')
    with col4:
        co2_value = st.text_input('CO2 Value', value='', key='co2_value')

    st.write("")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        co_value = st.text_input('CO Value', value='', key='co_value')
    with col2:
        curah_hujan = st.text_input('Curah Hujan (mm/day)', value='', key='curah_hujan')
    with col3:
        suhu = st.text_input('Suhu (C)', value='', key='suhu')
    with col4:
        kelembaban = st.text_input('Kelembaban (%)', value='', key='kelembaban')

    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        kep_pend = st.text_input('Kepadatan penduduk (jiwa/km2)', value='', key='kep_pend')
    with col2:
        persen_miskin = st.text_input('Persentase penduduk miskin (%)', value='', key='persen_miskin')
    with col3:
        rasio_dokter = st.text_input('Rasio dokter (per 1.000 penduduk)', value='', key='rasio_dokter')

    col1, col2 = st.column(2)
    with col1: 
        submitted = st.form_submit_button("Store to Data")
    with col2:
        clear_all = st.form_submit_button("Clear all existing data")

# Process the form data
if submitted:
    user_input = {
        'ndbi_value': validate_number(ndbi_value),
        'ndvi_value': validate_number(ndvi_value),
        'ndwi_value': validate_number(ndwi_value),
        'co2_value': validate_number(co2_value),
        'co_value': validate_number(co_value),
        'curah_hujan': validate_number(curah_hujan),
        'suhu': validate_number(suhu),
        'kelembaban': validate_number(kelembaban),
        'kep_pend': validate_number(kep_pend),
        'persen_miskin': validate_number(persen_miskin),
        'rasio_dokter': validate_number(rasio_dokter)
    }

    # Convert the user input to a DataFrame with a single row
    input_df = pd.DataFrame([user_input], columns=st.session_state.df_input.columns)
    
    # Check for None values
    if input_df.isnull().values.any():
        st.error("Please provide valid numeric input")
    else:
        # Append to the existing DataFrame in session state
        st.session_state.df_input = pd.concat([st.session_state.df_input, input_df], ignore_index=True)
        
        st.write("Data stored successfully!")
        st.write(st.session_state.df_input)

# Button to clear all existing data
if clear_all:
    st.session_state.df_input = pd.DataFrame(columns=columns)
    st.write("All existing data has been cleared.")

st.write("")
if st.button('Predict IK DBD Value!'):
    if len(st.session_state.df_input) < 2:
        st.error("Please provide more data input (minimum: 2)")
    else:
        data_used = np.array(st.session_state.df_input)
        scaler = StandardScaler()
        input_scaled = scaler.fit_transform(data_used)      
        
        # Import weight
        weighted_sum_raw = pd.read_csv('https://raw.githubusercontent.com/agungbhaskara23/ai-datathon-ytta2024/master/data/weight_pca.csv')
        weighted_sum = np.array(weighted_sum_raw)
        
        # Calculate the index with new dataset
        count_index = data_used.dot(weighted_sum)
        st.write(data_used)
        st.write(input_scaled)
        st.write(weighted_sum)
        st.write(count_index)
        data_used.shape
        input_scaled.shape
        weighted_sum.shape
        count_index.shape

        # Normalize the weighted sum to the range [0, 1]
        min_max_scaler = MinMaxScaler()
        count_index_normalized = min_max_scaler.fit_transform(count_index)
        st.write(count_index_normalized)
