import pandas as pd
import matplotlib.pyplot as plt
import utils

def get_rolling_mean(values, window):
  """Return rolling mean of given values, using specified window size."""
  return values.rolling(window).mean()

def get_rolling_std(values, window):
  """Return rolling standard deviation of given values, using specified window size."""
  return values.rolling(window).std() 

def get_bollinger_bands(rm, rstd):
  """Return upper and lower Bollinger Bands."""
  upper_band = rm + (2 * rstd)
  lower_band = rm - (2 * rstd)
  return upper_band, lower_band


def compute_daily_returns(df):
  """Compute and return the daily return values."""
  daily_returns = df.copy()
  # daily_returns.iloc[1:] = (df[1:] / df[:-1].values) - 1
  # Pandas way
  daily_returns.iloc[1:] = (df[1:] / df.shift(1)) - 1
  daily_returns.iloc[0] = 0

  return daily_returns

def compute_cumulative_returns(df):
  cumulative_returns = df.copy()
  cumulative_returns.iloc[0:] = 100 * ((df.iloc[0:] / df.iloc[0]) - 1)
  return cumulative_returns

if __name__ == "__main__":
  start = '2018-01-01'
  end   = '2018-12-31'

  df = utils.dates_frame(start, end)

  for ticker in ['GOOG', 'AMZN', 'QQQ', 'VOO']:
    data = utils.load_csv(ticker, ['Adj Close'])
    data = data.rename(columns={'Adj Close': ticker})
    df = df.join(data, how='inner')

  # print(df)

  # utils.plot_frame(utils.normalize_frame(df), 'Normalized')

  mean = df.mean()
  print('Mean of each ticker')
  print(mean)

  median = df.median()
  print('Median of each ticker')
  print(median)

  std = df.std()
  print('Standard deviation of each ticker')
  print(std)

  # Rolling mean / Bollinger bands on a 20 days period for AMZN
  window = 20
  amazon = df['AMZN']
  rolling_mean = get_rolling_mean(amazon, window)
  rolling_std = get_rolling_std(amazon, window)
  upper_band, lower_band = get_bollinger_bands(rolling_mean, rolling_std)
  
  # ax = amazon.plot(label='Amazon')
  # rolling_mean.plot(label='Rolling mean', ax=ax)
  # upper_band.plot(label='Upper band', ax=ax)
  # lower_band.plot(label='Lower band', ax=ax)
  
  '''
  ax.set_xlabel('Dates')
  ax.set_ylabel('Adjusted close')
  ax.legend(loc="upper left")
  plt.show()
  '''
  
  # Daily returns
  daily_returns = compute_daily_returns(df)
  daily_returns.plot(label="Daily returns")
  plt.show()

  # Cumulative returns
  cumulative_returns = compute_cumulative_returns(df)
  cumulative_returns.plot(label="Cumulative returns")
  plt.show()
