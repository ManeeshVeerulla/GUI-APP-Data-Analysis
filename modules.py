# modules.py
# Import necessary libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox, filedialog, ttk
import Data
import eda
import tkinter as tk
import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
