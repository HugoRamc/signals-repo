from tkinter import *
import numpy as np
from scipy.fftpack import fft,ifft
from transCos import *

class transCFourier(object):


	def __init__(self):
		self.ventanaInicio()

	#estas cuatro funciones son para llamar a las clases que contienen los cuadros de texto para graficar la serie de fourier
	def plotRecta(self):
		#obj = recta()
		pass

	def plotSen(self):
		pass
		#obj = fSeno()

	def plotCos(self):
		obj = transCos()

	def plotExp(self):
		pass
		#obj = fexp()


#funcion para iniciar la ventana
	def ventanaInicio(self):
		#declaracion de la ventana
		w = 0
		h=0
		ventana = Tk()
		#definimos los tamaños de la ventana
		w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
		ventana.geometry("%dx%d+%d+%d" % (600, 400,w,h))


		ventana.title("Graficadora Fourier")

		#declaracion de los botones para hacer un llamado a las clases que tendrán las interfaces y los botones
		btnRecta = Button(ventana,text="Recta",command=self.plotRecta)
		#image = ImageTk.PhotoImage(file="graficadora\\recta.png")
		#btnRecta.config(image=image)
		#btnRecta.image = image
		btnRecta.place(x=100,y=50)

		btnPar = Button(ventana,text="e^x",command=self.plotExp)
		btnPar.place(x=200,y=50)

		btnSin = Button(ventana,text="Sin function",command=self.plotSen)
		btnSin.place(x=100,y=200)

		btnCos = Button(ventana,text="Cos function",command=self.plotCos)
		btnCos.place(x=200,y=200)

		ventana.mainloop()


obj = transCFourier()