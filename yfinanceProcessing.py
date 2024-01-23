import yfinance as yf
import pandas as pd

tickersString = "MMM,AOS,ABT,ABBV,ACN,ADBE,AMD,AES,AFL,A,APD,ABNB,AKAM,ALB,ARE,ALGN,ALLE,LNT,ALL,GOOGL,GOOG,MO,AMZN,AMCR,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,AME,AMGN,APH,ADI,ANSS,AON,APA,AAPL,AMAT,APTV,ACGL,ADM,ANET,AJG,AIZ,T,ATO,ADSK,ADP,AZO,AVB,AVY,AXON,BKR,BALL,BAC,BK,BBWI,BAX,BDX,BRK-B,BBY,BIO,TECH,BIIB,BLK,BX,BA,BKNG,BWA,BXP,BSX,BMY,AVGO,BR,BRO,BF-B,BLDR,BG,CDNS,CZR,CPT,CPB,COF,CAH,KMX,CCL,CARR,CTLT,CAT,CBOE,CBRE,CDW,CE,COR,CNC,CNP,CDAY,CF,CHRW,CRL,SCHW,CHTR,CVX,CMG,CB,CHD,CI,CINF,CTAS,CSCO,C,CFG,CLX,CME,CMS,KO,CTSH,CL,CMCSA,CMA,CAG,COP,ED,STZ,CEG,COO,CPRT,GLW,CTVA,CSGP,COST,CTRA,CCI,CSX,CMI,CVS,DHR,DRI,DVA,DE,DAL,XRAY,DVN,DXCM,FANG,DLR,DFS,DG,DLTR,D,DPZ,DOV,DOW,DHI,DTE,DUK,DD,EMN,ETN,EBAY,ECL,EIX,EW,EA,ELV,L"

tickers = tickersString.split(",")

start_date = "2022-12-30"
end_date = "2023-12-31"

all_returns = []

for stock_symbol in tickers:
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    stock_data['Daily_Return'] = (stock_data['Close'] - stock_data['Close'].shift(1)) / stock_data['Close'].shift(1) * 100
    stock_data = stock_data.dropna()
    
    # Extract the date and daily return columns, and rename the daily return column with the ticker symbol
    stock_data = stock_data[['Daily_Return']].rename(columns={'Daily_Return': stock_symbol})
    
    all_returns.append(stock_data)

# Concatenate all DataFrames in the list
all_returns = pd.concat(all_returns, axis=1)

print(all_returns)

#accessing the dataframe example
target_stock = 'EBAY'
target_date = '2023-12-22'
print(all_returns.loc[target_date, target_stock])