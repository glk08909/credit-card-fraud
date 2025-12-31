# credit-card-fraud

Here’s a polished, professional **Deployment** section you can drop straight into your README. It’s written to match the tone of a real production ML project and aligns perfectly with the ML Zoomcamp rubric.

---

# 🚀 Deployment

This project includes a fully containerized machine learning service for real‑time credit card fraud detection. The model is exposed through a Flask API and deployed to the cloud using Docker.

## 🐳 Docker Setup

The service is packaged in a lightweight Docker image using the included `Dockerfile`.  
To build and run the container locally:

```bash
docker build -t fraud-detector .
docker run -p 9696:9696 fraud-detector
```

Once running, the API is available at:

```
http://localhost:9696/predict
```

## ☁️ Cloud Deployment (Render)

The application is deployed on **Render** as a Docker‑based web service.

### Deployment Steps
1. Push the project to GitHub  
2. Create a new **Web Service** on Render  
3. Select **Docker** as the environment  
4. Use the default `Dockerfile`  
5. Set the exposed port to **9696**  
6. Deploy

Render automatically builds the Docker image and hosts the API.

### Live Endpoint  
Once deployed, the API becomes accessible at a public URL such as:

```
https://<your-service-name>.onrender.com/predict
```

## 🧪 Example Request

Send a POST request with transaction features in JSON format:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"V1": -1.359807, "V2": -0.072781, "V3": 2.536346, "V4": 1.378155, "V5": -0.338321, "V6": 0.462388, "V7": 0.239599, "V8": 0.098698, "V9": 0.363787, "V10": 0.090794, "V11": -0.551600, "V12": -0.617801, "V13": -0.991390, "V14": -0.311169, "V15": 1.468177, "V16": -0.470400, "V17": 0.207971, "V18": 0.025791, "V19": 0.403993, "V20": 0.251412, "V21": -0.018307, "V22": 0.277838, "V23": -0.110474, "V24": 0.066928, "V25": 0.128539, "V26": -0.189115, "V27": 0.133558, "V28": -0.021053, "Amount": 149.62, "Time": 0}' \
  https://<your-service-name>.onrender.com/predict
```

### Example Response

```json
{
  "fraud_prediction": 0
}
```

A value of **1** indicates a fraudulent transaction; **0** indicates a legitimate one.

---

If you'd like, I can help you craft the **final README sections** (Project Overview, Features, How to Run Locally, Model Training, API Usage, etc.) so your repository looks polished end‑to‑end.
