import pandas as pd

df = pd.read_csv("Pandas\data.csv")

#Prints ABSOLUTELY EVERYTHING
#print(df.to_string())

# print(df[["Name","Type 1"]].to_string())


# While accessing the data we can also set the index to the name for eg so that its easier to search for data

# df = pd.read_csv("data.csv", index_col = "Name")


print(df.loc[13, ["Name", "Type 1", "Type 2"]])