import pandas as pd
import altair as alt
data = pd.read_json("https://api.blockchain.com/v3/exchange/tickers")

alt.Chart(data).mark_bar()

