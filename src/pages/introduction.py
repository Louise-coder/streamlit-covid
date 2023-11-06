import folium
from folium import Map
import streamlit as st
from streamlit_folium import folium_static
from pandas import DataFrame
from common import df_covid_data, df_covid_data_our_countries


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
    st.header("What is streamlit?")
    display_streamlit_introduction()
    display_map(df_covid_data)
    display_map_description()


