import streamlit as st
from pandas import DataFrame
from common import df_covid_data, df_covid_data_our_countries


def display_datasets_introduction():
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


def display_datasets_description():
    """Display dataset description."""
    st.write(
        "The dataset with only countries selected for this project,\
        wich are France, Germany, Spain, Italy, Sweden and England:"
    )


def display_datasets_page():
    """Display the page dedicated to the overview of the datasets."""
    st.header("Overview of the datasets")
    display_datasets_introduction()
    display_dataframe(df_covid_data)
    display_datasets_description()
    display_dataframe(df_covid_data_our_countries)


# if __name__ == "__main__":
#     display_datasets_page()
