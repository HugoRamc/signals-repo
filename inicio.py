from tkinter import *
from serieFourierContinua import *
class inicio(object):
		
	def serieCFourier(self):
		print("Serie continua de fourier")
		obj = serieFourierContinua()

	def serieDFourier(self):
		print("Serie discreta de fourier")

	def transCFourier(self):
		print("Transformada continua de fourier")

	def transDFourier(self):
		print("Transformada discreta de fourier")

	def redirige(self):
		#print("Estas redirigiendo")

		print("El valor de la variable1 es: "+str(self.var.get()))
		print("El valor de la variable2 es: "+str(self.var2.get()))

		if(self.var.get()==1):
			if(self.var2.get()==1):
				self.serieCFourier()
			elif(self.var2.get()==1):
				self.transCFourier()
			else:
				print("Elige una opcion entre Transformada o Serie")

		elif(self.var.get()==2):
			if(self.var2.get()==1):
				self.serieDFourier()
			elif(self.var2.get()==1):
				self.transDFourier()
			else:
				print("Elige una opcion entre Transformada o Serie")
		else:
			print("selecciona una opcion de tiempo")

	def __init__(self):
		self.ventInicio = Tk()
		w, h = self.ventInicio.winfo_screenwidth()/4, self.ventInicio.winfo_screenheight()/4
		self.ventInicio.geometry("%dx%d+%d+%d" % (600, 400,w,h))
		self.ventInicio.title("Graficadora Fourier")
		lblTitulo = Label(self.ventInicio,text="Selecciona los valores para iniciar ")
		lblTitulo.grid(column=11,row=0)
		#poner los check buttons

		self.var = IntVar()
		self.c = Radiobutton(self.ventInicio,text="Tiempo Continuo",value=1,variable = self.var)
		self.c2 = Radiobutton(self.ventInicio,text="Tiempo Discreto",value = 2,variable = self.var)

		self.c.grid(column=10,row=3)
		self.c2.grid(column=11,row=3)

		self.var2 = IntVar()
		self.c3 = Radiobutton(self.ventInicio,text="Serie de Fourier",value=1,variable = self.var2)
		self.c4 = Radiobutton(self.ventInicio,text="Transformada de Fourier",value = 2,variable = self.var2)

		self.c3.grid(column=10,row=5)
		self.c4.grid(column=11,row=5)

		self.btnAceptar = Button(self.ventInicio,text="Aceptar",command=self.redirige)
		self.btnAceptar.grid(column=10,row=6)
		self.ventInicio.mainloop()

	
		
init = inicio()


	





	
