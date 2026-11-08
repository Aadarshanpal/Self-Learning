import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 1000

# 1. Generate features
# Hours studied: Uniform distribution between 1.0 and 10.0 hours
hours_studied = np.random.uniform(1.0, 10.0, n_samples)

# Prior knowledge: Uniform scale from 0 to 10
prior_knowledge = np.random.uniform(0.0, 10.0, n_samples)

# Quality sleep: Normal distribution centered around 7 hours (std dev: 1.2), clipped between 4 and 9
quality_sleep = np.clip(np.random.normal(7.0, 1.2, n_samples), 4.0, 9.0)

# 2. Combine features into an (N, 3) input array X
X = np.column_stack((hours_studied, prior_knowledge, quality_sleep))

# 3. Generate target variable y (Marks obtained out of 100)
# Formula: Base score + weight*hours + weight*prior + weight*sleep + random noise
base_score = 20
noise = np.random.normal(0, 3.5, n_samples) # Gaussian noise for realism

marks_obtained = (
    base_score 
    + (5.5 * hours_studied) 
    + (3.0 * prior_knowledge) 
    + (2.5 * quality_sleep) 
    + noise
)

# Clip marks to a realistic 0–100 percentage range
marks_obtained = np.clip(marks_obtained, 0.0, 100.0)

# Reshape y to be a column vector (100, 1) to align nicely with X 
y = marks_obtained.reshape(-1, 1)



# Dividing the data into sets

training_set = int(0.8 * len(X))
evaluation_set = int(0.1 * len(X))

X_train = X[:training_set]
X_eval = X[training_set: training_set + evaluation_set]
X_test= X[training_set + evaluation_set:]

y_train = y[:training_set]
y_eval = y[training_set: training_set + evaluation_set]
y_test = y[training_set + evaluation_set: ]


# Training settings

lr = 0.0001
epochs = 2000


# Weights and biases

W1 = np.random.randn(4,3)
b1 = np.zeros((4,1))

W2 = np.random.randn(1,4)
b2 = np.zeros((1,1))


# Keeping history to plot later
loss_history = []
epoch_history = []


# Rectified linear unit
def ReLU(z):
    return np.maximum(0.01*z,z)


# Predcition
def predict(X,W1,W2,b1,b2):
    z1 = W1 @ X.T + b1
    a1 = ReLU(z1)

    y_pred = W2 @ a1 + b2

    return y_pred, z1, a1


# Loss
def loss_calc(y_pred,y):
    loss = 1/y.size * np.sum((y_pred - y.T) ** 2)
    return loss


# Deltas for back propagation

# Output deltas 
def delta_output(a1,y_pred,y):
    dY = 2/y.size * (y_pred - y.T)
    dW2 = dY @ a1.T
    db2 = np.sum(dY)

    return dY, dW2, db2


# hidden delta
def delta_hidden(X,dY,W2,z1):
    da1 = W2.T @ dY
    dz1 = da1 * np.where(z1 > 0, 1, 0.01)

    dW1 = dz1 @ X
    db1 = np.sum(dz1, axis = 1, keepdims = True)

    return dW1, db1


# Update parameters
def update_params(param,delta,lr):
    return param - delta * lr


# Learning loop

for epoch in range(epochs):
    # predict
    y_pred, z1, a1 = predict(X_train,W1,W2,b1,b2)

    # calc loss
    loss = loss_calc(y_pred,y_train)

    # calc deltas
    dY, dW2, db2 = delta_output(a1,y_pred,y_train)
    dW1, db1 = delta_hidden(X_train,dY,W2,z1)

    if (epoch + 1) % 100 == 0:
        y_pred, z1, a1 = predict(X_eval,W1,W2,b1,b2)
        
        loss = loss_calc(y_pred,y_eval)
        loss_history.append(loss)
        epoch_history.append(epoch + 1)
        print(f"Loss at iteration {epoch + 1} is {loss}.\n")

    # update params
    W1 = update_params(W1,dW1,lr)
    W2 = update_params(W2,dW2,lr)
    b1 = update_params(b1,db1,lr)
    b2 = update_params(b2,db2,lr)

y_pred, _, _ = predict(X_test,W1,W2,b1,b2)
loss = loss_calc(y_pred,y_test)

# Printing the loss of the test set
print("The loss of the test set was: ",loss, " over a 100 examples.\nMaking the root mean square error: ",np.sqrt(loss))
print("Meaning the average difference between actual marks and predicted marks is: ",np.sqrt(loss))


# Ploting graph
plt.plot(epoch_history, loss_history)

plt.xlabel("Iteration")
plt.ylabel("Loss")

plt.title("Evaluation loss V/S Iterations")
plt.show()

