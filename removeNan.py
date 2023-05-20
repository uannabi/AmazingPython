
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({
  'A': ['foo', 'bar', 'baz'],
  'B': ['one', 'one', 'two'],
  'C': ['x', 'y', 'z'],
  'D': [1, 2, 3]
})

# Convert the DataFrame to a dictionary
dict_df = df.to_dict()

print(dict_df)


# Drop rows with null values
df.dropna(axis=0, inplace=True)

# Drop columns with null values
df.dropna(axis=1, inplace=True)

# Fill null values with a specific value (e.g., 0)
df.fillna(0, inplace=True)

# Fill null values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Fill null values with the previous value in the column (forward fill)
df.fillna(method='ffill', inplace=True)

# Fill null values with the next value in the column (backward fill)
df.fillna(method='bfill', inplace=True)

# Replace null values with a specific value (e.g., -1)
df.replace(np.nan, -1, inplace=True)

# Fill null values using linear interpolation
df.interpolate(method='linear', inplace=True)


