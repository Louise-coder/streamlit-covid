"""File containing all the common variables."""
import pandas as pd

PROJECT_TITLE = """COVID-19 Time Series Tracker 😷"""
CSV_FILE_PATH = "owid-covid-data.csv"

# ? CSTES mais au travail on m'a dit que objets pas en maj... on fait quoi?
country_options = [
    "France",
    "Germany",
    "Spain",
    "Italy",
    "Sweden",
    "England",
    "World"
]
df_covid_data = pd.read_csv("data/" + CSV_FILE_PATH)
df_covid_data_our_countries = df_covid_data[
    df_covid_data["location"].isin(country_options)
]
