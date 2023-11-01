## Library importation ##
import streamlit as st
from datetime import datetime as dt, timedelta
import folium 
from streamlit_folium import folium_static
import pandas as pd
import matplotlib.pyplot as plt

## CONSTANT ##
df = pd.read_csv('owid-covid-data.csv')
selected_countries = ['France', 'Germany', 'Spain', 'Italy', 'Sweden', 'England']
df_f = df[df['location'].isin(selected_countries)]


## FUNCTION ##
def format_tooltip_properties(properties, df):
    country_name = properties['NAME']
    total_cases = df.loc[country_name, 'total_cases'] 
    for elem in total_cases:
        if type(elem) == float:
            total_cases = elem
    if country_name == 'Sweden' or country_name == 'England':
        total_cases = "No data"
    tooltip = f'Country: {country_name}<br>Total Cases: {total_cases}'
    return tooltip


def display_map(df):
    europe_map = folium.Map(location=[57, 10], zoom_start=3.3, scrollWheelZoom=False)    
    df_indexed = df.set_index('location')

    choropleth = folium.Choropleth(
        geo_data='carte.geojson',
        data=df_f,
        columns=('location', 'total_cases'),
        key_on='feature.properties.NAME',
        line_opacity=1,
        highlight=True, 
        legend_name="Total cases of COVID19"
    ).add_to(europe_map)

    # Ajoutez un tooltip personnalisé basé sur le DataFrame
    for feature in choropleth.geojson.data['features']:
        tooltip = format_tooltip_properties(feature['properties'], df_indexed)
        feature['properties']['tooltip'] = tooltip

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(fields=['tooltip'], aliases=['Tooltip'], labels=True)
    )
    st_map = folium_static(europe_map, width=700, height=450)


# Fonction pour la page "Projet"
def page_project():
    # Contenu de la page Projet
    st.write("Contenu de la page Projet : Introduction + Fonctionnalité Streamlit")
    st.write("")
    
    st.write("Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. Here is an exemple of the power of Streamlit :")
    display_map(df)
    st.write("The map above shows the total cases of COVID-19 in Europe : the darker blue the country is, the more cases it has. And the grey ones are the countries that have no data.")
    

# Fonction pour la page "Importation des données"
def page_data():
    st.subheader("The Dataset :")
    st.write(f"The dataset used for this project is the COVID-19 dataset from Our World in Data  : https://github.com/owid/covid-19-data/tree/master/public/data ")
    st.write("It is updated daily and includes data on confirmed cases, deaths, hospitalizations, testing, and vaccinations, as well as other variables of potential interest.")
    st.dataframe(df)
    st.write("The dataset with only countries selected for this project, wich are France, Germany, Spain, Italy, Sweden and England :")
    st.dataframe(df_f)     


def page_visualisation():
    # Initialisez l'état de l'expander
    expander_state = True
    with st.expander("Options", expanded=expander_state):
        # Choix de l'utilisateur 
        selected_country = st.selectbox("Select a country", ["France", "Italy", "Germany", "Sweden", "Spain", "England"])
        selected_color = st.color_picker("Select a color for the curve", "#905DB7")
        start_date = st.date_input("Start date")
        end_date = st.date_input("End date", value=start_date + timedelta(days=1))
        # bien de rajouter le choix du type de plot 
        if end_date < start_date or end_date == start_date:
            st.error("Error: The end date must be later than the start date.")

    if st.button("Done"):
        expander_state = False
        st.write("")
        start_date_f = dt.strftime(start_date, "%d %B %Y")
        end_date_f = dt.strftime(end_date, "%d %B %Y")
        st.write(f"Here is the COVID-19 Cases Evolution for {selected_country} from {start_date_f} to {end_date_f}:")
       
        
## MAIN ##
# Project title
st.title("""COVID-19 Time Series Tracker 😷""")

# create a sidebar for navigation
st.sidebar.title("Navigation")
selected_part = st.sidebar.radio('', ["Project", "Dataset", "COVID-19 Cases Evolution"])

# to add space between the radio buttons and the authors
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# create authors section
st.sidebar.markdown("<p style='font-size: 20px; color: white; font-weight: bold;'>Authors</p>", unsafe_allow_html=True)
st.sidebar.text("BENRADHIA Takwa \nBENYAKHLAF Dounia \nLAM Louise\nTOUAMI Essmay")

# Display the selected part
if selected_part == "Project":
    page_project()
if selected_part == "Dataset" :
    page_data()
if selected_part == "COVID-19 Cases Evolution" :
    page_visualisation()