import numpy as np

ages = np.array([[21,17,18,45,66,99,101],
                [80,17,23,25,67,68,71]])



#print(ages[(ages > 18) & (ages < 65)])

adults = np.where(ages > 18, ages, 0)

print(adults)