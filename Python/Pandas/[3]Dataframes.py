# dataframes = A tabular data structure with rows and columns (2D)

import pandas as pd


data = {"Name": ["Aadarsha", "Aasana", "Just us"],
        "Age": [19, 21, 1]}

df = pd.DataFrame(data, index = ["Man","Women","Relationship"])

#Add a new column
df["Job"] = ["Husband", "Wife", "Married"]


#Add a new row
new_row = pd.DataFrame([{"Name": "Child" , "Age": 0, "Job": "Child"}], index = ["Unborn"])


df = pd.concat([df, new_row])


print(df)