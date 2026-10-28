import numpy as np

x= np.array([[2],
             [3]])

W = np.array([[1,2],
              [-1,1],
              [3,-2]])

b = np.array([[1],
              [0],
              [-1]])

z = W @ x + b

a = np.maximum(0,z)

print("z:",z,"\na:",a)

# second layer


W2 = np.array([[1,2,3],
               [4,5,-6],
               [-7,8,9],
               [10,-11,-12]])   

b2 = np.array([[1],
               [1],
               [-1],
               [-2]])

z2 = W2 @ a + b2

a2 = np.maximum(0,z2)

print("z:",z2,"\na:",a2)