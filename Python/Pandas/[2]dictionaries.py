import pandas as pd

calories = {"Day 1": 1700, "Day 2": 2100, "Day 3": 1800, "Day 4": 2000}

series = pd.Series(calories)

series.loc["Day 4"] = 2100

print(series)