from fastapi import FastAPI
from mangum import Mangum
import joblib
import numpy as np

app = FastAPI()

# loading the saved model
model = joblib.load("linear_regression_model.pkl")

@app.get("/")
def home():
    try:
        return {
            "message": "Welcome to the Salary Prediction API! Use the /predict endpoint with a 'years_of_experience' query parameter to get a salary prediction."
        }
    except Exception as e:
        return {
            "message": f"An error occured: {str(e)}"
        }
    
@app.get("/predict/{years_of_experience}")
def predict(years_of_experience: float):
    try:
        input_data = np.array([[years_of_experience]])
        predicted_salary = float(model.predict(input_data)[0])
        return {
            "message": "Prediction successfully",
            "data": {
                "years_of-experience": years_of_experience,
                "predicted_salary": predicted_salary
            }
        }
    
    except Exception as e:
        return {
            "message": f"An error occured during prediction: {str(e)}"
        }
    
# vercel serverless handler
handler = Mangum(app)