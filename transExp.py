from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import *
from validaStrings import *

class transExp(object):
	
	def __init__(self):


		ventana = Tk()
		ventana.title("Graficadora función Exponencial")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Introduce los valores para graficar la la función e^x")
		lblTitulo.grid(columnspan=10,row=0)


		lblAmplitud = Label(ventana,text="Introduce la Amplitud")
		self.txtAmplitud = Entry(ventana)
		lblAmplitud.grid(column=0,row=1,sticky=E)
		self.txtAmplitud.grid(column=1, row=1)

		lblFrecuencia = Label(ventana,text="Introduce la Frecuencia")
		self.txtFrecuencia = Entry(ventana)
		lblFrecuencia.grid(column=0,row=2 ,sticky=E)
		self.txtFrecuencia.grid(column=1,row=2)

		lblOrdenada = Label(ventana,text="Introduce la Ordenada")
		self.txtOrdenada = Entry(ventana)
		lblOrdenada.grid(column=0,row=3 ,sticky=E)
		self.txtOrdenada.grid(column=1,row=3)

		lblpntFinal = Label(ventana,text="Introduce el punto inicial para graficar")
		self.txtpntFinal = Entry(ventana)

		lblpntFinal.grid(column=0,row=4 ,sticky=E)
		self.txtpntFinal.grid(column=1,row=4)

		#lblperiodo = Label(ventana,text="Introduce el periodo de muestreo")
		#self.txtPeriodo = Entry(ventana)

		#lblperiodo.grid(column=0,row=6 ,sticky=E)
		#self.txtPeriodo.grid(column=1,row=6)


		self.btnGrafica = Button(ventana,text="Graficar",command=self.pintaExp)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def pintaExp(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		edo = 0
		amplitud = self.txtAmplitud.get()
		frecuencia = self.txtFrecuencia.get()
		ordenada = self.txtOrdenada.get()
		pntIni = self.txtpntFinal.get()

		valida = validaStrings()
		if(valida.validaCadena(amplitud)<1):
			edo = 1
		if(valida.validaCadena(frecuencia)<1):
			edo = 1
		if(valida.validaCadena(ordenada)<1):
			edo = 1
		if(valida.validaCadena(pntIni)<1):
			edo = 1

		if edo == 0:
			namp = valida.getValorCadena(amplitud)
			nfrec = valida.getValorCadena(frecuencia)
			nord = valida.getValorCadena(ordenada)
			npntI = int(valida.getValorCadena(pntIni))
			nmues = 200

			w = np.linspace(npntI-5,(np.abs(npntI)+5),nmues)
			#y = w
			y = (namp*(np.exp(nfrec)/np.sqrt((np.power(w,2)+np.power(nfrec,2))))) + nord/w
			#yf = fft(y)

			#ym = self.magintudesVectores(yf)

			plt.plot(w,y)
			plt.grid(True)
			plt.show()
		else:
			print("cadena no aceptada")

	
	def magintudesVectores(self,lista):	
		yf  = []
		for i in range(len(lista)):
				yf.append(np.sqrt(np.power(lista[i].real,2)+np.power(lista[i].imag,2)))

		return yf

#obj = transExp()