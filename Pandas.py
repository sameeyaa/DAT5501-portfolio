import pandas as pd
import matplotlib.pyplot as plt  #will help create graphs

#load the datasets
df = pd.read_csv('/Users/sameeyaali/Downloads/US-2016-primary.csv',delimiter = ";")
print(df)

print(df.columns)  #names of all the columns
#columns: state, state abbreviation, countyr, fips, party, candidate, votes, fraction votes
