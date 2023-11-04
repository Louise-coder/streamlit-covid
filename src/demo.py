"""Module containing the Streamlit covid application.

Usage:
======
From streamlit-covid/ repository, run:
    streamlit run src/demo.py

"""

__authors__ = (
    "Takwa BENRADHIA",
    "Dounia BENYAKHLAF",
    "Louise LAM",
    "Essmay TOUAMI",
)
__contacts__ = (
    "takwa.benradhia@etu.u-paris.fr",
    "dounia.benyakhlaf@etu.u-paris.fr",
    "louise.lam@etu.u-paris.fr",
    "essmay.touami@etu.u-paris.fr",
)
__copyright__ = "Universite Paris-Cite"
__date__ = "2023"

from datetime import datetime as dt, timedelta, date
import folium
from folium import Map

# TODO utiliser matplotlib
import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
from streamlit import expander
from typing import Tuple, Dict
from pandas import DataFrame

# ? POURQUOI CETTE LIGNE EST SOULIGNE PAR LE LINTER ?
from common import PROJECT_TITLE, CSV_FILE_PATH, country_options


# ? CSTES mais au travail on m'a dit que objets pas en maj... on fait quoi?
df_covid_data = pd.read_csv("data/" + CSV_FILE_PATH)
df_covid_data_our_countries = df_covid_data[
    df_covid_data["location"].isin(country_options)
]


def format_tooltip_properties(properties, df: DataFrame) -> str:
    """_summary_

    Parameters
    ----------
    properties : _type_
        _description_
    df : DataFrame
        _description_

    Returns
    -------
    tooltip : str
        _description_
    """
    country_name = properties["NAME"]  # ? un dictionnaire ?
    total_cases = df.loc[country_name, "total_cases"]
    for elem in total_cases:
        if type(elem) == float:
            total_cases = elem
    if country_name == "Sweden" or country_name == "England":
        total_cases = "No data"
    tooltip = f"Country: {country_name}<br>Total Cases: {total_cases}"
    return tooltip


def display_project_title():
    """Display the project title on the center of the page."""
    st.title(PROJECT_TITLE)


def display_sidebar_title():
    """Display the sidebar's title."""
    st.sidebar.title("Navigation")


def display_sidebar_page_choices_and_get_selected_page():
    """Display the pages in radio button format and returns the selected
    page.

    Returns
    -------
    selected_page: str
        The name of the selected page.
    """
    selected_page = st.sidebar.radio(
        "my_radio_buttons",
        [
            "What is streamlit?",
            "Overview on the datasets",
            "COVID-19 Cases Evolution",
        ],
        label_visibility="hidden",
    )
    return selected_page


def display_spaces_sidebar():
    """Display some spaces in the sidebar"""
    st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)


def display_authors_sidebar():
    """Display the authors in the sidebar."""
    st.sidebar.markdown(
        "<p style='font-size: 20px;\
        color: white;\
        font-weight: bold;\
        '>Authors</p>",
        unsafe_allow_html=True,
    )
    for author in __authors__:
        st.sidebar.text(author)


def display_sidebar_and_get_selected_page():
    """Display the sidebar and get the name of the selected page.
    Returns
    -------
    selected_page: str
        The name of the selected page.
    """
    display_sidebar_title()
    selected_page = display_sidebar_page_choices_and_get_selected_page()
    display_spaces_sidebar()
    display_authors_sidebar()
    return selected_page


def display_title_page(title: str):
    """Take a title and display it."""
    st.header(title)


def display_streamlit_introduction():
    """Display the introduction: what is streamlit?"""
    st.write(
        "Streamlit is an open-source Python library that makes it easy to \
        create and share beautiful, custom web apps for machine learning \
        and data science. Here is an exemple of the power of Streamlit:"
    )


def get_europe_map() -> Map:
    """Get Europe map.

    Returns
    -------
    europe_map : Map
        The Europe map.
    """
    europe_map = folium.Map(
        location=[57, 10], zoom_start=3.3, scrollWheelZoom=False
    )
    return europe_map


def display_map(covid_data_df: DataFrame):
    """Display the map corresponding to the df containing covid data.

    Parameters
    ----------
    covid_data_df : DataFrame
        The dataframe containing covid data.
    """
    europe_map = get_europe_map()
    choropleth = folium.Choropleth(
        geo_data="data/covid-map.geojson",
        data=df_covid_data_our_countries,
        columns=("location", "total_cases"),
        key_on="feature.properties.NAME",
        line_opacity=1,
        highlight=True,
        legend_name="Total cases of COVID19",
    ).add_to(europe_map)
    df_indexed = covid_data_df.set_index("location")
    # Ajoutez un tooltip personnalisé basé sur le DataFrame
    for feature in choropleth.geojson.data["features"]:
        tooltip = format_tooltip_properties(
            feature["properties"], df_indexed
        )
        feature["properties"]["tooltip"] = tooltip

    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(
            fields=["tooltip"], aliases=["Tooltip"], labels=True
        )
    )
    st_map = folium_static(europe_map, width=700, height=450)


def display_map_description():
    """Display the map's description."""
    st.write(
        "The map above shows the total cases of COVID-19 in Europe: the \
        darker blue the country is, the more cases it has. And the grey \
        ones are the countries that have no data."
    )


def display_introduction_page():
    """Display the what's streamlit page."""
    display_title_page("What is streamlit?")
    display_streamlit_introduction()
    display_map(df_covid_data)
    display_map_description()


def display_dataset_introduction():
    """Display the Importation des données page."""
    st.write(
        "The dataset used for this project is the COVID-19 dataset from \
        Our World in Data: \
        https://github.com/owid/covid-19-data/tree/master/public/data "
    )
    st.write(
        "It is updated daily and includes data on confirmed cases, deaths,\
        hospitalizations, testing, and vaccinations, as well as other \
        variables of potential interest."
    )


def display_dataframe(dataframe: DataFrame):
    """Display a dataframe.

    Parameters
    ----------
    dataframe : DataFrame
        The dataframe to display.
    """
    st.dataframe(dataframe)


def display_dataset_description():
    """Display dataset description."""
    st.write(
        "The dataset with only countries selected for this project,\
        wich are France, Germany, Spain, Italy, Sweden and England:"
    )


def display_dataset_page():
    """Display the page dedicated to the overview of the datasets."""
    display_title_page("Overview of the datasets")
    display_dataset_introduction()
    display_dataframe(df_covid_data)
    display_dataset_description()
    display_dataframe(df_covid_data_our_countries)


def verify_dates(start_date: dt, end_date: dt) -> Tuple:
    """Verify that the start_date is before the end_date.

    Parameters
    ----------
    start_date : dt
        The starting date.
    end_date : dt
        The ending date.
    """
    if end_date < start_date or end_date == start_date:
        st.error("Error: The end date must be later than the start date.")


def initialize_expander_state_to_expanded():
    """Initialize the state of the expander to expanded."""
    if "expander_state" not in st.session_state:
        st.session_state["expander_state"] = True


def display_form_and_get_results() -> Dict:
    """Display the form and get the results.

    Returns
    -------
    form_results : Dict
        The dictionnary containing the results of the form.
    """
    form_results = dict()
    form_results["country"] = st.selectbox(
        "Select a country", country_options
    )
    form_results["color"] = st.color_picker(
        "Select a color for the curve", "#905DB7"
    )
    form_results["start_date"] = st.date_input(
        "Start date",
        value=date.today() - timedelta(days=1) # Plus pratique
    )
    form_results["end_date"] = st.date_input(
        "End date",
        #value=form_results["start_date"] + timedelta(days=1), #ce n'est pas pratique
    )
    form_results["graph"] = st.selectbox(
        'Select the graph type',
        ('Curve','Histogram'))
    verify_dates(form_results["start_date"], form_results["end_date"])
    return form_results


def display_expander_form_and_get_results() -> Dict:
    """Display expander and his form and get the results.

    Returns
    -------
    form_results : Dict
        The dictionnary containing the results of the form.
    """
    with st.expander(
        "Options", expanded=st.session_state["expander_state"]
    ):
        form_results = display_form_and_get_results()
    return form_results


def close_expander():
    """Put the expander state to not expanded."""
    st.session_state["expander_state"] = False


def get_data_form_results(form_results : Dict) -> DataFrame:
    #on récupère les cas de covid du pays choisi entre start_date et end_date
    df_data_form_country = df_covid_data_our_countries[df_covid_data_our_countries["location"] == form_results["country"]]
    
    df_data_form_results = df_data_form_country[
        (pd.to_datetime(df_data_form_country["date"]) >= pd.to_datetime(form_results["start_date"])) &
        (pd.to_datetime(df_data_form_country["date"]) <= pd.to_datetime(form_results["end_date"]))
    ]
    
    return df_data_form_results


def display_curve(data : Tuple, form_results : Dict):
    #représentation graph sous forme de courbe
    fig = plt.figure(figsize=(8,8))
    plt.plot(data[0], data[1], color = form_results["color"], label='Nombre de cas de COVID-19')
    plt.xlabel('Date')
    plt.ylabel('Nombre de cas')
    plt.title('Évolution du nombre de cas de COVID-19 au cours du temps')
    plt.xticks(rotation=45)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
    st.pyplot(fig)


def display_hist(data : Tuple, form_results : Dict):
    #représentation graph sous forme d'histogramme
    fig = plt.figure(figsize=(8, 8))
    plt.bar(data[0], data[1], color = form_results["color"])
    plt.xlabel('Date')
    plt.ylabel('Nombre de cas de COVID-19')
    plt.title('Nombre de cas de COVID-19 par date')
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    st.pyplot(fig)


def display_graph_evolution_form_results(form_results: Dict):
    df_covid_data_form_results = get_data_form_results(form_results)
    x = pd.to_datetime(df_covid_data_form_results["date"])
    y = df_covid_data_form_results["total_cases"]
    if form_results["graph"] == "Curve":
        display_curve((x,y), form_results)
    else :
        display_hist((x,y), form_results)


def submit_form_when_done_clicked(form_results: Dict):
    """Submit the form results (and close the expander) when the Done
    button is clicked.

    Parameters
    ----------
    form_results : Dict
        The dictionnary containing the results of the form.
    """
    if st.button("Done", key="done_button", on_click=close_expander):
        st.write("")
        start_date_f = dt.strftime(form_results["start_date"], "%d %B %Y")
        end_date_f = dt.strftime(form_results["end_date"], "%d %B %Y")
        st.write(
            f"""Here is the COVID-19 Cases Evolution for \
            {form_results["country"]} from {start_date_f} to \
            {end_date_f}:
            """
        )
        display_graph_evolution_form_results(form_results)


def display_visualisation_page():
    """Display the COVID-19 Cases Evolution page."""
    initialize_expander_state_to_expanded()
    form_results = display_expander_form_and_get_results()
    submit_form_when_done_clicked(form_results)


def display_selected_page(selected_page: str):
    """Display the selected page.

    Parameters
    ----------
    selected_page : str
        The name of the page to display.
    """
    if selected_page == "What is streamlit?":
        display_introduction_page()
    elif selected_page == "Overview on the datasets":
        display_dataset_page()
    else:
        display_visualisation_page()


if __name__ == "__main__":
    display_project_title()
    my_selected_page = display_sidebar_and_get_selected_page()
    display_selected_page(my_selected_page)
