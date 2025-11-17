#plot closing price vs date for Tesla ( 1 year)

#import relevant libraries that are needed
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import datetime

#create a dataframe from the Tesla Inc csv file
df = pd.read_csv('TESLA INC (08-27-2024 _ 11-17-2025).csv')
print(df.head())

#ensure dates are in datetime format
df['Date'] = pd.to_datetime(df['Date'])
print(df.head())

#seperate each month in the year into a data frame
#focusing on January 2025 - November 2025 as there is no December 2025 data
january_df = (df['Date'] >= '2025-01-01') & (df['Date'] <= '2025-01-31')
january_df = df.loc[january_df]
january_df['day'] = january_df['Date'].dt.day


