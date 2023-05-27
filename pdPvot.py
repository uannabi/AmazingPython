
import pandas as pd

# Create a sample dataframe
data = {
    'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-02'],
    'Category': ['A', 'B', 'A', 'B', 'C'],
    'Value': [10, 20, 30, 40, 50]
}

df = pd.DataFrame(data)

# Create a pivot table
pivot_table = df.pivot_table(index='Date', columns='Category', values='Value', aggfunc='sum')

print(pivot_table)

'''
In this example, the dataframe df contains three columns: 'Date', 'Category', and 'Value'. We want to create a pivot table that summarizes the 'Value' column based on the 'Date' and 'Category' columns.

By using the pivot_table() function, we specify the index column ('Date'), the columns to be used as columns in the pivot table ('Category'), and the values to be aggregated ('Value'). The aggfunc parameter is used to define the aggregation function to be applied when multiple values exist for a specific combination of index and column.

The resulting pivot table is stored in the variable pivot_table and is printed to the console. It shows the sum of 'Value' for each combination of 'Date' and 'Category'.

Pivot tables are a powerful tool for summarizing and analyzing data, allowing you to transform and present the data in a more meaningful way for analysis and reporting purposes.

'''
