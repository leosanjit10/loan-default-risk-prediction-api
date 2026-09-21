# Loan Default Risk Prediction API

An end-to-end Machine Learning project that predicts whether a customer is likely to repay a loan.

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

![reenshots/random_forest_evaluation.png

---

### FastAPI Swagger Documentation

screenshots/swagger_ui.png

---

### Prediction Response

screenshots/prediction_response.png


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

## Note

The trained model file (loan_default_model.pkl) is not included in this repository because it exceeds GitHub's web upload size limit.

To reproduce:

1. Train the model using the notebook.
2. Save the model using joblib.
3. Place the generated model file in the project root directory.

## Author

Sanjit Sitaula
