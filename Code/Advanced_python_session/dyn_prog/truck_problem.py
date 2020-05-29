distance = 0
for i in range(1, 101):
	distance += 1.0/i
distance *= 100
print(distance)
import numpy as np
print( 100 *(0.5/100 + np.log(100) + 0.57721566490153286060651209008240243104215933593992))