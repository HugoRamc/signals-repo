from tkinter import *
import numpy as np
from scipy.fftpack import fft,ifft

class serieDFourier(object):
	"""docstring for serieDFourier"""

	def calcularSerie(self):
		print("Serie discreta")

	def __init__(self):
		self.muestras = ""
		ventana = Tk()
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (500, 250,w,h))
		lblTitulo = Label(ventana,text="Introduce los valores de la función separados por comas")
		lblTitulo.grid(columnspan=10,row=0)

		lblAmplitud = Label(ventana,text="Introduce la Amplitud")
		self.txtAmplitud = Entry(ventana)
		lblAmplitud.grid(column=0,row=1,sticky=E)
		self.txtAmplitud.grid(column=1, row=1)

		self.btnGrafica = Button(ventana,text="Graficar",command=self.calcularSerie)
		self.btnGrafica.grid(row=7,columnspan=2)

		ventana.mainloop()
		
#obj = serieDFourier()