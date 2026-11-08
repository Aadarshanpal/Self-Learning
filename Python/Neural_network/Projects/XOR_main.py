import numpy as np

data = np.load(r"Python\Neural_network\Projects\Xor_Data.npz")

W1 = data["W1"]
W2 = data["W2"]
b1 = data["b1"]
b2=  data["b2"]


def ReLU(z1):
    return np.maximum(0.01 * z1, z1)

def sigmoid(y):
    return 1 / (1 + np.exp(-y))


# Actual prediction

def predict(X,W1,W2,b1,b2):
    z1 = W1 @ X.T + b1
    a1 = ReLU(z1)

    y_pred = W2 @ a1 + b2

    return sigmoid(y_pred)


n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the Second number: "))

if (n1 != 0 and n1 != 1) or (n2 != 0 and n2 != 1):
    print("Enter a valid number 0 or 1.\n")
    exit(0)

X = np.array([[n1,n2]])


output = predict(X,W1,W2,b1,b2)
print(n1, " XOR ", n2, " = ", round(output[0][0]))