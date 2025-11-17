#plot closing price vs date for Tesla ( 1 year)

#import relevant libraries that are needed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#create a dataframe from the Tesla Inc csv file
df = pd.read_csv('TESLA INC (08-27-2024 _ 11-17-2025).csv')
print(df.head())