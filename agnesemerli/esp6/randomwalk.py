import sys
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import transforms

def random_walk(s, N):

    phi = np.random.uniform(0, 2*np.pi, N)

    deltax = s * np.cos(phi)
    deltay = s * np.sin(phi)

    return deltax, deltay
