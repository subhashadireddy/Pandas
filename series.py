import pandas as pd

data = [100,102,104]

series = pd.Series(data)

print(series)

series1 = pd.Series(data,index = ["a","b","c"])
print(series1)