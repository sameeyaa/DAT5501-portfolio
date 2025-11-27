
from ucimlrepo import fetch_ucirepo 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import pandas as pd

# fetch dataset 
car_evaluation = fetch_ucirepo(id=19) 
  
# data (as pandas dataframes) 
X = car_evaluation.data.features 
y = car_evaluation.data.targets 
  
# metadata 
#print(car_evaluation.metadata) 
  
# variable information 
#print(car_evaluation.variables) 

#create categorical columns
label_encoders = {}
X_encoded = X.copy()

for col in X.columns:
    le = LabelEncoder
    X_encoded[col] = le.fit_transform(X[col])
    label_encoders[col] = le





