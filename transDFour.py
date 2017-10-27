from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 
from scipy.fftpack import fft, ifft


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
		
		self.btnGrafica = Button(ventana,text="Graficar",command=self.calculaTrans)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def calculaTrans(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		#espacio = self.txtespacio.get()
		muestras = self.txtMuestras.get()
		lista = muestras.split(",")
		listanums = []
		for i in range(len(lista)):
			listanums.append(float(lista[i]))

		#teniendo las muestras procedemos a calcular la transformada discreta de fourier
		#x = np.linspace(-10,10,float(espacio))

		y =  fft(lista)
		#esta funcion nos regresa un arreglo de números complejos, el la linea que sigue se hace el proceso de graficación
		fig,ax = plt.subplots()
		for i in range(len(y)):
			ax.scatter(y[i].real,y[i].imag)
		plt.suptitle("Transformada Discreta de Fourier para: "+str(len(lista))+" muestras")
		plt.grid()
		plt.show()

		# ya obtenidas las muestras obtener la transformada discreta de fourier
		
		
		

#obj = transDFour()