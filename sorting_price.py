import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_csv('/Users/sameeyaali/Downloads/NVIDIA CORPORATION (08-05-2024 _ 11-07-2025).csv')
print(df)

df['Close'] = df['Close'].astype(str).str.replace(',' , '').astype(float)

prices = df['Close'].values
change_in_p = np.diff(prices)

n_values = np.arange(7, len(change_in_p) + 1)
T = []

for n in n_values:
    sample = change_in_p[:n]
    start = time.perf_counter()
    sorted(sample)
    end = time.perf_counter()
    T.append (end - start)

    nlogn = n_values * np.log(n_values)
    nlogn_scaled = nlog / nlogn.max * max(T)

    #plot the graph
    plt.figure(figsize = (10, 6))
    plt.plot(n_values, T, label='Measured sort time')
    plt.plot(n_values, nlogn_scaled, '--', label = 'n log n scaled')
    plt.xlabel('n (number of daily changes)')
    plt.ylabel('Time to sort(seconds)')
    plt.title('Sorting Time vs Daily Price changes')
    plt.legend()
    plt.show
