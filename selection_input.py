import pandas as pd

df = pd.read_csv("data.csv",index_col="name")

NAME = input("Enter a name (first letter capital):")

try:
    print(df.loc[NAME])
except KeyError:
    print(f"{NAME} not found")    