import requests
import json
data = requests.get("https://api.blockchain.com/v3/exchange/tickers")


print(data)
