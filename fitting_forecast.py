#import modules needed
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

#convert my chosen csv into a dataframe
life_expectancy_df = pd.read_csv("life-expectancy.csv")
print(life_expectancy_df.head())

#getting rid of any columns that are not needed - cleaning data
life_expectancy_df = life_expectancy_df.drop(columns = ['Entity' , 'Code' ])

print(life_expectancy_df.columns.tolist())
print(life_expectancy_df.head())

#change column name to a simpler name
life_expectancy_df.rename(columns = {'Period life expectancy at birth' : 'Life expectancy at birth'}, inplace = True)
print(life_expectancy_df.head())

#masking the data for a specific