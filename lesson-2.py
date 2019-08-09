import pandas as pd
import matplotlib.pyplot as plt

def load_csv(file_name):
  data_frame = pd.read_csv(file_name)
  # print(data_frame.head()) # prints head
  return data_frame

if __name__ == "__main__":
  # print('Amazon')
  # load_csv('data/AMZN.csv')

  # print('Google')
  # google = load_csv('data/GOOG.csv')
  # print(google[20:30]) # prints a range of rows (slicing)

  '''
  for ticker in ['AMZN', 'GOOG']:
    df = load_csv(f'data/{ticker}.csv')

    print(f'${ticker}')
    print('Max close')
    print(df['Close'].max())
    print('Mean volume')
    print(df['Volume'].mean())
  '''

  google = load_csv('data/GOOG.csv')
  print(google.head())
  
  to_plot = google[['High', 'Adj Close']]
  print(to_plot)

  to_plot.plot()
  plt.show()