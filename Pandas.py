import pandas as pd
import matplotlib.pyplot as plt  # will help create graphs

#load the dataset
df = pd.read_csv('/Users/sameeyaali/Downloads/US-2016-primary.csv', delimiter=";")

print(df.columns)  # names of all the columns

#chosen candidate
chosen_candidate = "Carly Fiorina"

#filter the data for that candidate
candidate_df = df[df["candidate"] == chosen_candidate]
print(candidate_df)

#change votes to a number format
candidate_df["votes"] = pd.to_numeric(candidate_df["votes"], errors="coerce")
candidate_df = candidate_df.dropna(subset=["votes"])

#plot the histogram
plt.hist(candidate_df["votes"], bins=15)
plt.xlabel("Number of Votes")
plt.ylabel("Number of States")
plt.title(f"Number of Votes for {chosen_candidate} by each State (2016)")
plt.show()

