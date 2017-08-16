#importacion de la libreria para realizar interfaces graficas
from tkinter import *

def plotRecta():

	vtnRec = Tk()
	vtnRec.title("Graficadora Recta")

	vtnRec.mainloop()


#funcion para iniciar la ventana
def ventanaInicio():
	#declaracion de la ventana
	ventana = Tk()
	ventana.title("Graficadora Fourier")

	#declaracion de un elemento de tipo etiqueta
	etiqueta = Label(ventana,text="Hola mundirri")
	etiqueta.pack()


	#declaracion de los botones para 
	btnRecta = Button(ventana,text="Recta",command=plotRecta)
	btnRecta.pack()

	btnSin = Button(ventana,text="Sin function")
	btnSin.pack()

	btnCos = Button(ventana,text="Cos function")
	btnCos.pack()

	btnPar = Button(ventana,text="Parabola Function")
	btnPar.pack()



	ventana.mainloop()


#funcion main
if __name__ == '__main__':
	ventanaInicio()