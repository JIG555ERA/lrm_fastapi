import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# dummy dataset
# Example: predicting salary baed on years of experience
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([30000, 35000, 40000, 45000, 50000])

# model creation
model = LinearRegression()

# model training
model.fit(x,y)

# save model
joblib.dump(model, "linear_regression_model.pkl")
print("Model trained and saved successfully!")