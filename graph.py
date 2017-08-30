import numpy as np
import matplotlib.pyplot as plt
import sympy as mp


class grafica(object):
	"""docstring for ClassName"""	
	#def __init__(self):
		#print("Hola graficador")


	def sumatoria(self,x):
		y = 0
		for n in range(0,10):
			y+= np.sin(x*n)/x
		return y



	def pinta(self):
		x = np.arange(-5, 5, 0.01);
		y = self.sumatoria(x)
		#y = np.sin(x)/x

		plt.plot(x, y)

		plt.ylabel('some numbers')
		plt.show()

	

ploteo = grafica()
ploteo.pinta()
