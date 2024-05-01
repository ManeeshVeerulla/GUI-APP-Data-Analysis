import pandas as pd
import requests
from bs4 import BeautifulSoup
import io
from tkinter import messagebox, filedialog

# Global variables to store fetched datasets
covid_df = None
who_df = None
population_df = None
quality_of_life_df = None

# Function to fetch COVID-19 data
def get_covid_data():
    global covid_df
    
    # URL of the CSV file
    url = "https://github.com/owid/covid-19-data/raw/master/public/data/cases_deaths/COVID-19%20Cases%20and%20deaths%20-%20WHO.csv"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Read the content of the response (the CSV file)
        csv_content = response.content
        
        # Convert the CSV content to a DataFrame using pandas
        covid_df = pd.read_csv(io.StringIO(csv_content.decode('utf-8')))
        return True, "COVID-19 data has been fetched successfully."
    else:
        return False, "Failed to retrieve COVID-19 data from the URL."

# Function to fetch WHO health system ranking data
def get_who_data():
    global who_df
    
    # URL of the Wikipedia page
    url = "https://en.wikipedia.org/wiki/World_Health_Organization_ranking_of_health_systems_in_2000?wprov=srpw1_0"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing the data (in this case, it's the only table on the page)
        table = soup.find('table', class_='wikitable')

        # Convert the HTML table to a DataFrame using pandas
        who_df = pd.read_html(str(table))[0]
        return True, "WHO health system ranking data has been fetched successfully."
    else:
        return False, "Failed to retrieve WHO health system ranking data from the URL."

# Function to fetch world population data
def get_population_data():
    global population_df
    
    # URL of the Worldometer page
    url = "https://www.worldometers.info/world-population/population-by-country/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing the data
        table = soup.find('table', id='example2')

        # Convert the HTML table to a DataFrame using pandas
        population_df = pd.read_html(str(table))[0]

        # Rename the 'Country (or dependency)' column to 'Country'
        population_df.rename(columns={'Country (or dependency)': 'Country'}, inplace=True)

        return True, "World population data has been fetched successfully."
    else:
        return False, "Failed to retrieve world population data from the URL."


# Function to fetch quality of life ranking data
def get_quality_of_life_data():
    global quality_of_life_df
    
    # URL of the Numbeo page
    url = "https://www.numbeo.com/quality-of-life/rankings_by_country.jsp"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table containing the data
        table = soup.find('table', class_='stripe row-border order-column compact')

        # Convert the HTML table to a DataFrame using pandas
        quality_of_life_df = pd.read_html(str(table))[0]
        return True, "Quality of life ranking data has been fetched successfully."
    else:
        return False, "Failed to retrieve quality of life ranking data from the URL."

# Function to save datasets to CSV files
def save_datasets():
    global covid_df, who_df, population_df, quality_of_life_df
    
    # Define a dictionary containing dataset names and their respective DataFrames
    datasets = {
        "COVID-19 Data": covid_df,
        "WHO Health System Ranking Data": who_df,
        "World Population Data": population_df,
        "Quality of Life Ranking Data": quality_of_life_df
    }
    
    # Loop through each dataset and save it to a CSV file
    for name, df in datasets.items():
        if df is not None:
            # Open a file dialog to choose the save location
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")), initialfile=f"{name}.csv")
            if file_path:
                df.to_csv(file_path, index=False)
                return True, f"{name} has been saved to {file_path}"
        else:
            return False, f"{name} is not available. Please fetch the data first."
