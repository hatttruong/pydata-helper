# coding: utf-8

import pandas as pd

# prepare symbol_infos.csv
info_df = pd.read_csv('infor.csv')
info_df[['symbol', 'name', 'exchange']].to_csv('symbol_infos.csv', index=False)


# prepare stock_prices.csv
df = pd.read_csv('stocks.csv')
df.rename(index=str,
          columns={"adj_open": "open", "adj_low": "low",
                   "adj_high": "high", "adj_close": "close"},
          inplace=True)
df[['symbol', 'date', 'open', 'high', 'low', 'close', 'volume']].to_csv(
    'stock_prices.csv', index=False)
