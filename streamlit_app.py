import pandas as pd
import json
data = pd.read_json("https://api.blockchain.com/v3/exchange/tickers")


print(data)
