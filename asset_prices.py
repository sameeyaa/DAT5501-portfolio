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
#january
january_df = (df['Date'] >= '2025-01-01') & (df['Date'] <= '2025-01-31')
january_df = df.loc[january_df]
print(january_df)

#february
february_df = (df['Date'] >= '2025-02-01') & (df['Date'] <= '2025-02-28')
february_df = df.loc[february_df]
print(february_df)

#march
march_df = (df['Date'] >= '2025-03-01') & (df['Date'] <= '2025-03-31')
march_df = df.loc[march_df]
print(march_df)

#april
april_df = (df['Date'] >= '2025-04-01') & (df['Date'] <= '2025-04-30')
april_df = df.loc[april_df]
print(april_df)

#may
may_df = (df['Date'] >= '2025-05-01') & (df['Date'] <= '2025-05-31')
may_df = df.loc[may_df]
print(may_df)

#june
june_df = (df['Date'] >= '2025-06-01') & (df['Date'] <= '2025-06-30')
june_df = df.loc[june_df]
print(june_df)





