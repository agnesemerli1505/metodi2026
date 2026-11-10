import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import transforms


N = 10000
u=np.random.random(100000)
def cumulativa(u):
	return 10*u**(1/3)
x=cumulativa(u)
plt.hist(x, bins=100)
plt.show()
	

