import pandas as pd
calories = {"day1":1750,"day2":2100,"day3":1700}

series = pd.Series(calories)

print(series)

print(series.loc["day3"])

series.loc["day2"] += 500

print(series)

print(series[series >= 2000])