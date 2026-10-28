# for a large number of weights and inputs we use vectors because thats easier

import numpy as np

x = np.array([3,4,5])
w = np.array([3,2,1])
b = 1

prediction = np.dot(x,w) + b
print(prediction)