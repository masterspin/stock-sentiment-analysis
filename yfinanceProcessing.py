import yfinance as yf

# Define the stock symbol and time period
stock_symbol = "AAPL"
start_date = "2022-12-30"
end_date = "2023-12-31"

# Retrieve historical stock prices
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Calculate daily returns using the previous day's close
stock_data['Daily_Return'] = (stock_data['Close'] - stock_data['Close'].shift(1)) / stock_data['Close'].shift(1) * 100

# Drop the first row since it will have NaN values
stock_data = stock_data.dropna()

# Display the resulting DataFrame
print(stock_data[['Close', 'Daily_Return']])
