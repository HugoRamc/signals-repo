
from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from validaStrings import *

class transCos(object):
	
	def __init__(self):

		#self.pendiente = StringVar()
		
		ventana = Tk()
		ventana.title("Transformada Función cos(t)")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Introduce los valores para graficar la Transformada de la función cos(t)")
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




		self.btnGrafica = Button(ventana,text="Graficar",command=self.pintaCos)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def pintaCos(self):
		edo = 0
		amplitud = self.txtAmplitud.get()
		frecuencia = self.txtFrecuencia.get()
		ordenada = self.txtOrdenada.get()
		pntFin = self.txtpntFinal.get()
		#hacemos un llamado a la clase para validar las cadenas

		valida = validaStrings()
		if(valida.validaCadena(amplitud)<1):
			edo = 1
		if(valida.validaCadena(frecuencia)<1):
			edo = 1
		if(valida.validaCadena(ordenada)<1):
			edo = 1
		if(valida.validaCadena(pntFin)<1):
			edo = 1

		if edo == 0:
			namp = valida.getValorCadena(amplitud)
			nfrec = valida.getValorCadena(frecuencia)
			nord = valida.getValorCadena(ordenada)
			npntF = valida.getValorCadena(pntFin)
			nmues = 200

			w = np.linspace(npntF-5,np.abs(npntF)+5,nmues)
			y = namp*(1/2)*(w/(np.power(w,2)-np.power(nfrec,2)))+ nord/w

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
		

