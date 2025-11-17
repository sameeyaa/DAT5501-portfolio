#import modules needed
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import numpy as np

#convert my chosen csv into a dataframe
life_expectancy_df = pd.read_csv("life-expectancy.csv")
print(life_expectancy_df.head())

#getting rid of any columns that are not needed - cleaning data
life_expectancy_df = life_expectancy_df.drop(columns = ['Entity'])

print(life_expectancy_df.columns.tolist())
print(life_expectancy_df.head())

#change column name to a simpler name
life_expectancy_df.rename(columns = {'Period life expectancy at birth' : 'Life expectancy at birth'}, inplace = True)
print(life_expectancy_df.head())

#masking the data for a specific timeframe
mask1 = life_expectancy_df['Year'] >= 1940
mask2 = life_expectancy_df['Year'] <= 2023

first_range = life_expectancy_df[mask1]
range_life_expectancy_df = first_range[mask2]
#print(range_life_expectancy_df.head())

#set the variables for the polynomial graph
# x axis = Year    y axis = Life expectancy at birth
#mask and choose one entity 'Cayman Islands'
mask3 = range_life_expectancy_df['Code'] == 'CYM'
cym_life_expectancy = range_life_expectancy_df[mask3]
print(cym_life_expectancy.head())
print(range_life_expectancy_df.head())
years = cym_life_expectancy['Year']
#years_centered = years - years.mean()
life_expectancy = range_life_expectancy_df['Life expectancy at birth']

xp = np.linspace(1940, 2023 + 10, 300)
degree = 10

def poly():
    for i in range(1, degree):
        coefficients = np.polyfit(years, cym_life_expectancy['Life expectancy at birth'], i)
        p = np.poly1d(coefficients)
        plt.figure(figsize=(10,6))
        plt.scatter(years, cym_life_expectancy['Life expectancy at birth'], label='Data points', color='blue')
        plt.plot(xp, p(xp), label= f'order {i}', linewidth=2)
        plt.show()

def polyall():
    plt.figure(figsize=(12, 7))
    plt.scatter(years, cym_life_expectancy['Life expectancy at birth'], label='data points')
    for i in range(1, degree):
        coefficients = np.polyfit(years, cym_life_expectancy['Life expectancy at birth'], i)
        p = np.poly1d(coefficients)
        plt.plot(xp, p(xp), label=f'order {i}', linewidth=2)

    plt.show()


polyall()
