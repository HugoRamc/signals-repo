from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 
from scipy.fftpack import fft, ifft
from validaStrings import *

class serieDFourier(object):
	
	def __init__(self):

		#self.pendiente = StringVar()
		
		ventana = Tk()
		ventana.title("Calcular Serie Discreta de Fourier")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (400, 180,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Transformada Discreta de Fourier")
		lblTitulo.grid(columnspan=10,row=0)


		lblMuestras = Label(ventana,text="Introduce las muestras de la Función separadas por comas")
		self.txtMuestras = Entry(ventana)
		lblMuestras.grid(column=0,row=1,sticky=E)
		self.txtMuestras.grid(column=0, row=2)

		lblPeriodo = Label(ventana,text="Introduce el periodo de muestreo")
		self.txtMuestreo = Entry(ventana)
		lblPeriodo.grid(column=0,row=3,sticky=E)
		self.txtMuestreo.grid(column=0, row=4)
		
		self.btnGrafica = Button(ventana,text="Graficar",command=self.calculaSerie)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def calculaSerie(self):
		#obtenemos los valores del usuario que introdujo en las cajas de texto
		muestras = self.txtMuestras.get()
		muestreo = self.txtMuestreo.get()
		#ponemos en una lista los valores de la funcion
		lista = muestras.split(",")
		listanums = []
		#realizamos la validacion de las cadenas que introdujo el usuario
		valida = validaStrings()
		edo = 0
		for i in range(len(lista)):
			if(valida.validaCadena(lista[i])==1):

				listanums.append(valida.getValorCadena(lista[i]))
			else:
				edo = 1

		if valida.validaCadena(muestreo)==1:
			nper = float(valida.getValorCadena(muestreo))		
		else:
			edo = 1
		
		if edo == 0:
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
		# ya obtenidas las muestras obtener la transformada discreta de fourier
		
	def magintudesVectores(self,lista):	
		yf  = []
		for i in range(len(lista)):
				yf.append(np.sqrt(np.power(lista[i].real,2)+np.power(lista[i].imag,2)))

		return yf
