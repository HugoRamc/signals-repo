from scipy.fftpack import fft
import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft

def magintudesVectores(lista):	
		yf  = []
		for i in range(len(lista)):
				yf.append(np.sqrt(np.power(lista[i].real,2)+np.power(lista[i].imag,2)))

		return yf

n = 500.0
mues = 0.5
x = np.linspace(0,float(float(n)/float(mues)),n)
y = np.sin(x)
yf = fft(y)

ym = magintudesVectores(yf)
plt.plot(x,ym)
plt.grid()
plt.show()

print("el valor de la division es"+str(n/mues))
