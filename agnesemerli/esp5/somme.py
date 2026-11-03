import numpy as np

def somma(n):
	som=0
	prod=1
	
	for i in range(1, n+1):
		som= som + i
	for i in range(1, n+1):
		prod=prod*i
		
	return som, prod
	
def somma_radice(n):
	somma=0
	
	for i in range(1, n+1):
		somma= somma + np.sqrt(n)
		
	return somma
def somma_potenze(n, a):
	somma=0
	
	for i in range(1, n+1):
		somma= somma + i*a
		
	return somma
