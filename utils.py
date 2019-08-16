import pandas as pd
import matplotlib.pyplot as plt

def load_csv(ticker, columns):
  columns.insert(0, 'Date')
  return pd.read_csv(f'data/{ticker}.csv',
    index_col='Date',
    usecols=columns,
    na_values=['nan'],
    parse_dates=True)

def plot_frame(df, title, x_label = 'Dates', y_label = 'Values'):
  plot = df.plot()
  plt.title(title)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()
  return plot

def normalize_frame(df):
  return df / df.iloc[0, :]

def dates_frame(start, end):
  dates = pd.date_range(start, end)
  return pd.DataFrame(index=dates)
