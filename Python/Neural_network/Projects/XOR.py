import numpy as np
np.random.seed(42)

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

W1 = np.random.randn(4,2)
b1 = np.zeros((4,1))

W2 = np.random.randn(1,4)
b2 = np.zeros((1,1))


# Training settings
lr = 0.1
epochs = 5000


# Rectified Linear Unit

def ReLU(z1):
    return np.maximum(0.01 * z1, z1)



# Sigmoid to produce output (0-1)

def sigmoid(y):
    return 1 / (1 + np.exp(-y))


# Actual prediction

def predict(X,W1,W2,b1,b2):
    z1 = W1 @ X.T + b1
    a1 = ReLU(z1)

    y_pred = W2 @ a1 + b2

    return sigmoid(y_pred), a1, z1


# Binary entropy loss

def loss_calc(y,y_pred):
    loss =  -((1 / y.size) * np.sum(y*np.log(y_pred) + np.log(1-y_pred) *(1-y)))
    return loss



# Calculating deltas 

def delta_output(y_pred,y,a1):
    delta_out = y_pred - y

    dw2 = 1/y.size * delta_out @ a1.T

    db2 = 1/y.size * np.sum(delta_out)

    return delta_out, dw2, db2


def delta_hidden(z1,W2,delta_output,y,X):
    da1 = W2.T @ delta_output 
    dZ1 = da1 * np.where(z1 > 0, 1, 0.01)

    dw1 = 1/y.size * dZ1 @ X
    db1 = 1/ y.size * np.sum(dZ1, axis = 1, keepdims = True)

    return dw1,db1


# Updating params
def update_param(param,delta,lr):
    return param - delta * lr



for epoch in range(epochs):
    # Prediction
    y_pred, a1, z1 = predict(X,W1,W2,b1,b2)


    # loss
    loss = loss_calc(y.T,y_pred)

    if (epoch + 1) % 100 == 0:
        print(f"The loss at iteration {epoch} is {loss}.\n")

    # Deltas
    delta_out, dw2, db2 = delta_output(y_pred,y.T,a1)
    dw1,db1 = delta_hidden(z1,W2,delta_out,y.T,X)

    # Update parameters
    W1 = update_param(W1,dw1,lr)
    W2 = update_param(W2,dw2,lr)
    b1 = update_param(b1,db1,lr)
    b2 = update_param(b2,db2,lr)


y_pred, _,_ = predict(X,W1,W2,b1,b2)
print("The final loss of the network is: ",loss_calc(y.T,y_pred))
y_pred = y_pred.T
for i in range(y.size):
    print(X[i][0]," XOR ",X[i][1], " = ", y_pred[i])

print("W1:\n", W1)
print("b1:\n", b1)
print("W2:\n", W2)
print("b2:\n", b2)


np.savez("Xor_Data.npz",
         W1 = W1,
         W2 = W2,
         b1 = b1,
         b2 = b2)