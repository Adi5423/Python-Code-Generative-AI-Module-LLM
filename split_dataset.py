import numpy as np
from sklearn.model_selection import train_test_split

def split_dataset(dataset, test_size=0.25):
  """Splits the dataset into a training set and a test set.

  Args:
    dataset: A NumPy array containing the dataset.
    test_size: The proportion of the dataset to use for the test set.

  Returns:
    X_train: A NumPy array containing the training set.
    X_test: A NumPy array containing the test set.
  """

  X_train, X_test = train_test_split(dataset, test_size=test_size)

  return X_train, X_test
