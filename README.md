# Loan Default Risk Prediction API

An end-to-end Machine Learning project that predicts whether a customer is likely to repay a loan.

## Live Demo

### Live API
https://loan-default-risk-prediction-api-jdpr.onrender.com

### Swagger Documentation
https://loan-default-risk-prediction-api-jdpr.onrender.com/docs

You can test the API directly through the Swagger UI without installing any software locally.

## Tech Stack

- Python
- Pandas
- Scikit-Learn
- Random Forest
- FastAPI
- Uvicorn

## Features

- Loan repayment prediction
- Probability scoring
- REST API with FastAPI
- Interactive Swagger documentation

## Project Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Data Scaling
5. Model Training
6. Model Evaluation
7. Model Deployment using FastAPI
   
## Screenshots

### Correlation Heatmap

<img width="1326" height="1040" alt="image" src="https://github.com/user-attachments/assets/fd16db72-8a8d-4560-8b18-92ba7a77487b" />


---

### Random Forest Model Evaluation

<img width="561" height="342" alt="image" src="https://github.com/user-attachments/assets/0c126c7c-b92b-494b-8423-a29066219991" />


---

### FastAPI Swagger Documentation

<img width="1880" height="792" alt="image" src="https://github.com/user-attachments/assets/001044b6-c288-4864-8f4a-6e7bd356f1d3" />


---

### Prediction Response

<img width="485" height="153" alt="image" src="https://github.com/user-attachments/assets/b10bcd43-93cc-4516-a5e4-02a270b29dc4" />



## Run Locally

```bash
pip install -r requirements.txt
python -m uvicorn app:app --reload --port 8001
```

## API Endpoints

### Home

```http
GET /
```

### Prediction

```http
POST /predict
```

Example Response:

```json
{
  "risk_level": "Likely To Repay",
  "prediction": 1,
  "repayment_probability": 0.95
}
```

## Model Used

Random Forest Classifier

## Key Achievements

- Built an end-to-end machine learning pipeline.
- Performed EDA and feature engineering.
- Trained and evaluated multiple classification models.
- Selected Random Forest as the final model.
- Deployed the model using FastAPI.
- Implemented a real-time prediction endpoint.

## Author

Sanjit Sitaula
