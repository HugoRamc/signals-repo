from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 


class fSeno(object):
	
	def __init__(self):

		#self.pendiente = StringVar()

		ventana = Tk()
		ventana.title("Graficadora Función sen(t)")
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(ventana,text="Introduce los valores para graficar la la función sen(t)")
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

		lblpntInicial = Label(ventana,text="Introduce el pntInicial del periodo")
		self.txtpntInicial = Entry(ventana)
		lblpntInicial.grid(column=0,row=4 ,sticky=E)
		self.txtpntInicial.grid(column=1,row=4)

		lblPeriodo = Label(ventana,text="Introduce el Periodo")
		self.txtPeriodo = Entry(ventana)
		lblPeriodo.grid(column=0,row=5 ,sticky=E)
		self.txtPeriodo.grid(column=1,row=5)

		lblSumas = Label(ventana,text="Introduce la cantidad de iteraciones de la serie")
		self.txtSumas = Entry(ventana)
		lblSumas.grid(column=0,row=6 ,sticky=E)
		self.txtSumas.grid(column=1,row=6)

		self.btnGrafica = Button(ventana,text="Graficar",command=self.pintaSeno)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()



	def pintaSeno(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		amplitud = self.txtAmplitud.get()
		frecuencia = self.txtFrecuencia.get()
		ordenada = self.txtOrdenada.get()
		pntInicial = self.txtpntInicial.get()
		periodo = self.txtPeriodo.get()
		sumas = self.txtSumas.get()

		pintar = graph(float(pntInicial)*np.pi,float(periodo)*np.pi,int(sumas))
		pintar.plotSen(float(amplitud),float(frecuencia),float(ordenada))

		