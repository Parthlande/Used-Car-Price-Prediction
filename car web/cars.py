import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
import pickle

file_path = r"C:\web dev\car web\cars.csv" 

data = pd.read_csv(file_path)

print(data.isnull().sum())  # Check for missing values
data = data.dropna() 

X = data[['Year', 'Mileage', 'Fuel Type', 'Transmission']]
y = data['Price']

# Preprocess categorical and numerical features
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), ['Year', 'Mileage']),
        ('cat', OneHotEncoder(), ['Fuel Type', 'Transmission'])
    ]
)


# Create pipeline with preprocessing and model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train the model
model.fit(X_train, y_train)

# Save the trained model
with open('car_price_model.pkl', 'wb') as file:
    pickle.dump(model, file)
    
print("Model trained and saved successfully!")