import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_csv('/Users/sameeyaali/Downloads/NVIDIA CORPORATION (08-05-2024 _ 11-07-2025).csv')
print(df) #display the csv file to see data layout
df.head

#convert the dates to a datetime layout for pandas interpretation
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date') #make the dates ascending in order
#convert 'Close' column to number format to enable line plotting
df['Close'] = df['Close'].astype(str).str.replace(',', '').astype(float)

#calculate the change in price everyday for 318 days
prices = df['Close'].values
change_in_P = np.diff(prices)

#segment the data into portions to analyse sort time as n increases
n_values = np.arange(8, len(change_in_P) + 1)

#Initially have T blank so that it starts from no times recorded
T = []

for n in n_values:
    sample = change_in_P [:n] 
    start = time.perf_counter() 
    sorted(sample)
    end = time.perf_counter()
    T.append(end - start)

#plot an expected nlogn curve to compare fairly
nlogn = n_values * np.log(n_values)
curve = nlogn/ nlogn.max() * max(T) #will match measured range

#plotting the graph


