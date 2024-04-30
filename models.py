import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CovidAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COVID-19 Analysis Tool")
        self.root.configure(background="#f0f0f0")

        # Load the merged dataset
        self.merged_df = pd.read_csv("merged_dataset.csv")

        # Drop rows with missing values for the target variable
        self.merged_df.dropna(subset=['Total confirmed deaths due to COVID-19'], inplace=True)

        # Create and layout widgets
        self.create_widgets()

    def create_widgets(self):
        # Linear Regression Frame
        lr_frame = ttk.LabelFrame(self.root, text="Linear Regression", padding=20)
        lr_frame.grid(row=0, column=0, padx=20, pady=20)

        # Button to calculate Linear Regression
        lr_button = ttk.Button(lr_frame, text="Calculate Linear Regression", command=self.calculate_lr)
        lr_button.grid(row=0, column=0, padx=10, pady=10)

        # Linear Regression Result Label
        self.lr_result_label = ttk.Label(lr_frame, text="")
        self.lr_result_label.grid(row=1, column=0, padx=10, pady=10)

        # Random Forest Classifier Frame
        rf_frame = ttk.LabelFrame(self.root, text="Random Forest Classifier", padding=20)
        rf_frame.grid(row=0, column=1, padx=20, pady=20)

        # Button to calculate Random Forest Classifier
        rf_button = ttk.Button(rf_frame, text="Calculate Random Forest Classifier", command=self.calculate_rf)
        rf_button.grid(row=0, column=0, padx=10, pady=10)

        # Random Forest Classifier Result Label
        self.rf_result_label = ttk.Label(rf_frame, text="")
        self.rf_result_label.grid(row=1, column=0, padx=10, pady=10)

        # Create a canvas for plotting
        self.canvas = tk.Canvas(self.root, width=800, height=400, background="white")
        self.canvas.grid(row=1, columnspan=2, padx=20, pady=20)

    def calculate_lr(self):
        # Feature selection for Linear Regression
        features_lr = ['Health expenditure per capita in international dollars', 'Population  (2023)',
                       'Quality of Life Index', 'Purchasing Power Index', 'Safety Index',
                       'Health Care Index', 'Cost of Living Index']

        # Split data into features and target variable
        X_lr = self.merged_df[features_lr]
        y_lr = self.merged_df['Total confirmed deaths due to COVID-19']

        # Split data into training and testing sets
        X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

        # Train Linear Regression model
        lr_model = LinearRegression()
        lr_model.fit(X_train_lr, y_train_lr)

        # Make predictions
        y_pred_lr = lr_model.predict(X_test_lr)

        # Calculate RMSE
        rmse_lr = mean_squared_error(y_test_lr, y_pred_lr, squared=False)
        self.lr_result_label.config(text=f"Linear Regression RMSE: {rmse_lr:.2f}")

        # Plotting
        self.plot_evaluation(y_test_lr, y_pred_lr, "Linear Regression Evaluation")

    def calculate_rf(self):
        # Feature selection for Random Forest Classifier
        features_rf = ['Health expenditure per capita in international dollars', 'Population  (2023)',
                       'Quality of Life Index', 'Purchasing Power Index', 'Safety Index',
                       'Health Care Index', 'Cost of Living Index', 'Case fatality rate of COVID-19 (%)']

        # Classify countries into high or low case fatality rate categories
        self.merged_df['Case fatality rate category'] = self.merged_df['Case fatality rate of COVID-19 (%)'].apply(
            lambda x: 'High' if x > 3 else 'Low')

        # Split data into features and target variable
        X_rf = self.merged_df[features_rf]
        y_rf = self.merged_df['Case fatality rate category']

        # Split data into training and testing sets
        X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X_rf, y_rf, test_size=0.2, random_state=42)

        # Train Random Forest Classifier
        rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_model.fit(X_train_rf, y_train_rf)

        # Make predictions
        y_pred_rf = rf_model.predict(X_test_rf)

        # Calculate accuracy
        accuracy_rf = accuracy_score(y_test_rf, y_pred_rf)
        self.rf_result_label.config(text=f"Random Forest Classifier Accuracy: {accuracy_rf:.2f}")

        # Plotting
        self.plot_evaluation(y_test_rf, y_pred_rf, "Random Forest Classifier Evaluation")

    def plot_evaluation(self, true_values, predicted_values, title):
        plt.figure(figsize=(8, 4))
        plt.plot(true_values, label='True Values', color='#007acc')
        plt.plot(predicted_values, label='Predicted Values', color='#ff7f0e')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.title(title)
        plt.legend()
        plt.tight_layout()

        # Convert Matplotlib figure to Tkinter canvas
        self.canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, columnspan=2, padx=20, pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    app = CovidAnalysisApp(root)
    root.mainloop()
