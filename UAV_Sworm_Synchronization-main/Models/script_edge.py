import pandas as pd
import numpy as np
from keras.models import load_model

model_path_ANN = "ANN\model.h5"  
model_path_CNN = "ANN\model.h5"  
model_ANN = load_model(model_path_ANN)
model_CNN = load_model(model_path_CNN)

input_dataset_path_ANN = "ANN\dataset-1.csv"
input_dataset_path_CNN = "CNN\dataset-1.csv"

data_ANN = pd.read_csv(input_dataset_path_ANN)
data_CNN = pd.read_csv(input_dataset_path_CNN)

X_ANN = data_ANN.values
X_ANN = X_ANN[:, :52]

X_CNN = data_CNN.values
X_CNN = X_CNN[:, :52]

predictions_ANN = model_ANN.predict(X_ANN)
predictions_CNN = model_CNN.predict(X_CNN)

output_data_ANN = pd.DataFrame(predictions_ANN)  
output_data_CNN = pd.DataFrame(predictions_CNN)

output_dataset_path1 = "ANN\output_ann.csv"
output_dataset_path2 = "CNN\output_cnn.csv"

output_data_ANN.to_csv(output_dataset_path1, index=False , header = False)  
output_data_CNN.to_csv(output_dataset_path2, index=False , header = False)

