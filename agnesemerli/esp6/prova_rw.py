import randomwalk 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
from randomwalk import random_walk

s=1
N=1000
ubriachi=5
X = np.zeros((ubriachi, N+1))
Y = np.zeros((ubriachi, N+1))


for i in range(0, ubriachi):
	dx,dy = random_walk(s,N)
	
	X[i,1:] = np.cumsum(dx)
	Y[i,1:] = np.cumsum(dy)

	plt.plot(X[i], Y[i])
	
plt.show()
