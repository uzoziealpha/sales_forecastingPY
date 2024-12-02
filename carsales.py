import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA

# Load the dataset
df = pd.read_csv('/Users/obinnauzozie/Downloads/car_prices.csv')

# Convert saledate column to datetime with UTC
df['saledate'] = pd.to_datetime(df['saledate'], errors='coerce', utc=True)

# Display the first few rows to check the conversion
print(df.head())

# Check for any NaT values in the saledate column
print(df['saledate'].isna().sum())

# Set saledate as index
df.set_index('saledate', inplace=True)

# Display the first few rows to check the index
print(df.head())

# Resample data to monthly sales
monthly_sales = df['sellingprice'].resample('M').sum()

# Display the first few rows of the resampled data
print(monthly_sales.head())

# Exploratory Data Analysis
# Plot the sales data
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales)
plt.title('Monthly Sales Data')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Fit the ARIMA Model to the monthly sales data
model = ARIMA(monthly_sales, order=(5, 1, 0))
model_fit = model.fit(disp=0)

# Display the model summary
print(model_fit.summary())

# Forecast future sales for the next 12 months
forecast = model_fit.forecast(steps=12)[0]

# Display the forecasted values
print(forecast)

# Plot the forecast
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales, label='Actual Sales')
plt.plot(pd.date_range(start=monthly_sales.index[-1], periods=12, freq='M'), forecast, label='Forecasted Sales')
plt.title('Sales Forecast')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.show()

# Export the forecasted data to a CSV file
forecast_df = pd.DataFrame({
    'date': pd.date_range(start=monthly_sales.index[-1], periods=12, freq='M'),
    'forecast': forecast
})

forecast_df.to_csv('forecasted_sales.csv', index=False)

# Display the first few rows of the forecasted data
#print(forecast_df.head())

# Specify the path where you want to save the CSV file 
csv_path = os.path.expanduser('~/Downloads/forecasted_sales.csv') 
forecast_df.to_csv(csv_path, index=False) 
print(forecast_df.head())