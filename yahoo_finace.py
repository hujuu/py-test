import pandas_datareader.data as web
import pandas as pd

all_data = {ticker: web.get_data_yahoo(ticker)
            for ticker in ['AAPL', 'IBM']}

price = pd.DataFrame({ticker: data['Adj Close']
                      for ticker, data in all_data.items()})

volume = pd.DataFrame({ticker: data['Volume']
                       for ticker, data in all_data.items()})

returns = price.pct_change()

print(returns.tail())

