import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

df = pd.read_csv('/Users/sameeyaali/Downloads/NVIDIA CORPORATION (08-05-2024 _ 11-07-2025).csv')
print(df)
df.head

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
df['Close'] = df['Close'].astype(str).str.replace(',', '').astype(float)


prices = df['Close'].values
change_in_P = np.diff(prices)

# === Measure sorting time ===
n_values = np.arange(7, len(change_in_P) + 1)
T = []  

