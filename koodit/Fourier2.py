import numpy as np
import matplotlib.pyplot as plt

N = 100
j = complex(0,1)
k = 0
n = np.arange(0,N,1)
v0 = np.exp(-j*(2*np.pi*k*n)/N)
k = 90
v1 = np.exp(-j*(2*np.pi*k*n)/N)

plt.figure(1)
plt.subplot(6,1,1),plt.stem(v0),plt.title('Eka Vertailusignaali')
plt.subplot(6,1,2),plt.stem(v1.real),plt.title('Toka cos part')
plt.subplot(6,1,3),plt.stem(v1.imag),plt.title('toka sin part')
plt.show()