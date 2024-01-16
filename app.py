import finnhub
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]
finnhub_client = finnhub.Client(api_key=API_KEY)

print(finnhub_client.stock_symbols('US'))