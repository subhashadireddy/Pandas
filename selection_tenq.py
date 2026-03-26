import pandas as pd

df = pd.read_csv("data.csv")

#selection by column
print(df["name"])
print(df[["name","age","city"]])

#search ROWS

#to search by name(index) keep the name as the indx column
df1 = pd.read_csv("data.csv" , index_col = "name")
print(df1)

#search by name
print(df1.loc["Manoj"])

print(df1.loc["Manoj",["age","city"]])

#range of rows
print(df1.loc["Manoj" : "Kavya"])