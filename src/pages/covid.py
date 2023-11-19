from datetime import datetime as dt, timedelta, date
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


from pages.datasets import DF_PAYS_COVID, OPTIONS_PAYS


def display_expander_form_and_get_results():
    """Display expander and his form and get the results.

    Returns
    -------
    form_results : Dict
        The dictionnary containing the results of the form.
    """
    with st.expander("Options", expanded=True):
        # FORMULAIRE
        form_results = dict()
        form_results["country"] = st.selectbox(
            "Select a country", OPTIONS_PAYS
        )
        form_results["color"] = st.color_picker(
            "Select a color for the curve", "#905DB7"
        )
        form_results["start_date"] = pd.to_datetime(
            st.date_input(
                "Start date",
                value=date.today() - 3 * timedelta(days=365),
            )
        )
        form_results["end_date"] = pd.to_datetime(
            st.date_input(
                "End date",
            )
        )
        # Erreur si dates incompatibles
        if (
            form_results["end_date"] < form_results["start_date"]
            or form_results["end_date"] == form_results["start_date"]
        ):
            st.error(
                "Error: The end date must be later than the start date."
            )
    return form_results


def get_data_from_results(form_results):
    """Return data on covid cases in the selected country
    between start date and end date.

    Parameters
    ----------
    form_results : Dict
        The dictionnary containing the results of the form.

    Returns
    -------
    df_data_form_results : DataFrame
        data on covid cases
    """
    # Les données du pays
    df_data_form_country = DF_PAYS_COVID[
        DF_PAYS_COVID["location"] == form_results["country"]
    ]
    # casting dans le bon type
    df_data_form_country["date"] = pd.to_datetime(
        df_data_form_country["date"]
    )
    data_after_start_date = (
        df_data_form_country["date"] >= form_results["start_date"]
    )
    data_before_end_date = (
        df_data_form_country["date"] <= form_results["end_date"]
    )
    data_btw_start_end = data_after_start_date & data_before_end_date
    df_data_form_results = df_data_form_country[data_btw_start_end]
    return df_data_form_results


def display_graph_evolution_form_results(form_results):
    """Display the selected graph of covid cases.

    Parameters
    ----------
    form_results : Dict
        The dictionnary containing the results of the form.
    """
    df_covid_data_form_results = get_data_from_results(form_results)
    x = df_covid_data_form_results["date"]
    y = df_covid_data_form_results["total_cases"]
    fig = plt.figure(figsize=(8, 8))
    plt.plot(
        x,
        y,
        color=form_results["color"],
        label="Number of cumulated COVID-19 cases",
    )
    plt.xlabel("Date")
    plt.ylabel("Number of cumulated cases")
    plt.title(
        "Evolution of the number of cumulated COVID-19 cases over time"
    )
    plt.xticks(rotation=45)
    st.pyplot(fig)


def display_covid_page():
    """Display the COVID-19 Cases Evolution page."""
    # Afficher et récupérer les données du formulaire
    form_results = display_expander_form_and_get_results()
    # Soumettre le formulaire en cliquant sur Done
    if st.button("Done", key="done_button"):
        st.write("")  # mettre des espaces
        start_date_f = dt.strftime(form_results["start_date"], "%d %B %Y")
        end_date_f = dt.strftime(form_results["end_date"], "%d %B %Y")
        st.write(
            f"""Here is the COVID-19 Cases Evolution for \
            {form_results["country"]} from {start_date_f} to \
            {end_date_f}:
            """
        )
        display_graph_evolution_form_results(form_results)


if __name__ == "__main__":
    display_covid_page()
