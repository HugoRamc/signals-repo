from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 
from validaStrings import *

class recta(object):
	
	def __init__(self):

		#self.pendiente = StringVar()

		vtnRec = Tk()
		vtnRec.title("Graficadora Recta")
		w, h = vtnRec.winfo_screenwidth()/4, vtnRec.winfo_screenheight()/4
		vtnRec.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		#ploteo de la recta usando matplotlib

		lblTitulo = Label(vtnRec,text="Introduce los valores para graficar la recta")
		lblTitulo.grid(columnspan=10,row=0)


		lblPendiente = Label(vtnRec,text="Introduce la pendiente de la recta")
		self.txtPendiente = Entry(vtnRec)

		lblPendiente.grid(column=0,row=1,sticky=E)
		self.txtPendiente.grid(column=1, row=1)


		lblOrdenada = Label(vtnRec,text="Introduce la Ordenada de la recta")
		self.txtOrdenada = Entry(vtnRec)

		lblOrdenada.grid(column=0,row=2 ,sticky=E)
		self.txtOrdenada.grid(column=1,row=2)

		lblpntInicial = Label(vtnRec,text="Introduce la pntInicial para definir el periodo")
		self.txtpntInicial = Entry(vtnRec)

		lblpntInicial.grid(column=0,row=3 ,sticky=E)
		self.txtpntInicial.grid(column=1,row=3)

		lblPeriodo = Label(vtnRec,text="Introduce la Periodo de la recta")
		self.txtPeriodo = Entry(vtnRec)

		lblPeriodo.grid(column=0,row=4 ,sticky=E)
		self.txtPeriodo.grid(column=1,row=4)

		lblSumas = Label(vtnRec,text="Introduce la Sumas de la recta")
		self.txtSumas = Entry(vtnRec)

		lblSumas.grid(column=0,row=5 ,sticky=E)
		self.txtSumas.grid(column=1,row=5)

		self.btnGrafica = Button(vtnRec,text="Graficar",command=self.pintaRecta)
		self.btnGrafica.grid(row=6,columnspan=2)

		vtnRec.mainloop()



	def pintaRecta(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		pendiente = self.txtPendiente.get()
		ordenada = self.txtOrdenada.get()
		pntInicial = self.txtpntInicial.get()
		periodo = self.txtPeriodo.get()
		sumas = self.txtSumas.get()
		valida = validaStrings()

		edo = 0
		if(valida.validaCadena(pendiente)<1):
			edo = 1
		if(valida.validaCadena(ordenada)<1):
			edo = 1
		if(valida.validaCadena(pntInicial)<1):
			edo = 1
		if(valida.validaCadena(periodo)<1):
			edo = 1
		if(valida.validaCadena(sumas)<1):
			edo = 1

		if(edo==0):

			carac = pntInicial.split("*")
			if(len(carac)>1):
				npntI = float(carac[0])*np.pi
			else:
				npntI = float(pntInicial)

			nper = valida.getValorCadena(periodo)
			npen = valida.getValorCadena(pendiente)
			nord = valida.getValorCadena(ordenada)


			pintar = graph(npntI,nper,int(sumas))
			pintar.plotRecta(npen,nord)

		