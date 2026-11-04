import numpy as np


X = np.array([
    [800,  2],
    [900,  2],
    [1000, 2],
    [1100, 3],
    [1200, 3],
    [1300, 3],
    [1400, 3],
    [1500, 3],
    [1600, 3],
    [1700, 3],
    [1800, 4],
    [1900, 4],
    [2000, 4],
    [2100, 4],
    [2200, 4],
    [2300, 4],
    [2400, 4],
    [2500, 4],
    [2600, 5],
    [2700, 5]
])

y = np.array([
    [100000],
    [110000],
    [120000],
    [130000],
    [140000],
    [150000],
    [160000],
    [170000],
    [180000],
    [190000],
    [200000],
    [210000],
    [220000],
    [230000],
    [240000],
    [250000],
    [260000],
    [270000],
    [280000],
    [290000]
])

rng = np.random.defaukt_rng(42)
indices = rng.permutaion(len(X))

train_size = int(len(X) * 0.8)
validation_size = int(len(X) * 0.1)

# Split indices
train_indices = indices[:train_size]
validation_indices = indices[train_size: train_size + validation_size]
test_size = indices[train_size + validation_size:]

X_train = X[train_indices]
Y_train = y[train_indices]

X_val = X[validation_indices]
Y_val = y[validation_indices]

X_train = X[train_indices]
Y_train = y[train_indices]

