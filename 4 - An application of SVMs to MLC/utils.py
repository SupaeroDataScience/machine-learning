from sklearn.utils import shuffle
import numpy as np

def shuffle_and_split(X, y, train_ratio=0.8, random_state=42):
    """
    Shuffle data and split it into train and test sets based on a specified ratio.

    Parameters:
    - X: Features (numpy array or pandas DataFrame)
    - y: Labels (numpy array or pandas Series)
    - train_ratio: Ratio of data to include in the train set (default is 0.8)
    - random_state: Seed for shuffling (default is None)

    Returns:
    - X_train, y_train, X_test, y_test: Shuffled and split data
    """
    X_shuffled, y_shuffled = shuffle(X, y, random_state=random_state)

    # Calculate the split point based on the train_ratio
    n = int(train_ratio * len(X_shuffled))

    X_train, X_test = X_shuffled[:n], X_shuffled[n:]
    y_train, y_test = y_shuffled[:n], y_shuffled[n:]

    return X_train, y_train, X_test, y_test