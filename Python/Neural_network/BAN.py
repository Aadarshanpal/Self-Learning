import numpy as np

b1 = np.zeros((3, 1))
b2 = np.zeros((2, 1))

x = np.array([[2.0],
              [3.0]])

y = np.array([[5.0],
              [6.0]])

W1 = np.array([[1.0, -1.0],
               [1.0,  2.0],
               [3.0, -4.0]])

W2 = np.array([[1.0, 2.0, -1.0],
               [1.0, 3.0,  2.0]])

z1 = W1 @ x + b1
a1 = np.maximum(0, z1)

z2 = W2 @ a1 + b2
y_predict = np.maximum(0, z2)

loss = 0.5 * np.sum((y - y_predict) ** 2)

print("Hidden layer:\n", a1)
print("Predictions:\n", y_predict)
print("Loss:", loss)