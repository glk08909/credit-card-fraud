# credit-card-fraud

**This project implements a full machine learning pipeline to detect fraudulent credit card transactions. It covers everything from data exploration and model training to API deployment and cloud hosting. The goal is to build a production‑ready fraud detection service capable of real‑time inference.**
---
Project Overview
Credit card fraud is a major financial threat, and early detection is essential.  
This project uses the popular Credit Card Fraud Detection dataset (Kaggle) containing anonymized PCA‑transformed features (V1–V28) along with Time and Amount.
The workflow includes:
• Exploratory Data Analysis (EDA)
• Model training and evaluation
• Hyperparameter tuning
• Exported training and prediction scripts
• Flask API for real‑time predictions
• Docker containerization
• Cloud deployment (Render)

🧠 Features
• End‑to‑end ML workflow
• Multiple models tested (Logistic Regression, Decision Tree, Random Forest, XGBoost)
• Best model exported as model.pkl
• Scaler exported as scaler.pkl
• Reproducible training (train.py) and inference (predict.py) scripts
• REST API for predictions
• Dockerized application
• Cloud‑hosted API endpoint

# Project Structure
credit-card-fraud/
│
├── data/                 # Dataset (ignored in Git)
├── models/               # Saved model and scaler
├── notebooks/            # EDA and experimentation
├── src/
│   ├── train.py          # Training script
│   ├── predict.py        # Local prediction script
│   └── app.py            # Flask API
│
├── Dockerfile            # Container configuration
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
└── .gitignore

# Model Training

Train the model using:
python src/train.py

This script:
• Loads the dataset
• Splits into train/test
• Scales features
• Trains multiple models
• Selects the best one
• Saves model.pkl and scaler.pkl

# Local Prediction
Run predictions locally:
python src/predict.py

This loads the saved model and scaler and prints the prediction for a sample input.

# API Usage (Flask)
Start the API:
python src/app.py

The API exposes a single endpoint:
POST /predict

# Example Request
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"V1": -1.359807, "V2": -0.072781, "V3": 2.536346, "V4": 1.378155, "V5": -0.338321, "V6": 0.462388, "V7": 0.239599, "V8": 0.098698, "V9": 0.363787, "V10": 0.090794, "V11": -0.551600, "V12": -0.617801, "V13": -0.991390, "V14": -0.311169, "V15": 1.468177, "V16": -0.470400, "V17": 0.207971, "V18": 0.025791, "V19": 0.403993, "V20": 0.251412, "V21": -0.018307, "V22": 0.277838, "V23": -0.110474, "V24": 0.066928, "V25": 0.128539, "V26": -0.189115, "V27": 0.133558, "V28": -0.021053, "Amount": 149.62, "Time": 0}' \
  http://localhost:9696/predict

# Example Response

{
  "fraud_prediction": 0
}

# Docker Deployment
Build the Docker image:

docker build -t fraud-detector .
docker run -p 9696:9696 fraud-detector

The API becomes available at:
http://localhost:9696/predict

# Cloud Deployment (Render)
The application is deployed using Render’s Docker Web Service.
Steps:
1. Push project to GitHub
2. Create a new Web Service on Render
3. Select Docker as the environment
4. Set port to 9696
5. Deploy
Render builds the Docker image and hosts the API.

# Live Endpoint
https://<your-service-name>.onrender.com/predict

# Dataset
The dataset is not included in this repository due to GitHub’s file size limits.  
You can download it from Kaggle:
Credit Card Fraud Detection Dataset  
https://www.kaggle.com/mlg-ulb/creditcardfraud
Place it in:
data/creditcard.csv

# Conclusion
This project demonstrates a complete machine learning workflow, from data exploration to cloud deployment. It showcases best practices in reproducibility, API design, containerization, and real‑world ML service development.
