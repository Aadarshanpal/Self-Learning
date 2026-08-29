import pandas as pd


data = [1, 2 , 3, 5, 8]
ind = pd.Series(["i","ii","iii","iv","v"])
series = pd.Series(data, index=ind)                         # Series is like a column like a 1D 

print(series.loc["iii"])


print(series[series >= 3])


