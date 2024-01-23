import os
from dotenv import load_dotenv
import time
import pandas as pd
from langdetect import detect

finnhubDF = pd.read_csv('companyNews.csv')

finnhubDF['language'] = finnhubDF['headline'].apply(lambda x: detect(str(x)) if pd.notna(x) else None)

finnhubDF = finnhubDF[finnhubDF['language'] == 'en']

finnhubDF = finnhubDF.drop(columns=['language'])

finnhubDF.to_csv("Filtered_companyNews.csv", index=False)
