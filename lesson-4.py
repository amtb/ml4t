import numpy as np

if __name__ == "__main__":
  array_1 = np.array([1, 2, 3])
  print(array_1)

  array_2 = np.array([(1, 2, 3), (4, 5, 6)])
  print(array_2)

  # generates a 5*4 2D array of ones
  ones = np.ones((5, 4), np.int64)
  print(ones)

  random_ints = np.random.randint(0, 10, size=(5))
  print(random_ints)

  # few attributes
  print(random_ints.size)
  print(ones.shape)

  # operations
  print('Sum array_2 = ', array_2.sum())
  print('Sum of the rows = ', array_2.sum(axis=0))
  print('Sum of the columns = ', array_2.sum(axis=1))
  print('Min of each row = ', array_2.min(axis=0))
  print('Max of each column = ', array_2.max(axis=1))
  print('Mean of the array = ', array_2.mean())

  # slicing
  print('First column = ', array_2[:, 0])
  print('Second row = ', array_2[1, :])

  # masking
  print('Less than 4 = ', array_2[array_2 <= 4])

  # arithmetic ops
  twos = 2 * ones
  print(twos)

  multiply = ones * twos
  print(multiply)