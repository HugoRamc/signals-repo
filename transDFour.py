from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 


class transDFour(object):
	
	def __init__(self):

		#self.pendiente = StringVar()

		ventana = Tk()
		ventana.title("Graficadora Función cos(t)")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Transformada Discreta de Fourier")
		lblTitulo.grid(columnspan=10,row=0)


		lblAmplitud = Label(ventana,text="Introduce las muestras de la Función separadas por comas")
		self.txtAmplitud = Entry(ventana)
		lblAmplitud.grid(column=0,row=1,sticky=E)
		self.txtAmplitud.grid(column=1, row=1)

		
		self.btnGrafica = Button(ventana,text="Graficar",command=self.calculaTrans)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def calculaTrans(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		amplitud = self.txtAmplitud.get()
		
		#pintar = graph(float(pntInicial)*np.pi,float(periodo)*np.pi,int(sumas))
		#pintar.plotCos(float(amplitud),float(frecuencia),float(ordenada))

obj = transDFour()