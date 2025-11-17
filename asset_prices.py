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

#plot whole year closing price vs date
plt.figure (figsize = (16,8))
plt.plot(df['Date'],
         df['Close'],
         linewidth = 2,
         label = 'Closing Price')

plt.xlabel('Date', fontsize = 12)
plt.ylabel('Closing Price ($)', fontsize = 12)
plt.title ("Tesla Inc 2025 Closing Price vs Date", fontsize = 16)
plt.legend()
plt.tight_layout
plt.show()






