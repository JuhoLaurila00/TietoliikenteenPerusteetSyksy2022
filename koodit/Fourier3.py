import numpy as np
import matplotlib.pyplot as plt

j=complex(0,1)
taajuustaso = np.zeros(100,dtype=complex)
taajuustaso[3] = 10+10*j
taajuustaso[15] = 1+j
aikataso = np.fft.ifft(taajuustaso)

plt.figure(1)
plt.subplot(2,1,1),plt.stem(aikataso.real),plt.title('Real Part')
plt.subplot(2,1,2),plt.stem(aikataso.imag),plt.title('Imaginary Part')
plt.show()