from tkinter import *
import tkinter.messagebox
import numpy as np
import matplotlib.pyplot as plt
from graph import * 
from scipy.fftpack import *
from validaStrings import *

class transRecta(object):
	
	def __init__(self):

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

		#lblpntInicial = Label(vtnRec,text="Introduce el pntInicial de la función")
		#self.txtpntInicial = Entry(vtnRec)

		#lblpntInicial.grid(column=0,row=3 ,sticky=E)
		#self.txtpntInicial.grid(column=1,row=3)

		lblpntFinal = Label(vtnRec,text="Introduce el punto inicial para graficar")
		self.txtpntFinal = Entry(vtnRec)

		lblpntFinal.grid(column=0,row=4 ,sticky=E)
		self.txtpntFinal.grid(column=1,row=4)

		self.btnGrafica = Button(vtnRec,text="Graficar",command=self.pintaRecta)
		self.btnGrafica.grid(row=8,columnspan=2)

		vtnRec.mainloop()



	def pintaRecta(self):
		#print("hola la pendiente es: ",self.txtPendiente.get())
		pendiente = self.txtPendiente.get()
		ordenada = self.txtOrdenada.get()
		#pntInicial = self.txtpntInicial.get()
		pntFinal = self.txtpntFinal.get()
		valida = validaStrings()
		
		edo = 0
		if(valida.validaCadena(pendiente)!=1):
			edo = 1
		if(valida.validaCadena(ordenada)!=1):
			edo = 1
		#if(valida.validaCadena(pntInicial)!=1):
		#	edo = 1
		if(valida.getValorCadena(pntFinal)>1):
			edo = 1

		if(edo ==0):
			npen = valida.getValorCadena(pendiente)
			nord = valida.getValorCadena(ordenada)
			#npntI = valida.getValorCadena(pntInicial)
			nmues = 100
			nfinal = valida.getValorCadena(pntFinal)


			w = np.linspace(nfinal-5,np.abs(nfinal)+5,nmues)
			y = (npen/np.power(w,2)) +nord/w
			

			plt.plot(w,y)
			plt.grid(True)
			plt.show()
		else:
			print("Cadenas no aceptadas")


	def magintudesVectores(self,lista):	
		yf  = []
		for i in range(len(lista)):
				yf.append(np.sqrt(np.power(lista[i].real,2)+np.power(lista[i].imag,2)))

		return yf

obj = transRecta()