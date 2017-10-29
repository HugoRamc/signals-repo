from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 
from scipy.fftpack import fft, ifft
from validaStrings import *


class transDFour(object):
	
	def __init__(self):

		#self.pendiente = StringVar()
		
		ventana = Tk()
		ventana.title("Calcular Transformada Discreta de Fourier")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Transformada Discreta de Fourier")
		lblTitulo.grid(columnspan=10,row=0)


		lblMuestras = Label(ventana,text="Introduce las muestras de la Función separadas por comas")
		self.txtMuestras = Entry(ventana)
		lblMuestras.grid(column=0,row=1,sticky=E)
		self.txtMuestras.grid(column=0, row=2)

		lblMuestreo = Label(ventana,text="Introduce el periodo de muestreo")
		self.txtMuestreo = Entry(ventana)
		lblMuestreo.grid(column=0,row=3,sticky=E)
		self.txtMuestreo.grid(column=0, row=4)
		
		self.btnGrafica = Button(ventana,text="Graficar",command=self.calculaTrans)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def calculaTrans(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		#espacio = self.txtespacio.get()
		muestras = self.txtMuestras.get()
		periodom = self.txtMuestreo.get()
		valida = validaStrings()
		lista = muestras.split(",")
		listanums = []
		edo = 0
		for i in range(len(lista)):
			if(valida.validaCadena(lista[i])==1):
				listanums.append(valida.getValorCadena(lista[i]))
			else:
				edo = 1

		if(valida.validaCadena(periodom)==1):
			nper = (valida.getValorCadena(periodom))
		else:
			edo = 1
		if(edo == 0):
			
			y =  fft(lista)			
			yf = self.magintudesVectores(y)

			x = np.arange(0,(len(yf)*nper),nper)
			#print("el numero final es: "+str(len(yf)*nper))
			print("la longitud de x:" + str(len(x)))
			print("la lonfitud de y: "+str(len(yf)))

			plt.plot(x,yf)
			plt.grid(True)
			plt.show()
		else:
			print("cadenas no aceptadas")
		
		
	def magintudesVectores(self,lista):	
		yf  = []
		for i in range(len(lista)):
				yf.append(np.sqrt(np.power(lista[i].real,2)+np.power(lista[i].imag,2)))

		return yf
