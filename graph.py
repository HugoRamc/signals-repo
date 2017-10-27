#clase para plotear las series de fourier

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.special as special



class graph(object):
	
	def __init__(self,pntInicial = (-np.pi),periodo = (2 * np.pi),limite=50):
		self.amplitud = 1
		self.frecuencia = 1
		self.pntInicial = pntInicial
		self.periodo = periodo
		self.limite = limite

	def plotConst(self,constante = 5):
		t = np.arange(-5, 5, 0.001);
		y=0
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

		plt.plot(t, y)

		plt.ylabel('Serie de Fourier')
		plt.grid()
		plt.show()


	def plotExponencial(self,amplitud=1,frecuencia=1,ordenada = 0):
		t = np.arange(-5, 5, 0.001);
		y=0

		w0 = (2*np.pi)/self.periodo

		resultA0 = integrate.quad(lambda x: ((amplitud*np.sin(frecuencia * x)) + ordenada),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite+1):

			resultAn = integrate.quad(lambda x: (amplitud*(np.exp(x*frecuencia)) + ordenada)*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: (amplitud*(np.exp(x*frecuencia)) + ordenada)*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		

		y = a0 + an + bn

		plt.plot(t, y)

		plt.ylabel('Serie de Fourier')
		plt.grid()
		plt.show()

	def plotRecta(self,pendiente=1,ordenada=0):
		t = np.arange(-5, 5, 0.001);
		y=0

		w0 = (2*np.pi)/self.periodo
		resultA0 = integrate.quad(lambda x: (pendiente*x + ordenada),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,int(self.limite)+1):

			resultAn = integrate.quad(lambda x: (pendiente*x + ordenada)*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: (pendiente*x + ordenada)*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		
		y = a0 + an + bn

		plt.plot(t, y)

		plt.ylabel('Serie de Fourier')
		plt.grid()
		plt.show()

	def plotSen(self,amplitud=1,frecuencia=1,ordenada = 0):
		t = np.arange(-5, 5, 0.001);
		y=0

		w0 = (2*np.pi)/self.periodo

		resultA0 = integrate.quad(lambda x: ((amplitud*np.sin(frecuencia * x)) + ordenada),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite+1):

			resultAn = integrate.quad(lambda x: ((amplitud*np.sin(frecuencia * x)) + ordenada)*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: ((amplitud*np.sin(frecuencia * x)) + ordenada)*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		

		y = a0 + an + bn

		plt.plot(t, y)

		plt.ylabel('Serie de Fourier')
		plt.grid()
		plt.show()

	def plotCos(self,amplitud=1,frecuencia=1,ordenada = 0):
		t = np.arange(-5, 5, 0.001);
		y=0
		w0 = (2*np.pi)/self.periodo

		resultA0 = integrate.quad(lambda x: ((amplitud*np.cos(frecuencia * x))+ordenada),self.pntInicial,self.pntInicial + self.periodo)
		a0 = resultA0[0]
		an=0
		bn=0

		
		for n in range(1,self.limite):

			resultAn = integrate.quad(lambda x: ((amplitud*np.cos(frecuencia * x))+ordenada)*np.cos(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)		
			resultBn = integrate.quad(lambda x: ((amplitud*np.cos(frecuencia * x))+ordenada)*np.sin(n*w0*x),self.pntInicial,self.pntInicial+self.periodo)

			an+= resultAn[0]*(2/self.periodo)*np.cos(n*w0*t)
			bn+= resultBn[0]*(2/self.periodo)*np.sin(n*w0*t)
		

		y = a0 + an + bn
		plt.plot(t, y)

		plt.ylabel('Serie de Fourier')
		plt.grid()
		plt.show()

#ploteo = graph()
#ploteo.plotExponencial()