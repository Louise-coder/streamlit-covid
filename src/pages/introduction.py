''' Ce module contient la fonction pour afficher la page dédiée
    à introduire streamlit.
'''

# IMPORTS
import streamlit as st
import folium
from streamlit_folium import folium_static
from pages.datasets import DF_PAYS_COVID


# CLASSE CARTE
class CarteCovid:
    """Classe pour la carte des cas COVID-19."""
    def __init__(self, df_initial):
        """Initialise la classe CarteCovid.

        Paramètres
        ----------
        df_covid_data : DataFrame
            Le DataFrame contenant les données COVID.
        """
        self.df_pays_covid = df_initial


    def formater_infobulle_proprietes(self, properties, df_index) -> str:
        """Formate les propriétés pour afficher dans une infobulle.

        Paramètres
        ----------
        properties : dict
            Dictionnaire des propriétés du pays.

        Retourne
        -------
        infobulle : str
            Texte pour l'infobulle.
        """
        # Récupère le nom du pays
        nom_pays = properties["NAME"]
        # Récupère le nombre total de cas
        cas_total = df_index.loc[nom_pays, "total_cases"]
        # Traitement des cas où le nombre total est de type float
        if isinstance(cas_total, float):
            cas_total = int(cas_total)
        # Traitement des cas sans données
        if nom_pays in ('Suède', 'Angleterre'):
            cas_total = "Pas de données"
        # Construction du texte de l'infobulle
        infobulle = f"Pays : {nom_pays}<br>Cas totaux : {cas_total}"
        return infobulle


    def affiche_carte(self):
        """Affiche la carte correspondant au DataFrame des données COVID.
        Parameters
        ----------
        self : objet
            L'instance de la classe CarteCovid.
        """
        # Création de la carte centrée sur l'Europe
        carte_europe = folium.Map(location=[57, 10], zoom_start=3.3, scrollWheelZoom=False)
        # Ajout d'une couche choroplèthe à la carte
        choropleth = folium.Choropleth(
            # Fichier GeoJSON définissant les frontières des pays
            geo_data="data/covid-map.geojson",
            # DataFrame contenant les données COVID
            data=self.df_pays_covid,
            # Colonnes à utiliser dans le DataFrame
            columns=("location", "total_cases"),
            # Clé pour faire correspondre les données GeoJSON et DataFrame
            key_on="feature.properties.NAME",
            # Met en évidence les pays au survol de la souris
            highlight=True,
            # Légende
            legend_name="Cas totaux de COVID19",
        ).add_to(carte_europe)  # Ajoute la couche à la carte

        # Indexation du DataFrame par le nom du pays
        df_index = self.df_pays_covid.set_index("location")

        # Ajout des infobulles personnalisées basées sur le DataFrame
        for feature in choropleth.geojson.data["features"]:
            # Formatage des infobulles
            infobulle = self.formater_infobulle_proprietes(
                            feature["properties"], df_index
                            )
            # Ajout des infobulles aux propriétés du GeoJSON
            feature["properties"]["infobulle"] = infobulle

        # Ajout d'une couche d'infobulles à la carte
        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(
                fields=["infobulle"],  # Les données à afficher
                labels=True   # Affiche l'étiquette des données
            )
        )

        # Affichage de la carte dans le cadre Streamlit
        folium_static(carte_europe, width=700, height=450)


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
    # Création de l'objet CarteCovid et affichage de la carte
    carte_covid = CarteCovid(DF_PAYS_COVID)
    carte_covid.affiche_carte()

    # afficher la description de la carte
    st.write(
        "La carte ci-dessus montre les cas totaux de COVID-19 dans certains\
        pays d'Europe : plus le pays est en bleu foncé, plus il a de cas. \
        Et les pays gris sont ceux qui n'ont pas de données."
    )


if __name__ == "__main__":
    affiche_page_intro()
