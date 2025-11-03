import pandas as pd
import numpy as np

data = {'Name': ['Alice', 'Bob', np.nan, 'David'], 
        'Age': [25, 30, np.nan, 35], 
        'City': ['New York', np.nan, 'London', 'Paris']}

df = pd.DataFrame(data)

#identifying missing values
print("missing value counts per column:\n",df.isnull().sum())

#removing missing values
df_dropped = df.dropna()
print("\ndataframe after dropping null values: \n", df_dropped)

#imputing with mean
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print("\n dataframe filling missing 'Age' with mean:\n",df_filled_mean )

#imputing with median
df_filled_median = df.fillna(df.median(numeric_only=True))
print("\n dataframe filling missing 'Age' with median:\n", df_filled_median)

#handling outliers assuming 40 is max
df["Age capped"] = df["Age"].clip(upper=40)
print("\ndataframe with age capped at 40:\n",df)

#data type conversion
df["Age"] = pd.to_numeric(df["Age"],errors = "coerce")#convert to numeric, handling errors
print("\ndata types after conversion:\n", df.dtypes)

#exploratory data analysis
print("\n descriptive statistics:\n", df.describe())

#group by and aggregate
grouped_data = df.groupby('City')['Age'].mean()
print("\naverage age bycity:\n",grouped_data)