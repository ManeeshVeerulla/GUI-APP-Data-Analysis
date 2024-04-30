from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd 
df=pd.read_csv("merged_dataset.csv")

def run_regression(df):
    # Assuming 'target' is the target variable column name
    X = df.drop('target', axis=1)  # Features
    y = df['target']  # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create linear regression object
    model = LinearRegression()

    # Train the model using the training sets
    model.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Return evaluation metrics or any relevant information
    return "Regression model prediction completed."

def run_random_forest(df):
    # Assuming 'target' is the target variable column name
    X = df.drop('target', axis=1)  # Features
    y = df['target']  # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create random forest classifier object
    model = RandomForestClassifier(n_estimators=100)

    # Train the model using the training sets
    model.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Return evaluation metrics or any relevant information
    return f"Random Forest Classifier model prediction completed. Accuracy: {accuracy}"
