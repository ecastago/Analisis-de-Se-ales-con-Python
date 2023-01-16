import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from celluloid import Camera

def mandelbrot(real, im, max_iter):
    c = complex(re,im)
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if(z.real*z.real +z.imag*z.imag) >= 4:
            return i
    return max_iter
    
columnas = 5000
filas = 5000

plano_imag = np.zeros([columnas,filas])

for indice_fila, re in enumerate(np.linspace(-2,1,num=filas)):
    for indice_columna, im in enumerate(np.linspace(-1,1,num=columnas)):
        plano_imag[indice_columna,indice_fila] = mandelbrot(re,im,100)

plt.figure(dpi=100)
plt.imshow(plano_imag, cmap='viridis', extent=[-2,1,-1,1])
plt.show()