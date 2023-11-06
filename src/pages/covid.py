import streamlit as st
from typing import Tuple, Dict
from pandas import DataFrame
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime as dt, timedelta, date

from common import country_options, df_covid_data_our_countries


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
        value=date.today() - timedelta(days=1),  # Plus pratique
    )
    form_results["end_date"] = st.date_input(
        "End date",
        # value=form_results["start_date"] + timedelta(days=1), #ce n'est pas pratique
    )
    form_results["graph"] = st.selectbox(
        "Select the graph type", ("Curve", "Histogram")
    )
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


def get_data_form_results(form_results: Dict) -> DataFrame:
    # on récupère les cas de covid du pays choisi entre start_date et end_date
    df_data_form_country = df_covid_data_our_countries[
        df_covid_data_our_countries["location"] == form_results["country"]
    ]

    df_data_form_results = df_data_form_country[
        (
            pd.to_datetime(df_data_form_country["date"])
            >= pd.to_datetime(form_results["start_date"])
        )
        & (
            pd.to_datetime(df_data_form_country["date"])
            <= pd.to_datetime(form_results["end_date"])
        )
    ]

    return df_data_form_results


def display_curve(data: Tuple, form_results: Dict):
    # représentation graph sous forme de courbe
    fig = plt.figure(figsize=(8, 8))
    plt.plot(
        data[0],
        data[1],
        color=form_results["color"],
        label="Nombre de cas de COVID-19",
    )
    plt.xlabel("Date")
    plt.ylabel("Nombre de cas")
    plt.title("Évolution du nombre de cas de COVID-19 au cours du temps")
    plt.xticks(
        rotation=45
    )  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
    st.pyplot(fig)


def display_hist(data: Tuple, form_results: Dict):
    # représentation graph sous forme d'histogramme
    fig = plt.figure(figsize=(8, 8))
    plt.bar(data[0], data[1], color=form_results["color"])
    plt.xlabel("Date")
    plt.ylabel("Nombre de cas de COVID-19")
    plt.title("Nombre de cas de COVID-19 par date")
    plt.grid(axis="y")
    plt.xticks(rotation=45)
    st.pyplot(fig)


def display_graph_evolution_form_results(form_results: Dict):
    df_covid_data_form_results = get_data_form_results(form_results)
    x = pd.to_datetime(df_covid_data_form_results["date"])
    y = df_covid_data_form_results["total_cases"]
    if form_results["graph"] == "Curve":
        display_curve((x, y), form_results)
    else:
        display_hist((x, y), form_results)


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


def display_covid_page():
    """Display the COVID-19 Cases Evolution page."""
    initialize_expander_state_to_expanded()
    form_results = display_expander_form_and_get_results()
    submit_form_when_done_clicked(form_results)


# if __name__ == "__main__":
#     display_covid_page()
