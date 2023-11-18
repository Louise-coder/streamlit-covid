''' Ce module contient la fonction pour afficher la page dédiée
    à l'aperçu des ensembles de données.
'''

# IMPORTS
import streamlit as st
import pandas as pd


# CONSTANTES
CHEMIN_DATA = "data/owid-covid-data.csv"
OPTIONS_PAYS = [
    "France",
    "Germany",
    "Spain",
    "Italy",
    "Sweden",
    "England"
]


# FONCTIONS
def charger_donnees():
    """Charge et prétraite le jeu de données COVID-19."""
    df_donnees_covid = pd.read_csv(CHEMIN_DATA)
    df_pays_covid = df_donnees_covid[
                    df_donnees_covid["location"].isin(OPTIONS_PAYS)
                    ]
    return df_pays_covid

DF_PAYS_COVID = charger_donnees()  # on charge les données ici dans une variable globale

def afficher_page_donnees():
    """Affiche la page dédiée à la vue d'ensemble des jeux de données."""
    st.header("Vue d'ensemble du jeu de données")
    # Source des données
    st.write(
        "Les données utilisées pour ce projet sont issues du jeu de données \
        COVID-19 de Our World in Data : \
        https://github.com/owid/covid-19-data/tree/master/public/data "
    )
    st.write(
        "Il est mis à jour quotidiennement et inclut des données sur les cas \
        confirmés, les décès, les hospitalisations, les tests, les \
        vaccinations, ainsi que d'autres variables d'intérêt potentiel."
    )
    # Charge et affiche le dataframe
    st.write(
        "Le jeu de données avec seulement les pays sélectionnés pour \
        ce projet, soit la France, l'Allemagne, l'Espagne, l'Italie, \
        la Suède et l'Angleterre :"
    )
    st.dataframe(DF_PAYS_COVID)


if __name__ == "__main__":
    afficher_page_donnees()
