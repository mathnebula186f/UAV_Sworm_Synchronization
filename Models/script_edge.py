import pandas as pd
import numpy as np
from keras.models import load_model

model_choice = input("Choose a model to use (ANN or CNN): ").strip().upper()

if model_choice == "ANN":
    model_path = "ANN\\model.h5"
    input_dataset_path = "ANN\\dataset-1.csv"
    output_dataset_path = "ANN\\output_ann.csv"
elif model_choice == "CNN":
    model_path = "CNN\\model.h5"
    input_dataset_path = "CNN\\dataset-1.csv"
    output_dataset_path = "CNN\\output_cnn.csv"
else:
    raise ValueError("Invalid model choice. Please choose 'ANN' or 'CNN'.")

model = load_model(model_path)
data = pd.read_csv(input_dataset_path)
X = data.values
X = X[:, :52]
predictions = model.predict(X)
output_data = pd.DataFrame(predictions)
output_data.to_csv(output_dataset_path, index=False, header=False)
