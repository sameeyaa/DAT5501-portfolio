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

#masking the data for a specific timeframe
mask1 = life_expectancy_df['Year'] >= 1923
mask2 = life_expectancy_df['Year'] <= 2023

first_range = life_expectancy_df[mask1]
range_life_expectancy_df = first_range[mask2]
print(range_life_expectancy_df.head())

#set the variables for the polynomial graph
# x axis = Year    y axis = Life expectancy at birth
years = range_life_expectancy_df['Year']
#years_centered = years - years.mean()
life_expectancy = range_life_expectancy_df['Life expectancy at birth']

