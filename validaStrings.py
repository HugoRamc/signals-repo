import numpy as np
class validaStrings(object):
	"""docstring for validaString"""
	def __init__(self):
		pass

	def validaCadena(self,cadena):
		edo=1
		if cadena == "inf" or cadena == "-inf":
			return 2
		else:
			for i in range(len(cadena)):
				if edo == 0:
					break
				elif edo == 1:
					if(ord(cadena[i])>=48 and ord(cadena[i])<=57):
						edo = 2
					elif(cadena[i]=='p' or cadena[i]=='P'):
						i = i+1
						if(cadena[i]=='i' or cadena[i]== 'I'):
							edo = 4
						else:
							edo = 0
					elif(cadena[i]=='+' or cadena[i]=='-'):
						edo = 5
					else:
						edo = 1
				elif edo == 2:
					if(ord(cadena[i])>=48 and ord(cadena[i])<=57):
						edo = 2
					elif(cadena[i]=='*' ):
						edo = 3
					elif(cadena[i]=='.'):
						edo = 7
					else:
						edo = 0
				elif edo == 3:
					if(cadena[i]=='p' or cadena[i]=='P'):
						i = i+1
						if(cadena[i]=='i' or cadena[i]== 'I'):
							edo = 4
						else:
							edo = 0
					else:
						edo = 0
				elif edo == 4:
					edo = 6
				elif edo == 5:
					if(ord(cadena[i])>=48 and ord(cadena[i])<=57):
						edo = 2
					elif(cadena[i]=='p' or cadena[i]=='P'):
						i = i+1
						if(cadena[i]=='i' or cadena[i]== 'I'):
							edo = 4
						else:
							edo = 0
					else:
						edo = 0
				elif edo == 6:
					edo = 0
				elif edo== 7:
					if(ord(cadena[i])>=48 and ord(cadena[i])<=57):
						edo = 2
					else:
						edo = 0
			if (edo == 2 or edo == 6):
				return 1
			else:
				print("cadena no aceptada")
				return 0

		

	def getValorCadena(self,cadena):
		salida = 0.0
		##dado a la gramatica de solo se pueden tener cadenas que tengan el formato "num*pi" o "num"
		
		aux = cadena.split("*")
			#si se realizó el split, indica que el usuario escribió pi como parámetro, por lo que 
		if (len(aux)>1):
			salida = float(aux[0])*np.pi
		else:
			salida = float(cadena)
		return salida		

#obj = validaStrings()
#val = obj.validaCadena("0.1")
#val1 = obj.getValorCadena("0.1")
#print("La cadena es: "+str((val1)))
		