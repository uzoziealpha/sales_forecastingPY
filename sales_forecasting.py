import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/obinnauzozie/Downloads/car_prices.csv')

# Convert saledate column to datetime with UTC
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)

# Display the first few rows to check the conversion
#print(df.head())

# Check for any NaT values in the saledate column
print(df['saledate'].isna().sum())

# Set saledate as index
df.set_index('saledate', inplace=True)

# Display the first few rows to check the index
#print(df.head())

# Resample data to monthly sales
monthly_sales = df['sellingprice'].resample('M').sum()

# Display the first few rows of the resampled data
print(monthly_sales.head())



# Plot the sales data
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales)
plt.title('Monthly Sales Data')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

