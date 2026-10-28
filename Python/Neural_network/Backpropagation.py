import numpy as np

# -----inputs and target-----#

x = np.array([[2],
              [4]])

y = np.array([[1],
              [7]])

# -----Training parameters-----#

learning_rate = 0.01
epochs = 1000

# -----Weights and bias----- #

w1 = np.array([[3, 4],
               [4, 5],
               [6, 7]])


b1 = np.zeros((3,1))


w2 = np.array([[3, 7, 6],
               [6, 5, 8]])

b2 = np.zeros((2,1))


# -------Training loop-----------#

for epoch in range(epochs):
    # ------Forward pass--------#

    z1 = w1 @ x + b1

    a1 = np.maximum(0,z1)

    y_pred = w2 @ a1 + b2


    # -------Loss-------- #
    loss = 0.5 * np.sum((y-y_pred) ** 2)


    # ----- Backpropagation------ #
    delta_out = y_pred - y
    dw2 = delta_out @ a1.T

    db2 = delta_out

    delta_hidden = (w2.T @ delta_out) * (z1 > 0)

    dw1 = delta_hidden @ x.T
    db1 = delta_hidden


    #------ updaing parameters------#


    w2 = w2 - learning_rate * dw2
    b2 = b2 - learning_rate * db2

    w1 = w1 - learning_rate * dw1
    b1 = b1 - learning_rate * db1


print("Target: ",y)
print("Prediction: ", y_pred)

print("w1 = ",w1)
print("w2 = ",w2)
print("b1 = ",b1)
print("b2 = ",b2)

print("Loss = ", loss)