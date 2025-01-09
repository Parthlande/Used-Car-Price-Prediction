from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates')
CORS(app)

# Load the model
with open('car_price_model.pkl', 'rb') as file:
    pipeline = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.json
        year = data.get('Year')
        mileage = data.get('Mileage')
        fuel_type = data.get('Fuel Type')
        transmission = data.get('Transmission')


        # Validate input (add more robust checks as needed)
        if not year or not mileage or not fuel_type or not transmission:
            return jsonify({'error': 'Please fill in all fields.'}), 400

        # Format data for prediction
        input_data = pd.DataFrame([[year, mileage, fuel_type, transmission]], 
                                 columns=['Year', 'Mileage', 'Fuel Type', 'Transmission'])

        # Predict the price
        predicted_price = pipeline.predict(input_data)[0]

        return jsonify({'predicted_price': round(predicted_price, 2)})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)