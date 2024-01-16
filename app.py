import finnhub
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ["API_KEY"]
finnhub_client = finnhub.Client(api_key=API_KEY)

print(finnhub_client.company_news('AAPL', _from="2020-06-01", to="2020-06-10"))
