import pandas as pd

data = [100,102,104]

series = pd.Series(data)

print(series)

series1 = pd.Series(data,index = ["a","b","c"])
print(series1)
print(series1.loc["c"]) ##104

series1.loc["c"] = 200
print(series1)


print(series[series < 104])