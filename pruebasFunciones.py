import scipy.integrate as integrate
import scipy.special as special

result = integrate.quad(lambda x: x, 0, 5)

#print("El resultado de la integral es: "+result)
print(result[0])