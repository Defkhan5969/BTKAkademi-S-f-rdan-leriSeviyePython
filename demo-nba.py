import pandas as pd
import numpy as np

df = pd.read_csv("BTK Kurs/nba.csv")

result = df

result = df.head(10)
result = len(df.index)

result = df["Salary"].mean()
result = df["Salary"].max()
result = df[df["Salary"].max() == df["Salary"]]["Name"]
result = df[(df["Age"]>=20) & (df["Age"]<=25)][["Name","Team"]]
result = df[df["Name"]=="John Holland"]["Team"]

result = df.groupby("Team").mean()["Salary"]
result = len(df.groupby("Team"))
result = df["Team"].nunique()

result = df["Team"].value_counts()

df = df.dropna()
result = df[df["Name"].str.contains("and")]

def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find)]
print(result)