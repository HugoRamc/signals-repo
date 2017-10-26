import matplotlib.pyplot as plt
from matplotlib.pyplot import *
import plotly.plotly as py
import numpy as np


arreglo = [ -3. -3.j,  1. +7.j,  2. +8.j,  3. +9.j,  4.+10.j]
fig,ax = subplots()
for x in range(len(arreglo)):
	ax.scatter(arreglo[x].real,arreglo[x].imag)

#for x in range(len(arreglo)):
    #plt.plot([0,arreglo[x].real],[0,arreglo[x].imag])

plt.show()
