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

def plot_data(df, title, x_label = 'Dates', y_label = 'Values'):
  df.plot()
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()

def normalize_data(df):
  return df / df.iloc[0, :]

if __name__ == "__main__":
  start = '2019-03-01'
  end   = '2019-06-30'

  q2 = range(start, end)
  df = new_frame(q2)

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

  # plot_data(df, 'Q2')
  
  normalized_data = normalize_data(df)
  plot_data(normalized_data, 'Normalized Q2')