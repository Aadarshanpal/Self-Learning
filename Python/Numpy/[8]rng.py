import numpy as np

rng = np.random.default_rng()
# rng = np.random.default_rng(seed = num)     #seed helps reproduce same results

# print(rng.integers(1,101, size = (3,2)))

# print(np.random.uniform(low = -1, high = 1, size = (3,3)))

array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)