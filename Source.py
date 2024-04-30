import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score

# Load the merged dataset
merged_df = pd.read_csv("merged_dataset.csv")

# Drop rows with missing values for the target variable
merged_df.dropna(subset=['Total confirmed deaths due to COVID-19'], inplace=True)

# Feature selection for Linear Regression
features_lr = ['Health expenditure per capita in international dollars', 'Population  (2023)', 
               'Quality of Life Index', 'Purchasing Power Index', 'Safety Index', 
               'Health Care Index', 'Cost of Living Index']

# Split data into features and target variable
X_lr = merged_df[features_lr]
y_lr = merged_df['Total confirmed deaths due to COVID-19']

# Split data into training and testing sets
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

# Train Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train_lr, y_train_lr)

# Make predictions
y_pred_lr = lr_model.predict(X_test_lr)

# Calculate RMSE
rmse_lr = mean_squared_error(y_test_lr, y_pred_lr, squared=False)
print("Linear Regression RMSE:", rmse_lr)

# Feature selection for Random Forest Classifier
features_rf = ['Health expenditure per capita in international dollars', 'Population  (2023)', 
               'Quality of Life Index', 'Purchasing Power Index', 'Safety Index', 
               'Health Care Index', 'Cost of Living Index', 'Case fatality rate of COVID-19 (%)']

# Classify countries into high or low case fatality rate categories
merged_df['Case fatality rate category'] = merged_df['Case fatality rate of COVID-19 (%)'].apply(lambda x: 'High' if x > 3 else 'Low')

# Split data into features and target variable
X_rf = merged_df[features_rf]
y_rf = merged_df['Case fatality rate category']

# Split data into training and testing sets
X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X_rf, y_rf, test_size=0.2, random_state=42)

# Train Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train_rf, y_train_rf)

# Make predictions
y_pred_rf = rf_model.predict(X_test_rf)

# Calculate accuracy
accuracy_rf = accuracy_score(y_test_rf, y_pred_rf)
print("Random Forest Classifier Accuracy:", accuracy_rf)
