import pandas as pd
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the dataset
df = pd.read_csv("merged_dataset.csv")

# Create a Tkinter window
root = tk.Tk()
root.title("COVID-19 Data Visualization")
root.configure(bg="#f0f0f0")

# Function to plot the data
def plot_data():
    # Create a figure and axes for subplots
    fig = Figure(figsize=(12, 10))
    axs = fig.subplots(3, 2)

    # Time series plot of daily new confirmed cases and deaths
    axs[0, 0].plot(df['Year'], df['Daily new confirmed cases of COVID-19'], label='Daily New Cases', color='blue')
    axs[0, 0].plot(df['Year'], df['Daily new confirmed deaths due to COVID-19'], label='Daily New Deaths', color='red')
    axs[0, 0].set_xlabel('Year', fontsize=12)
    axs[0, 0].set_ylabel('Count', fontsize=12)
    axs[0, 0].set_title('Daily New Confirmed Cases and Deaths of COVID-19 Over Time', fontsize=14)
    axs[0, 0].legend()
    axs[0, 0].grid(True)

    # Time series plot of total confirmed cases and deaths
    axs[0, 1].plot(df['Year'], df['Total confirmed cases of COVID-19'], label='Total Cases', color='blue')
    axs[0, 1].plot(df['Year'], df['Total confirmed deaths due to COVID-19'], label='Total Deaths', color='red')
    axs[0, 1].set_xlabel('Year', fontsize=12)
    axs[0, 1].set_ylabel('Count', fontsize=12)
    axs[0, 1].set_title('Total Confirmed Cases and Deaths of COVID-19 Over Time', fontsize=14)
    axs[0, 1].legend()
    axs[0, 1].grid(True)

    # Comparison plot of daily new confirmed cases across different countries
    axs[1, 0].set_title('Comparison of Daily New Confirmed Cases of COVID-19 Across Countries', fontsize=14)
    for country in ['USA', 'India', 'Brazil', 'Russia', 'France']:
        country_data = df[df['Country'] == country]
        axs[1, 0].plot(country_data['Year'], country_data['Daily new confirmed cases of COVID-19'], label=country)
    axs[1, 0].set_xlabel('Year', fontsize=12)
    axs[1, 0].set_ylabel('Daily New Confirmed Cases', fontsize=12)
    axs[1, 0].legend()
    axs[1, 0].grid(True)

    # Comparison plot of total confirmed cases across different countries
    axs[1, 1].set_title('Comparison of Total Confirmed Cases of COVID-19 Across Countries', fontsize=14)
    for country in ['USA', 'India', 'Brazil', 'Russia', 'France']:
        country_data = df[df['Country'] == country]
        axs[1, 1].plot(country_data['Year'], country_data['Total confirmed cases of COVID-19'], label=country)
    axs[1, 1].set_xlabel('Year', fontsize=12)
    axs[1, 1].set_ylabel('Total Confirmed Cases', fontsize=12)
    axs[1, 1].legend()
    axs[1, 1].grid(True)

    # Scatter plot to visualize the relationship between Quality of Life Index and Health Care Index
    axs[2, 0].scatter(df['Quality of Life Index'], df['Health Care Index'], alpha=0.5, color='green')
    axs[2, 0].set_xlabel('Quality of Life Index', fontsize=12)
    axs[2, 0].set_ylabel('Health Care Index', fontsize=12)
    axs[2, 0].set_title('Relationship between Quality of Life Index and Health Care Index', fontsize=14)
    axs[2, 0].grid(True)

    # Histogram of Population Density
    axs[2, 1].hist(df['Density  (P/Km²)'], bins=20, color='skyblue', edgecolor='black')
    axs[2, 1].set_xlabel('Population Density (P/Km²)', fontsize=12)
    axs[2, 1].set_ylabel('Frequency', fontsize=12)
    axs[2, 1].set_title('Histogram of Population Density', fontsize=14)
    axs[2, 1].grid(True)

    # Adjust layout to prevent overlap
    fig.tight_layout()

    # Convert the Matplotlib figure to Tkinter canvas
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

# # Button to plot the data
plot_button = tk.Button(root, text="Plot Data", command=plot_data, bg='#4CAF50', fg='white', font=('Arial', 14, 'bold'))
plot_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
