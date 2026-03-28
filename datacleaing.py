import pandas as pd
df = pd.read_csv("clean_data.csv")
#dropping colums 
# df = df.drop(columns=["Irrelevant_Column"])
# print(df)

#handling missing data (the rows are deleted)
# df1 = df.dropna(subset=["Quantity"])
# print(df1)

#fix inconsistent values
# df["Product"] = df["Product"].replace({"Chair" : "CHAIR"})
# print(df)

#Fix Datatypes
# df["Sales"] = df["Sales"].astype(bool)
# print(df)

#remove Duplicates
df = df.drop_duplicates()
print(df)