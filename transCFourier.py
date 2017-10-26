from tkinter import *
import numpy as np
from scipy.fftpack import fft,ifft

class transCFourier(object):


	def integrand(self,func):
		return np.exp(np.imag(-j))

	def calcular(self):
		t = np.arange(-5, 5, 0.001);
		w = np.arange(-5,5,0.001)
		y=0
		w0 = (2*np.pi)/self.periodo
		#resultA0 = integrate.quad(lambda x: constante,self.pntInicial,self.pntInicial + self.periodo)
		#resultA0 = integrate.quad(lambda x: x,0,np.inf)
		a0 = resultA0[0]
		an=0
		bn=0

		
		y = resultA0[0]

		plt.plot(t, y)

		plt.ylabel('Transformada de Fourier')
		plt.show()

	def validaCampos(self):
		pass

	def __init__(self):
		ventana = Tk()
		ventana.title("Graficadora de la Transformada de Fourier")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Introduce los valores para graficar la la función cos(t)")
		lblTitulo.grid(columnspan=10,row=0)


		lblFuncion = Label(ventana,text="Introduce la Función a transformar")
		self.txtFuncion = Entry(ventana)
		lblFuncion.grid(column=0,row=1,sticky=E)
		self.txtFuncion.grid(column=1, row=1)

		lblpntInicial = Label(ventana,text="Introduce el Punto Inicial de Integración")
		self.txtpntInicial = Entry(ventana)
		lblpntInicial.grid(column=0,row=4 ,sticky=E)
		self.txtpntInicial.grid(column=1,row=4)

		lblpntFinal = Label(ventana,text="Introduce el Punto Final de Integración")
		self.txtpntFinal = Entry(ventana)
		lblpntFinal.grid(column=0,row=5 ,sticky=E)
		self.txtpntFinal.grid(column=1,row=5)

		btnCalcular = Button(ventana,text="Calcular",command=self.calcular)
		btnCalcular.grid(column=1,row=6)

		ventana.mainloop()

obj = transCFourier()