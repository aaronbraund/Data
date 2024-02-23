import pandas as pd
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)
print(df.head())

filtered_df = df.query("sepal_length > 5.0")
print(filtered_df.head())