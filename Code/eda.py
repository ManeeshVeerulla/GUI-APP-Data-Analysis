import tkinter as tk
from tkinter import messagebox, filedialog
import Data
import pandas as pd
import modules
# Function to fetch data when the corresponding button is clicked
def fetch_data(fetch_func, success_msg):
    success, msg = fetch_func()
    if success:
        messagebox.showinfo("Success", success_msg)
    else:
        messagebox.showerror("Error", msg)

# Function to save datasets to CSV files
def save_datasets():
    success, msg = Data.save_datasets()
    if success:
        messagebox.showinfo("Success", msg)
    else:
        messagebox.showerror("Error", msg)

# Function to perform exploratory data analysis (EDA)
def perform_eda(df, eda_func):
    success, result = eda_func(df)
    if success:
        messagebox.showinfo("Exploratory Data Analysis", result)
    else:
        messagebox.showerror("Error", result)

# Function to merge datasets
def merge_datasets():
    # Check if all datasets are available
    if Data.covid_df is not None and Data.who_df is not None and Data.population_df is not None and Data.quality_of_life_df is not None:
        # Merge the datasets
        merged_df = pd.merge(Data.covid_df, Data.who_df, on='Country', how='inner')
        merged_df = pd.merge(merged_df, Data.population_df, on='Country', how='inner')
        merged_df = pd.merge(merged_df, Data.quality_of_life_df, on='Country', how='inner')
        
        # Ask user to choose the save location
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=(("CSV files", "*.csv"), ("All files", "*.*")), initialfile="merged_dataset.csv")
        if file_path:
            success, msg = eda.save_to_csv(merged_df, file_path)
            if success:
                messagebox.showinfo("Success", msg)
            else:
                messagebox.showerror("Error", msg)
    else:
        messagebox.showerror("Error", "One or more datasets are missing. Please fetch all datasets first.")

# Function to check headers of a DataFrame
def check_headers():
    if Data.covid_df is not None:
        headers = Data.covid_df.columns.tolist()
        messagebox.showinfo("Headers", headers)
    else:
        messagebox.showerror("Error", "DataFrame is empty.")

# Function to display summary statistics of a DataFrame
def display_summary():
    if Data.covid_df is not None:
        summary = Data.covid_df.describe().to_string()
        messagebox.showinfo("Summary Statistics", summary)
    else:
        messagebox.showerror("Error", "DataFrame is empty.")

# Function to display information about a DataFrame
def display_info():
    if Data.covid_df is not None:
        info = Data.covid_df.info()
        messagebox.showinfo("DataFrame Info", info)
    else:
        messagebox.showerror("Error", "DataFrame is empty.")

# Function to display shape of a DataFrame
def display_shape():
    if Data.covid_df is not None:
        shape = Data.covid_df.shape
        messagebox.showinfo("DataFrame Shape", shape)
    else:
        messagebox.showerror("Error", "DataFrame is empty.")

# Function to display column names of a DataFrame
def display_columns():
    if Data.covid_df is not None:
        columns = Data.covid_df.columns.tolist()
        messagebox.showinfo("DataFrame Columns", columns)
    else:
        messagebox.showerror("Error", "DataFrame is empty.")

# Create the main window
root = tk.Tk()
root.title("Intelligent Application")

# Create a frame to contain the buttons
button_frame = tk.Frame(root)
button_frame.grid(row=0, column=0, sticky="ew")

# Create the "GET DATA" buttons
get_covid_button = tk.Button(button_frame, text="GET COVID-19 DATA", command=lambda: fetch_data(Data.get_covid_data, "COVID-19 data has been fetched successfully."), relief=tk.RAISED, padx=10, pady=5, anchor="w")
get_who_button = tk.Button(button_frame, text="GET WHO DATA", command=lambda: fetch_data(Data.get_who_data, "WHO health system ranking data has been fetched successfully."), relief=tk.RAISED, padx=10, pady=5, anchor="w")
get_population_button = tk.Button(button_frame, text="GET POPULATION DATA", command=lambda: fetch_data(Data.get_population_data, "World population data has been fetched successfully."), relief=tk.RAISED, padx=10, pady=5, anchor="w")
get_quality_of_life_button = tk.Button(button_frame, text="GET QUALITY OF LIFE DATA", command=lambda: fetch_data(Data.get_quality_of_life_data, "Quality of life ranking data has been fetched successfully."), relief=tk.RAISED, padx=10, pady=5, anchor="w")

# Create the "SAVE DATASETS" button
save_datasets_button = tk.Button(root, text="SAVE DATASETS", command=save_datasets, relief=tk.RAISED, padx=10, pady=5, anchor="w")

# Create the "EDA" button
eda_button = tk.Button(root, text="Perform EDA", command=lambda: perform_eda(Data.covid_df, check_headers), relief=tk.RAISED, padx=10, pady=5, anchor="w")

# Create the "MERGE DATASETS" button
merge_datasets_button = tk.Button(root, text="Merge Datasets", command=merge_datasets, relief=tk.RAISED, padx=10, pady=5, anchor="w")

# Create the buttons for displaying DataFrame information
check_headers_button = tk.Button(root, text="Check Headers", command=check_headers)
display_summary_button = tk.Button(root, text="Display Summary", command=display_summary)
display_info_button = tk.Button(root, text="Display Info", command=display_info)
display_shape_button = tk.Button(root, text="Display Shape", command=display_shape)
display_columns_button = tk.Button(root, text="Display Columns", command=display_columns)

# Arrange the widgets in the window
get_covid_button.grid(row=0, column=0, sticky="ew")
get_who_button.grid(row=0, column=1, sticky="ew")
get_population_button.grid(row=0, column=2, sticky="ew")
get_quality_of_life_button.grid(row=0, column=3, sticky="ew")
save_datasets_button.grid(row=1, column=0, columnspan=4, sticky="ew")
eda_button.grid(row=2, column=0, columnspan=4, sticky="ew")
merge_datasets_button.grid(row=3, column=0, columnspan=4, sticky="ew")
check_headers_button.grid(row=4, column=0, sticky="ew")
display_summary_button.grid(row=4, column=1, sticky="ew")
display_info_button.grid(row=4, column=2, sticky="ew")
display_shape_button.grid(row=4, column=3, sticky="ew")
display_columns_button.grid(row=4, column=4, sticky="ew")

# Run the main event loop
root.mainloop()