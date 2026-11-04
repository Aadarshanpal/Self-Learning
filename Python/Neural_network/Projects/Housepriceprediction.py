import numpy as np

# raw data
X = np.array([[800, 2],
              [1000, 2],
              [1200, 3],
              [1400, 3],
              [1600, 3],
              [1800, 4],
              [2000, 5]])

y = np.array([[100000],
              [150000],
              [200000],
              [250000],
              [300000],
              [350000],
              [400000]])


# Normalizing raw data (preprosessing)
X_normalized = X.astype(float)
X_normalized[:,0] = X_normalized[:,0] / 1000

Y_normalized = y.astype(float)
Y_normalized = Y_normalized / 100000

# Training settings

lr = 0.001 # Learning rate
epochs = 5000 # how many times does the machine learn

# Initializing weights and biases

W1 = np.random.rand(3,2)
b1 = np.zeros((3,1))

W2 = np.random.rand(1,3)
b2 = np.zeros((1,1))

# ReLU (Rectified Linear Unit)

def ReLU(Z):
    return np.maximum(0,Z)


# Prediction function

def predict(X,W1,W2,b1,b2):
    z1 = W1 @ X.T + b1
    a1 = ReLU(z1)

    y_pred = W2 @ a1 + b2
    return y_pred, a1, z1 


# Loss function

def loss_calc(y_pred,y):
    loss =  1/y.size * np.sum((y_pred - y) ** 2)
    return loss


# Calculating deltas
def delta_output(a1,y,y_pred):
    dY = 2/y.size * (y_pred - y.T)
    dW2 = dY @ a1.T
    db2 = np.sum(dY, axis = 1, keepdims = True)

    return dY, dW2, db2

def delta_hidden(X,W2,dY,Z):
    dA1 = W2.T @ dY
    dZ1 = dA1 * (Z > 0)
    dW1 = dZ1 @ X
    db1 = np.sum(dZ1, axis = 1, keepdims=True)

    return dW1, db1


# Updating params
def Update_param(param,delta,lr):
    return param - delta * lr


# Main loop

for epoch in range(epochs):
    # Predict 
    y_pred, a1, z1 = predict(X_normalized, W1, W2, b1, b2)

    # Calculate loss
    loss = loss_calc(y_pred,Y_normalized)

    # Back propagation
    dY, dW2, db2 = delta_output(a1,Y_normalized,y_pred)
    dW1, db1 = delta_hidden(X_normalized, W2, dY, z1)

    # Updating params
    W1 = Update_param(W1, dW1, lr)
    W2 = Update_param(W2, dW2, lr)
    b1 = Update_param(b1, db1, lr)
    b2 = Update_param(b2, db2, lr)

    if epoch % 100 == 0:
        print(f"Loss at iteration", epoch, "is", loss)


print("Training ended with the following result: ")

print("Loss: ", loss_calc(y_pred,Y_normalized))
print("W1:",W1)
print("W2:",W2)
print("b1:",b1)
print("b2:",b2)

print("Final hidden activations:")
print(a1)
print("Final Z1:")
print(z1)