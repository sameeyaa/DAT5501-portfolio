import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#call the files from my laptop
disorders_path = 'mental disorders data.csv'
working_path = 'working hours.csv'

disorders = pd.read_csv(disorders_path)
working = pd.read_csv(working_path)

#select the data relevant to what I am analysing and the date range I have chosen
filtered = disorders[
    (disorders["cause_name"] == "Mental disorders") &
    (disorders["age_name"] == "All ages") &
    (disorders["location_name"].isin(["China", "United Kingdom"])) &
    (disorders["metric_name"] == "Number") &
    (disorders["year"].between(2011, 2019))
]


pivot_df = filtered.pivot_table(
    index=["year", "location_name"],
    columns="sex_name",
    values="val",
    aggfunc="sum"
).reset_index()

#rename columns for easier layout and easier to write code
working = working.rename(columns={
    "Entity": "location_name",
    "Year": "year",
    "Working hours per worker": "working_hours"
})


working = working[working["location_name"].isin(["China", "United Kingdom"])]
working = working[working["year"].between(2011, 2019)]


merged = pd.merge(
    pivot_df,
    working,
    on=["year", "location_name"],
    how="inner"
)


for country in merged["location_name"].unique():
    subset = merged[merged["location_name"] == country]
    corr_male = subset["Male"].corr(subset["working_hours"])
    corr_female = subset["Female"].corr(subset["working_hours"])
    print(f"{country}:")
    print(f"  Male correlation:   {corr_male:.3f}")
    print(f"  Female correlation: {corr_female:.3f}\n")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

#china
china = merged[merged["location_name"] == "China"]
sns.regplot(data=china, x="working_hours", y="Male", ax=axes[0],
            color="blue", label="Male", scatter_kws={'s': 60})
sns.regplot(data=china, x="working_hours", y="Female", ax=axes[0],
            color="orange", label="Female", scatter_kws={'s': 60})
axes[0].set_title("China: Mental Disorder Deaths vs Working Hours (2011–2019)")
axes[0].set_xlabel("Annual Working Hours per Worker")
axes[0].set_ylabel("Mental Disorder Cases")
axes[0].legend()
axes[0].grid(axis="both", linestyle="--", alpha=0.5)


for _, row in china.iterrows():
    axes[0].text(row["working_hours"], row["Male"], str(row["year"]),
                 fontsize=8, color="blue", ha="right", va="bottom")
    axes[0].text(row["working_hours"], row["Female"], str(row["year"]),
                 fontsize=8, color="orange", ha="left", va="bottom")

# UK
uk = merged[merged["location_name"] == "United Kingdom"]
sns.regplot(data=uk, x="working_hours", y="Male", ax=axes[1],
            color="green", label="Male", scatter_kws={'s': 60})
sns.regplot(data=uk, x="working_hours", y="Female", ax=axes[1],
            color="purple", label="Female", scatter_kws={'s': 60})
axes[1].set_title("UK: Mental Disorder Deaths vs Working Hours (2011–2019)")
axes[1].set_xlabel("Annual Working Hours per Worker")
axes[1].legend()
axes[1].grid(axis="both", linestyle="--", alpha=0.5)


for _, row in uk.iterrows():
    axes[1].text(row["working_hours"], row["Male"], str(row["year"]),
                 fontsize=8, color="green", ha="right", va="bottom")
    axes[1].text(row["working_hours"], row["Female"], str(row["year"]),
                 fontsize=8, color="purple", ha="left", va="bottom")

plt.tight_layout()
plt.show(block=True)

#graphs plotted and correlation coefficient given
