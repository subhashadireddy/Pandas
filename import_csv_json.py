import pandas as pd
#csv
df = pd.read_csv("data.csv")

print(df)
#Json
df1 = pd.read_json("data.json")
print("\n\nJSON\n\n")
print(df1)
print("\n\n\n")
print(df1.to_string())