import pandas as pd
import matplotlib.pyplot as plt  #will help create graphs

#load the datasets
df = pd.read_csv('/Users/sameeyaali/Downloads/US-2016-primary.csv',delimiter = ";")
print(df)

print(df.columns)  #names of all the columns
#columns: state, state abbreviation, countyr, fips, party, candidate, votes, fraction votes

#choose my candidate I want to analyse from the list
chosen_candidate= "Carly Firiona"

#filter the data to only select data to do with Carly Firiona
candidate_df = df[df["candidate"]== chosen_candidate]

#check if specific data is only presented
print(candidate_df)

#plot the histogram listing the amount of votes from each state
plt.hist(candidate_df["votes"], bins = 15)
plt.xlabel(f"Number of Votes")
plt.ylabel("Number of States")
plt.title(f"Number of Votes for Carly Firiona by each State (2016)")
plt.show()
