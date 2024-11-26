from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from keras.models import load_model

# Load the trained model
ann_model = load_model("ANN/model.h5")
cnn_model = load_model("CNN/model.h5")

# Initialize FastAPI app
app = FastAPI()

# Define request schema
class InputData(BaseModel):
    features: list[float]  # Expecting a list of 52 float numbers

# Health check endpoint
@app.get("/")
def read_root():
    return {"message": "Model API is running!"}

# ANN Prediction endpoint
@app.post("/predict_using_ann")
def predict(input_data: InputData):
    # Validate input size
    if len(input_data.features) != 52:
        return {"error": "Input must have exactly 52 features."}
    
    # Convert input to numpy array and reshape for model
    input_array = np.array(input_data.features).reshape(1, -1)
    
    # Make prediction
    prediction = ann_model.predict(input_array)
    
    # Convert prediction to a list for JSON serialization
    prediction_list = prediction[0].tolist()
    return {"prediction": prediction_list}

# CNN Prediction endpoint
@app.post("/predict_using_cnn")
def predict(input_data: InputData):
    # Validate input size
    if len(input_data.features) != 52:
        return {"error": "Input must have exactly 52 features."}
    
    # Convert input to numpy array and reshape for model
    input_array = np.array(input_data.features).reshape(1, 52, 1, 1)
    
    # Make prediction
    prediction = cnn_model.predict(input_array)
    
    # Convert prediction to a list for JSON serialization
    prediction_list = prediction[0].tolist()
    return {"prediction": prediction_list}