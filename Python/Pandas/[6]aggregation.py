# Aggregate functions reduce the data into one single summary data.


import pandas as pd

df = pd.read_csv("Pandas/data.csv")

# print(df.sum(numeric_only=True))
# print(df.mean(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())
# print(df["HP"].mean())
#gd = df.groupby("Type 1")
#print(gd["HP"].mean())

print((df.groupby("Type 1")["HP"].mean()))