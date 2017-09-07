#importacion de la libreria para realizar interfaces graficas
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

w = 0
h=0
def plotRecta():

	vtnRec = Tk()
	vtnRec.title("Graficadora Recta")
	w, h = vtnRec.winfo_screenwidth()/4, vtnRec.winfo_screenheight()/4
	vtnRec.geometry("%dx%d+%d+%d" % (600, 400,w,h))
	#ploteo de la recta usando matplotlib



	txtAmplitud = Text(vtnRec, height=1, width=10)
	txtAmplitud.place(x=5,y=40)
	txtAmplitud.pack();

	txtFrecuencia = Text(vtnRec, height=1, width=10)
	txtFrecuencia.place(x=5,y=40)
	txtFrecuencia.pack();

	txtpntInicial = Text(vtnRec, height=1, width=10)
	txtpntInicial.place(x=5,y=40)
	txtpntInicial.pack();

	txtPeriodo = Text(vtnRec, height=1, width=10)
	txtPeriodo.place(x=5,y=40)
	txtPeriodo.pack();

	txtIteraciones = Text(vtnRec, height=1, width=10)
	txtIteraciones.place(x=5,y=40)
	txtIteraciones.pack();

	txtpendiente = Text(vtnRec, height=1, width=10)
	txtpendiente.place(x=0,y=200)
	txtpendiente.pack();

	txtOrdenada = Text(vtnRec, height=1, width=10)
	txtOrdenada.place(x=5,y=40)
	txtOrdenada.pack();





	vtnRec.mainloop()


#funcion para iniciar la ventana
def ventanaInicio():
	#declaracion de la ventana
	ventana = Tk()

	w, h = ventana.winfo_screenwidth()/4, ventana.winfo_screenheight()/4
	ventana.geometry("%dx%d+%d+%d" % (600, 400,w,h))


	ventana.title("Graficadora Fourier")

	#declaracion de un elemento de tipo etiqueta
	#etiqueta = Label(ventana,text="Hola mundirri")
	#etiqueta.pack()


	#declaracion de los botones para 
	btnRecta = Button(ventana,text="Recta",command=plotRecta)
	btnRecta.place(x=100,y=50)

	btnPar = Button(ventana,text="Parabola Function")
	btnPar.place(x=200,y=50)

	btnSin = Button(ventana,text="Sin function")
	btnSin.place(x=100,y=200)

	btnCos = Button(ventana,text="Cos function")
	btnCos.place(x=200,y=200)

	



	ventana.mainloop()


#funcion main
if __name__ == '__main__':
	ventanaInicio()