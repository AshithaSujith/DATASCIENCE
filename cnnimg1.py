import tensorflow as tf
from tensorflow.keras  import layers, models
import matplotlib.pyplot as plt

# Correct unpacking
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.cifar10.load_data()

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# print("Training set:", X_train.shape, y_train.shape)
# print("Test set:", X_test.shape, y_test.shape)

X_train=X_train.reshape(-1,28,28,1)
X_test=X_test.reshape(-1,28,28,1)
