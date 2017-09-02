#clase para plotear las series de fourier

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special


class grafica(object):
	
	def __init__(self,amplitud=1,frecuencia=1,pntInicial = (-np.pi),periodo = (2 * np.pi),limite=10):
		self.amplitud = amplitud
		self.frecuencia = frecuencia
		self.pntInicial = pntInicial
		self.periodo = periodo
		self.limite = limite

	def cambioVariables(self,amplitud=1,frecuencia=1,pntInicial = (-np.pi),periodo = (2 * np.pi),limite=10):
		self.amplitud = amplitud
		self.frecuencia = frecuencia
		self.pntInicial = pntInicial
		self.periodo = periodo
		self.limite = limite

	def plotConst(self,t,constante = 5):
		w0 = (2*np.pi)/self.periodo
		resultA0 = integrate.quad(lambda x: constante,self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite):

			resultAn = integrate.quad(lambda x: (constante)*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: (constante)*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)

		return (a0 + an + bn)

	def plotRecta(self,t,pendiente=1,ordenada=0):
		w0 = (2*np.pi)/self.periodo
		resultA0 = integrate.quad(lambda x: (pendiente*x + ordenada),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite):

			resultAn = integrate.quad(lambda x: (pendiente*x + ordenada)*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: (pendiente*x + ordenada)*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		

		return (a0 + an + bn)

	def plotSen(self,t,amplitud=1,frecuencia=1):
		w0 = (2*np.pi)/self.periodo

		resultA0 = integrate.quad(lambda x: (amplitud*np.sin(frecuencia * x)),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite):

			resultAn = integrate.quad(lambda x: (amplitud*np.sin(frecuencia * x))*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: (amplitud*np.sin(frecuencia * x))*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		

		return (a0 + an + bn)

	def plotCos(self,t,amplitud=1,frecuencia=1):
		w0 = (2*np.pi)/self.periodo

		resultA0 = integrate.quad(lambda x: (amplitud*np.cos(frecuencia * x)),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite):

			resultAn = integrate.quad(lambda x: (amplitud*np.cos(frecuencia * x))*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: (amplitud*np.cos(frecuencia * x))*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		

		return (a0 + an + bn)



	def pinta(self,tipo = 4):
		t = np.arange(-5, 5, 0.001);
		y=0

		if tipo == 1:
			y = self.plotConst(t)
		elif tipo == 2:
			y = self.plotRecta(t)
		elif tipo == 3:
			y = self.plotSen(t)
		elif tipo == 4:
			y = self.plotCos(t)
		else:
			print("Tipo de gráfica no reconocido")


		

		plt.plot(t, y)

		plt.ylabel('some numbers')
		plt.show()

ploteo = grafica()
ploteo.pinta()