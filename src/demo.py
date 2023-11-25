"""Ce module contient tout ce qui est relatif a la page d'introduction.

Utilisation :
=============
Depuis le depôt streamlit-covid/, executez :
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
__date__ = "Novembre 2023"

# IMPORTS
import streamlit as st

# POUR LA CARTE
import folium
from streamlit_folium import folium_static
from pages.les_datasets_covid import DF_PAYS_COVID


# CLASSE CARTE
class CarteCovid:
    """Classe pour la carte des cas COVID-19."""

    def __init__(self, df_initial):
        """Initialise la classe CarteCovid.

        Paramètres
        ----------
        df_covid_data : DataFrame
            Le DataFrame contenant les donnees COVID.
        """
        self.df_pays_covid = df_initial

    def affiche_carte(self):
        """Affiche la carte correspondant au DataFrame des donnees COVID.

        Parameters
        ----------
        self : objet
            L'instance de la classe CarteCovid.
        """
        # Creation de la carte centree sur l'Europe
        carte_europe = folium.Map(
            location=[57, 10], zoom_start=3.3, scrollWheelZoom=False
        )
        # Ajout d'une couche choroplèthe à la carte
        folium.Choropleth(
            # Fichier GeoJSON definissant les frontières des pays
            geo_data="data/covid-map.geojson",
            # DataFrame contenant les donnees COVID
            data=self.df_pays_covid,
            # Colonnes à utiliser dans le DataFrame
            columns=("location", "total_cases"),
            # Cle pour faire correspondre les donnees GeoJSON et DataFrame
            key_on="feature.properties.NAME",
            # Met en evidence les pays au survol de la souris
            # highlight=True,
            # Legende
            legend_name="Cas totaux de COVID19",
        ).add_to(
            carte_europe
        )  # Ajoute la couche à la carte

        # Affichage de la carte dans le cadre Streamlit
        folium_static(carte_europe, width=700, height=450)


def affiche_autrices_sidebar():
    """Affiche la barre laterale contenant les autrices."""
    st.sidebar.title("Autrices")
    # On parcourt chaque autrice et on l'affiche
    for autrice in __auteurs__:
        st.sidebar.text(autrice)


# FONCTION
def affiche_page_intro():
    """Affiche la page 'Qu'est-ce que Streamlit?'."""
    st.header("Qu'est-ce que Streamlit?")
    # afficher la description de streamlit
    st.write(
        "Streamlit est une bibliothèque Python open-source qui facilite \
        la création et le partage d'applications web personnalisées pour \
        l'apprentissage automatique et la science des données."
    )
    # Creation de l'objet CarteCovid et affichage de la carte
    carte_covid = CarteCovid(DF_PAYS_COVID)
    carte_covid.affiche_carte()

    # afficher la description de la carte
    st.write(
        "La carte ci-dessus montre les cas totaux de COVID-19 dans \
        certains pays d'Europe : plus le pays est en bleu foncé, plus il \
        a de cas. Et les pays gris sont ceux qui n'ont pas de données."
    )


if __name__ == "__main__":
    affiche_autrices_sidebar()
    affiche_page_intro()
