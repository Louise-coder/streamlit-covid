"""Module contenant l'application Streamlit COVID.

Utilisation :
=============
Depuis le dépôt streamlit-covid/, exécutez :
    streamlit run src/demo.py

"""

__auteurs__ = (
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


# IMPORTS
import streamlit as st
from Nvlle_version.src.pages.introduction import affiche_page_intro
from Nvlle_version.src.pages.datasets import afficher_page_donnees
from pages.covid import display_covid_page


# FONCTIONS
def afficher_sidebar_et_selectionner_page(): 
    """Affiche la barre latérale et sélectionne la page.

    Returns
    -------
    page_selectionnee : str
        Le nom de la page sélectionnée.
    """
    st.sidebar.title("Navigation")
    # Affiche les boutons radio dans la barre latérale
    # Récupère la page sélectionnée
    page_selectionnee = st.sidebar.radio(
        "mes_boutons_radio",
        [
            "Qu'est-ce que Streamlit ?",
            "Vue d'ensemble des données",
            "Évolution des cas de COVID-19",
        ],
        label_visibility="hidden",
    )
    # Ajoute de l'espace
    st.sidebar.markdown("<br><br><br>", unsafe_allow_html=True)

    # Affichage des auteurs dans la barre latérale
    st.sidebar.markdown(
        "<p style='font-size: 20px;\
        color: white;\
        font-weight: bold;\
        '>Auteurs</p>",
        unsafe_allow_html=True,
    )
    for auteur in __auteurs__:
        st.sidebar.text(auteur)

    return page_selectionnee


def afficher_page_selectionnee(selected_page: str):
    """Affiche la page sélectionnée.

    Parameters
    ----------
    page_selectionnee : str
        Le nom de la page à afficher.
    """
    if selected_page == "Qu'est-ce que Streamlit ?":
        affiche_page_intro()
    elif selected_page == "Vue d'ensemble des données":
        afficher_page_donnees()
    else:
        display_covid_page()


# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    NO_SIDEBAR_STYLE = """ 
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(NO_SIDEBAR_STYLE, unsafe_allow_html=True)

    st.title("""Évolution des cas de COVID-19 😷""")
    ma_page = afficher_sidebar_et_selectionner_page()
    afficher_page_selectionnee(ma_page)
