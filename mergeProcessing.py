import pandas as pd

# Assuming 'date' and 'ticker' are the common columns in both DataFrame

companyNews = pd.read_csv("Filtered_companyNews.csv")
dailyReturns = pd.read_csv("filledDailyReturns.csv")
filtered_companyNews = companyNews[(companyNews['date'] >= "2023-01-01") & (companyNews['date'] <= "2023-12-31")]


dailyReturns = dailyReturns.set_index('Date')

for index, row in filtered_companyNews.iterrows():
    # Accessing data for each row
    # print(f"Index: {index}, Ticker: {row['ticker']}, Date: {row['date']}, Headline: {row['headline']}")
    target_stock = row['ticker']
    target_date = row['date']
    dailyReturn = (dailyReturns.loc[target_date, target_stock])
    filtered_companyNews.loc[index, 'dailyReturn'] = dailyReturn

filtered_companyNews.to_csv("mergedData.csv", index=False)
print(filtered_companyNews)

# Save the merged DataFrame to CSV
# merged_data.to_csv('mergedData.csv', index=False)

# Display the merged DataFrame
# print(merged_data)
