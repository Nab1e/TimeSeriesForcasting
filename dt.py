import pandas as pd

# Load the first CSV file
df1 = pd.read_csv('data1.csv', parse_dates=['Time'], date_parser=pd.to_datetime)

# Load the second CSV file
df2 = pd.read_csv('data2.csv', parse_dates=['Time'], date_parser=pd.to_datetime)

# Merge the two dataframes based on the common date column
merged_df = pd.merge(df1, df2, on='Time', how='inner')

# Save the merged dataframe to a new CSV file
merged_df.to_csv('merged_files.csv', index=False)
