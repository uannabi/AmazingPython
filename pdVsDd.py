import pandas as pd
import dask.dataframe as dd
import time 

# Create a large DataFrame
size = 10**7
df_pd = pd.DataFrame({'X': range(size)})
df_dd = dd.from_pandas(df_pd, npartitions=10)

# Benchmark Pandas
start_time = time.time()
result_pd = df_pd['X'].sum()
end_time = time.time()
print(f"Pandas time: {end_time - start_time}")

# Benchmark Dask
start_time = time.time()
result_dd = df_dd['X'].sum().compute()  # Dask computation is lazy; .compute() ensures it's evaluated
end_time = time.time()
print(f"Dask time: {end_time - start_time}")
