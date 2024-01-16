import os
from dotenv import load_dotenv
import time
import pandas as pd
from langdetect import detect

finnhubDF = pd.read_csv('companyNews.csv')

finnhubDF['language'] = finnhubDF['headline'].apply(lambda x: detect(str(x)) if pd.notna(x) else None)

# Drop rows where language is not English
finnhubDF = finnhubDF[finnhubDF['language'] == 'en']

# Drop the 'language' column if you don't need it anymore
finnhubDF = finnhubDF.drop(columns=['language'])

finnhubDF.to_csv("Filtered_companyNews.csv", index=False)
