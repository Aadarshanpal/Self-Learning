# DataCleaning is the process of removing/reducing all the unnecessary datas

import pandas as pd

df = pd.read_csv("Pandas/data.csv")

# 1. Dropping columns
df = df.drop(columns=["Sp. Atk","Sp. Def","Speed"])


# 2. Handling missing data
# df = df.dropna(subset=["Type 2"])
# df = df.fillna({"Type 2": "None"})


# 3. Fixing inconsistent data
df["Type 1"] = df["Type 1"].replace({"Dragon" : "DRAGUN"})


# 4. Standardize text
df["Name"] = df["Name"].str.lower()


# 5. Fix data types
# df["Column"] = df["Column"].astype(Type)


# 6. Remove duplicate values
df = df.drop_duplicates()


print(df)