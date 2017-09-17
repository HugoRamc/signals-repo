#importacion de la libreria para realizar interfaces graficas
from tkinter import *
import tkinter.messagebox
from graph import * 
from recta import *
from fSeno import *
from fCos import *
from fexp import *

w = 0
h=0


#estas cuatro funciones son para llamar a las clases que contienen los cuadros de texto para graficar la serie de fourier
def plotRecta():
	obj = recta()

def plotSen():
	obj = fSeno()

def plotCos():
	obj = fCos()

def plotExp():
	obj = fexp()


#funcion para iniciar la ventana
def ventanaInicio():
	#declaracion de la ventana
	ventana = Tk()
	#definimos los tamaños de la ventana
	w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
	ventana.geometry("%dx%d+%d+%d" % (600, 400,w,h))


	ventana.title("Graficadora Fourier")

	#declaracion de los botones para hacer un llamado a las clases que tendrán las interfaces y los botones
	btnRecta = Button(ventana,text="Recta",command=plotRecta)
	btnRecta.place(x=100,y=50)

	btnPar = Button(ventana,text="e^x",command=plotExp)
	btnPar.place(x=200,y=50)

	btnSin = Button(ventana,text="Sin function",command=plotSen)
	btnSin.place(x=100,y=200)

	btnCos = Button(ventana,text="Cos function",command=plotCos)
	btnCos.place(x=200,y=200)

	



	ventana.mainloop()


#funcion main
if __name__ == '__main__':
	ventanaInicio()