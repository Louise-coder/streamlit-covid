"""Module containing the Streamlit covid application.

Usage:
======
From streamlit-covid/ repository, run:
    streamlit run src/demo.py

"""

__authors__ = (
    "Takwa BEN RADHIA",
    "Dounia BENYAKHLAF",
    "Louise LAM",
    "Essmay TOUAMI",
)
__contacts__ = (
    "takwa.ben-radhia@etu.u-paris.fr",
    "dounia.benyakhlaf@etu.u-paris.fr",
    "louise.lam@etu.u-paris.fr",
    "essmay.touami@etu.u-paris.fr",
)
__copyright__ = "Universite Paris-Cite"
__date__ = "2023"

import streamlit as st


from common import PROJECT_TITLE
from pages.introduction import display_introduction_page
from pages.datasets import display_datasets_page
from pages.covid import display_covid_page


def display_sidebar_page_choices_and_get_selected_page():
    """Display the pages in radio button format and returns the selected page.

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
    st.sidebar.title("Navigation")
    selected_page = display_sidebar_page_choices_and_get_selected_page()
    st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)
    display_authors_sidebar()
    return selected_page


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
        display_datasets_page()
    else:
        display_covid_page()


if __name__ == "__main__":
    # ? est ce qu'on veut garder les radiobuttons ou utiliser la
    # ? navigation par défaut de streamlit ?
    NO_SIDEBAR_STYLE = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(NO_SIDEBAR_STYLE, unsafe_allow_html=True)

    st.title(PROJECT_TITLE)
    my_selected_page = display_sidebar_and_get_selected_page()
    display_selected_page(my_selected_page)
