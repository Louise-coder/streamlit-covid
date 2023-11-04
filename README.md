# Streamlit COVID-19 Time Series Tracker 😷

## Table of contents
1. [Introduction](#introduction)
2. [Project Contributors](#project-contributors)
3. [Project Description](#project-description)
4. [Getting Started](#getting-started)
5. [Technical Details](#technical-details)


## Introduction
This project, developed as part of the UE Python2, presents a Streamlit-based Covid19 Dashboard. The dashboard allows users to track the progression of Covid-19 cases over time for selected countries, with options to customize the display. 

**Streamlit**, the foundational technology behind this application, is an open-source Python library designed for creating interactive web applications effortlessly. It empowers data scientists and developers to transform data, visualizations, and analyses into user-friendly web applications with minimal code. By integrating Streamlit, this project provides a user-friendly interface for monitoring Covid-19 cases, making it accessible and informative !

## Project Contributors
- BENRADHIA Takwa
- BENYAKHLAF Dounia
- LAM Louise
- TOUAMI Essmay

## Project Description
The Streamlit Covid Dashboard provides the following functionalities:

1. **Country Selection**: Users can choose one of the following countries: France, Italy, Germany, Sweden, Spain, or England.

2. **Color Selection**: Users can customize the color of the line chart representing the Covid-19 cases' evolution.

3. **Date Range Selection**: Users can specify the start and end dates for visualization.

4. **Visualization**: The application uses Matplotlib to display the Covid-19 cases' evolution over time for the selected country.

To watch a demonstration of the project, view our [demo video on Canva](https://www.canva.com/design/DAFy1Cxgkag/GLL2fKyUclNy0Ky3sJCWDw/edit?utm_content=DAFy1Cxgkag&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).


## Getting Started
To run the application, follow these steps:

1. Clone this repository.
   ```bash
   git clone <https://github.com/Louise-coder/streamlit-covid>
   ```

2. Install Required Libraries
    ```bash
    pip install streamlit pandas matplotlib folium streamlit_folium # with pip
    conda install -y streamlit pandas matplotlib folium streamlit_folium # with conda mais tout marche pas...
    ```
3. Run the Application.

Navigate to the project directory in your terminal and execute the following command:
```bash 
streamlit run src/demo.py
```
After running the above command, a new browser window will open, and you'll be able to interact with the Streamlit Covid Dashboard.

Alternatively, you can access the application directly via the following Streamlit link: 

[![Click here!](https://img.shields.io/badge/Click%20here%21-Open%20Streamlit%20Covid%20Dashboard-blue?style=for-the-badge)](https://your-streamlit-app-link-here)




## Technical Details

- **Python Version**: 3.10
- **Streamlit Version**: 1.28.0
- **Matplotlib Version**: insert_latest_version_here
- **Pandas Version**: insert_latest_version_here



👋 Explore the latest Covid-19 data with our Streamlit Covid19 Dashboard and stay informed effortlessly !

