#create a bar chart displaying how many deaths have been caused in China and the UK by mental disorders
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#call the csv file to clean it
file_path = 'mental disorders data.csv'
data = pd.read_csv(file_path)

#clean the data to ensure only data from 2011-2019 is collected
filtered = data[
    (data["cause_name"] == "Mental disorders") &
    (data["age_name"] == "All ages") &
    (data["location_name"].isin(["China", "United Kingdom"])) &
    (data["metric_name"] == "Number") &
    (data["year"].between(2011, 2019))
]


pivot_df = filtered.pivot_table(
    index=["year", "location_name"],
    columns="sex_name",
    values="val",
    aggfunc="sum"
).reset_index()

#seperate the data so that China and UK data are shown on two seperate graphs
china = pivot_df[pivot_df["location_name"] == "China"]
uk = pivot_df[pivot_df["location_name"] == "United Kingdom"]

#set the size of the graphs for plotting
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

bar_width = 0.5
years = np.arange(len(china["year"]))

#China graph
axes[0].bar(years - bar_width/2, china["Male"], width=bar_width, label="Male", color="orange")
axes[0].bar(years + bar_width/2, china["Female"], width=bar_width, label="Female", color="blue")
axes[0].set_title("China: Mental Disorders by Sex (2011–2019)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("Number of Cases (per Thousand)")
axes[0].set_xticks(years)
axes[0].set_xticklabels(china["year"])
axes[0].legend()
axes[0].grid(axis="y", linestyle="--", alpha=0.5)

#UK
years_uk = np.arange(len(uk["year"]))
axes[1].bar(years_uk - bar_width/2, uk["Male"], width=bar_width, label="Male", color="green")
axes[1].bar(years_uk + bar_width/2, uk["Female"], width=bar_width, label="Female", color="purple")
axes[1].set_title("United Kingdom: Mental Disorders by Gender(2011–2019)")
axes[1].set_xlabel("Year")
axes[1].set_xticks(years_uk)
axes[1].set_xticklabels(uk["year"])
axes[1].legend()
axes[1].grid(axis="y", linestyle="--", alpha=0.5)

#print the graph
plt.tight_layout()
plt.show(block=True)

#graphs successfully ran