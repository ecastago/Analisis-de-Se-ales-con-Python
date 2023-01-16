import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from celluloid import Camera

plt.style.use('seaborn')

def fourier_onda_cuadrada(x,n):
    m = 2*n-1
    f = (4/np.pi)*(1/m)*np.sin(m*np.pi*x/L)
    return f
    
fig = plt.figure()
camera = Camera(fig)

L = np.pi
ciclos = 1

x = np.linspace(-0.001,2*ciclos*L,1000)

f = 0
n = 1
n_total = 100

while n<n_total:
    f += fourier_onda_cuadrada(x,n)
    plt.plot(x,f,c="tab:orange")
    if(n%10):
        camera.snap()
    n += 1
    
#plt.plot(x,f)
    
plt.plot(x,signal.square(x),color='k')
animation = camera.animate()
animation.save('fourier.gif')