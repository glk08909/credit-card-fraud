import pickle
import numpy as np

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

def predict(features: dict):
    values = np.array([list(features.values())]).reshape(1, -1)
    values_scaled = scaler.transform(values)
    pred = model.predict(values_scaled)
    return int(pred[0])