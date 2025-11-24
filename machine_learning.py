#decision tree mini project
#identify a dataset on the UC Irvine Machine Learning Repository
#use a decision tree to classify and predict
#evaluate your model with precision and recall
#use scikit-learn

#my chosen data topic is Car Evaluations

#merge the 3 csv files to make it easier to clean
import pandas as pd

df1 = pd.read_csv('car.c45-names.csv')
df2 = pd.read_csv('car.csv')
df3 = pd.read_csv('car.names.csv')

merged_df = pd.concat([df1, df2, df3], ignore_index=True)
merged_df.to_csv("merged.csv", index = False)
print("Merged csv saved as merged.csv.")