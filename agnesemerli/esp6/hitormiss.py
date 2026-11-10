import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import transforms

N= 10000

def parabola (x):
	return (3/1000)*x**2

x=np.random.uniform(0, 10, 100000)
y=np.random.uniform(0, 0.3, 100000)
mask = y <= parabola(x) 
plt.hist(x[mask], bins=100)
plt.show()

