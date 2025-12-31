from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model and scaler
with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert input to array
    values = np.array([list(data.values())]).reshape(1, -1)
    values_scaled = scaler.transform(values)

    pred = model.predict(values_scaled)[0]
    return jsonify({'fraud_prediction': int(pred)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9696)