import streamlit as st
from datetime import datetime as dt
from PIL import Image
from common import country_options


st.title("""COVID-19 Time Series Tracker 😷""")


st.sidebar.header("Options")
# Choix de l'utilisateur
selected_country = st.sidebar.selectbox(
    "Select a country", country_options
)
selected_color = st.sidebar.color_picker(
    "Select a color for the curve", "#905DB7"
)
start_date = st.sidebar.date_input("Start date")
end_date = st.sidebar.date_input("End date")

if end_date < start_date:
    st.error("Error: The end date must be later than the start date.")

if st.sidebar.button("Done"):
    # Affichage des choix
    st.write("")
    start_date_f = dt.strftime(start_date, "%d %B %Y")
    end_date_f = dt.strftime(end_date, "%d %B %Y")
    st.write(
        f"Here is the COVID-19 Cases Evolution for {selected_country} from \
        {start_date_f} to {end_date_f}:"
    )
