# Suivi des cas de COVID-A9 avec Streamlit 😷

## Table des matières
1. [Introduction](#introduction)
2. [Contributeurs](#project-contributors)
3. [Description](#project-description)
4. [Pour Commencer](#getting-started)
5. [Détails Techniques](#technical-details)


## Introduction
Ce projet, développé dans le cadre de l'UE Python2, présente un tableau de bord Covid-19 basé sur Streamlit. Le tableau de bord permet aux utilisateurs de suivre l'évolution des cas de Covid-19 au fil du temps pour certains pays sélectionnés, avec des options de personnalisation de l'affichage. 

**Streamlit**, la technologie fondamentale derrière cette application, est une bibliothèque Python open-source conçue pour créer facilement des applications web interactives. En intégrant Streamlit, ce projet offre une interface user-friendly pour surveiller les cas de Covid-19, la rendant accessible et informative !

## Contributeurs
- BENRADHIA Takwa
- BENYAKHLAF Dounia
- LAM Louise
- TOUAMI Essmay

## Description
Le tableau de bord Covid Streamlit propose les fonctionnalités suivantes :

1. **Sélection du Pays**: Les utilisateurs peuvent choisir l'un des pays suivants : France, Italie, Allemagne, Suède, Espagne ou Angleterre.

2. **Sélection de la Couleur**: Les utilisateurs peuvent personnaliser la couleur du graphique en ligne représentant l'évolution des cas de Covid-19.

3. **Sélection de la Plage de Dates**: Les utilisateurs peuvent spécifier les dates de début et de fin pour la visualisation.

4. **Visualisation**:  L'application utilise Matplotlib pour afficher l'évolution des cas de Covid-19 au fil du temps pour le pays sélectionné.

Pour visionner une démonstration du projet, consultez notre [vidéo de démo sur Canva](https://www.canva.com/design/DAFy1Cxgkag/GLL2fKyUclNy0Ky3sJCWDw/edit?utm_content=DAFy1Cxgkag&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).


## Pour Commencer
Pour exécuter l'application, suivez ces étapes :

1. Clonez ce dépôt.
   ```bash
   git clone <https://github.com/Louise-coder/streamlit-covid>
   ```

2. Installez les bibliothèques requises.
    ```bash
    pip install streamlit pandas matplotlib folium streamlit_folium # avec pip
    conda install -y streamlit pandas matplotlib folium streamlit_folium # avec conda
    ```
3. Run the Application.

Accédez au répertoire du projet dans votre terminal et exécutez la commande suivante :
```bash 
streamlit run src/demo.py
```
Après avoir exécuté la commande ci-dessus, une nouvelle fenêtre de navigateur s'ouvrira, et vous pourrez interagir avec le tableau de bord Streamlit Covid.

Alternativement, vous pouvez accéder à l'application directement via le lien Streamlit suivant :

[![Click here!](https://img.shields.io/badge/Click%20here%21-Open%20Streamlit%20Covid%20Dashboard-blue?style=for-the-badge)]()




## Détails Techniques

- **Python Version**: 3.10
- **Streamlit Version**: 1.28.0
- **Matplotlib Version**: 3.8.2
- **Pandas Version**: 2.1.3



👋 Explorez les dernières données sur la COVID-19 avec notre Tableau de Bord Streamlit Covid19 et restez informé(e) sans effort !

