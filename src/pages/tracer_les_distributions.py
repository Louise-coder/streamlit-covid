"""Ce module contient tout ce qui est relatif aux distributions COVID."""

from datetime import timedelta, date
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from pages.les_datasets_covid import DF_PAYS_COVID, OPTIONS_PAYS


def affiche_formulaire_et_recupere_resultats():
    """Affiche le formulaire et recupere les resultats.

    Returns
    -------
    resultats_form : Dict
        Le dictionnaire contenant tous les resultats du formulaire.
    """
    with st.expander("Options", expanded=True):
        # construction du formulaire et recuperation des choix
        resultats_form = {}  # dictionnaire
        resultats_form["pays"] = st.selectbox(
            "Choix du pays", OPTIONS_PAYS
        )
        resultats_form["couleur"] = st.color_picker(
            "Choix de la couleur pour la courbe", "#905DB7"
        )
        resultats_form["date_debut"] = st.date_input(
            "Date de début",
            # par defaut on prend debut = 3 ans avant date d'ajd
            value=date.today() - 3 * timedelta(days=365),
        )
        resultats_form["date_fin"] = st.date_input(
            "Date de fin",
        )  # par defaut on prend fin = ajd
        # Erreur si dates incompatibles
        if (
            resultats_form["date_fin"] < resultats_form["date_debut"]
            or resultats_form["date_fin"] == resultats_form["date_debut"]
        ):
            st.error(
                "Error: The end date must be later than the start date."
            )
    return resultats_form


def recupere_donnees(resultats_form):
    """Recupere les donnees specifiques correspondant aux choix de l'user.

    Parameters
    ----------
    resultats_form : Dict
        Le dictionnaire contenant les resultats du formulaire.

    Returns
    -------
    donnees_choisies : DataFrame
        Les donnees selectionnees a partir des filtres.
    """
    # Les donnees du pays
    donnees_de_mon_pays = DF_PAYS_COVID[
        DF_PAYS_COVID["location"] == resultats_form["pays"]
    ]
    # Masques pour selectionner la periode entre date_debut et date_fin
    apres_date_debut = pd.to_datetime(
        donnees_de_mon_pays["date"]
    ) >= pd.to_datetime(resultats_form["date_debut"])
    avant_date_fin = pd.to_datetime(
        donnees_de_mon_pays["date"]
    ) <= pd.to_datetime(resultats_form["date_fin"])
    periode_choisie = apres_date_debut & avant_date_fin
    # Application du masque sur les donnees
    donnees_choisies = donnees_de_mon_pays[periode_choisie]
    return donnees_choisies


def affiche_graphe_choisi(resultats_form):
    """Affiche le graphe correspondant aux choix du formulaire.

    Parameters
    ----------
    resultats_form : Dict
        Le dictionnaire contenant les resultats du formulaire.
    """
    # On recupere les donnees correspondant au formulaire
    donnees_choisies = recupere_donnees(resultats_form)
    # On veut tracer le nombre de cas (y) en fonction de la date (x)
    x_dates = pd.to_datetime(donnees_choisies["date"])
    y_nb_cas = donnees_choisies["total_cases"]
    # Construction du graphe y_nb_cas = f(x_dates)
    fig = plt.figure(figsize=(8, 8))
    plt.plot(x_dates, y_nb_cas, color=resultats_form["couleur"])
    # Legendes
    plt.xlabel("Dates")
    plt.xticks(rotation=45)  # rotation des dates pour incliner
    plt.ylabel("Nombre de cas cumulés")
    plt.title(
        f"Nombre de cas cumulés en {resultats_form['pays']} du COVID-19\n \
        du {resultats_form['date_debut']} au {resultats_form['date_fin']}"
    )
    # Affichage du graphe
    st.pyplot(fig)


def affiche_page_covid():
    """Affiche la page correspondant au tracage des distributions COVID."""
    st.write("Pour tracer une distribution de cas cumulés COVID : ")
    # Afficher et recuperer les donnees du formulaire
    resultats_form = affiche_formulaire_et_recupere_resultats()
    # Lorsque l'utilisateur demande a voir la distribution avec le bouton
    if st.button("Afficher distribution", key="done_button"):
        # Affichage du graphe choisi dans le formulaire
        affiche_graphe_choisi(resultats_form)


if __name__ == "__main__":
    affiche_page_covid()
