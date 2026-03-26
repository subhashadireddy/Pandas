import pandas as pd

data = {"name": ["Spongebob" , "patrick" , "squidrid"],
        "age": [10,20,30]}

df = pd.DataFrame(data)

print(df)

df1 = pd.DataFrame(data,index=["a","b","c"])
print(df1)

print(df1.loc["a"])

## adding a new COlumn
df["job"] = ["cook","n/a","cashier"]

#adding a new row 
new_row = pd.DataFrame([{"name":"sandy", "age":"40","job":"Engineer"}])
df = pd.concat([df,new_row])
print(df)