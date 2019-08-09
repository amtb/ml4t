import pandas as pd
import matplotlib.pyplot as plt

def range(start, end):
  dates = pd.date_range(start, end)
  return dates

def new_frame(dates):
  return pd.DataFrame(index=dates)

def load_csv(ticker):
  data_frame = pd.read_csv(f'data/{ticker}.csv',
    index_col='Date',
    usecols=['Date', 'Adj Close'],
    na_values=['nan'],
    parse_dates=True)
  # print(data_frame.head()) # prints head
  return data_frame

if __name__ == "__main__":
  start = '2019-03-01'
  end   = '2019-03-31'

  jan = range(start, end)
  df = new_frame(jan)

  for ticker in ['GOOG', 'AMZN', 'QQQ', 'VOO']:
    data = load_csv(ticker)
    data = data.rename(columns={'Adj Close': ticker})
    # df = df.join(goog).dropna()
    df = df.join(data, how='inner')

  print(df)

  # slicing
  print('Rows')
  print(df.loc['2019-02-12':'2019-02-18'])

  print('Columns')
  print(df[['GOOG', 'AMZN']])

  print('Rows & columns')
  print(df.loc['2019-02-12':'2019-02-18', ['GOOG', 'AMZN']])

  df.plot()
  plt.show()