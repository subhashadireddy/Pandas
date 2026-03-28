#used for summarize and analyze data

import pandas as pd

df = pd.read_csv("aggregate.csv")
print(df)
#Whole DataFRame
#Finding mean to the coloums which are numeric 
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count())


#single Column

print(df["Price"].mean())
print(df["Price"].sum())
print(df["Price"].min())
print(df["Price"].max())
print(df["Price"].count())
