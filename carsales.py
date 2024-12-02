import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/obinnauzozie/Downloads/car_prices.csv')

# Convert saledate column to datetime with error handling
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce')

# Display the first few rows to check the conversion
print(df.head())

# Check for any NaT values in the saledate column
print(df['saledate'].isna().sum())

# Set saledate as index 
df.set_index('saledate', inplace=True) 
 
