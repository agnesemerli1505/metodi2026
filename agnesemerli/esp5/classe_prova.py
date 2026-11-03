import numpy as np
import pandas as pd

class dati:
	
	def __init__(self, df): #costruttore
		self.data= df
		
		self.x= df['TIME']
		self.y= df['PDCSAP_FLUX']
	'''def __str__(self):
		return (self.data.__str__)'''
		
		
