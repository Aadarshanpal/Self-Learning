import numpy as np

array = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                [['S', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]])

# Simple trick to remember is that numeber of "[" brackets = dimension

print(array.shape)

# Start looking from the largest i.e (3,3,3) first 3 is the largest thing you can look at,
# the number of layers, second 3 is just a bit zoomed in, 3 rows and the last 3 is max zoomed
# 3 elements.

print(array[2,2,1])
