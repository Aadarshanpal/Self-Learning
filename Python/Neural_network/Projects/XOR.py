import numpy as np
np.random.seed(64)

# Raw dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

# Weights and biases

W1 = np.random.randn(2,2)
b1 = np.zeros((2,1))

W2 = np.random.randn(1,2)
b2 = np.zeros((1,1))


