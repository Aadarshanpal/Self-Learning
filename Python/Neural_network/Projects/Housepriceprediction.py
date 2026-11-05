import numpy as np
np.random.seed(42)


# raw data
house_nums = 1000

area = np.random.randint(600,3001,size = house_nums)
bedrooms = np.random.randint(1,7,size = house_nums)

X = np.column_stack((area,bedrooms))

price = (150 * area + 20000 * bedrooms + np.random.normal(0,15000, size = house_nums ))

y = price.reshape((-1,1))


# Normalizing raw data (preprosessing)

training_set = int(0.8 * len(X))
eval_set = int(0.1 * len(X))

X_train_raw = X[:training_set]
X_eval_raw = X[training_set:training_set + eval_set]
X_test_raw = X[training_set + eval_set:]

y_train = y[:training_set].astype(float) / 100000
y_eval = y[training_set:training_set + eval_set].astype(float) / 100000
y_test = y[training_set + eval_set:].astype(float) / 100000

# Calculate normalization parameters from training data
X_min = np.min(X_train_raw, axis=0)
X_max = np.max(X_train_raw, axis=0)

# Apply the same normalization to all three sets
X_train = (X_train_raw - X_min) / (X_max - X_min)
X_eval = (X_eval_raw - X_min) / (X_max - X_min)
X_test = (X_test_raw - X_min) / (X_max - X_min)

# Training settings

lr = 0.0001 # Learning rate
epochs = 5000 # how many times does the machine learn

# Initializing weights and biases

W1 = np.random.randn(8,2)
b1 = np.zeros((8,1))

W2 = np.random.randn(1,8)
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
    loss =  1/y.size * np.sum((y_pred - y.T) ** 2)
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
    y_pred, a1, z1 = predict(X_train, W1, W2, b1, b2)

    # Calculate loss
    loss = loss_calc(y_pred,y_train)
    if epoch == 0:
        print("Initial loss at iter 1: ", loss)
    # Back propagation
    dY, dW2, db2 = delta_output(a1,y_train,y_pred)
    dW1, db1 = delta_hidden(X_train, W2, dY, z1)

    # Updating params
    W1 = Update_param(W1, dW1, lr)
    W2 = Update_param(W2, dW2, lr)
    b1 = Update_param(b1, db1, lr)
    b2 = Update_param(b2, db2, lr)

    if (epoch + 1) % 200 == 0:
        y_pred, _, _ = predict(X_eval, W1, W2, b1, b2)
        loss = loss = loss_calc(y_pred,y_eval)
        print(f"The loss at iteration {epoch + 1} is {loss}")

print("Training ended with the following result: ")


y_pred, a1, z1 = predict(X_train, W1, W2, b1, b2)
print("Loss: ", loss_calc(y_pred,y_train))
print("W1:",W1)
print("W2:",W2)
print("b1:",b1)
print("b2:",b2)


# Testing
y_pred, _, _ = predict(X_test, W1, W2, b1, b2)
loss  = loss_calc(y_pred,y_test)

print("The Testing results are:\n Loss: ",loss)