import numpy as np
import matplotlib.pyplot as plt

Fs=1000; Ts=1/Fs; t=np.arange(0,1,Ts)
s1 = np.sin(2 * np.pi * 1 * t)
s2 = (1/3)*np.sin(2 * np.pi *3* t)
s3 = (1/5)*np.sin(2 * np.pi *5* t)
s4 = (1/7)*np.sin(2 * np.pi *7* t)
s5 = (1/9)*np.sin(2 * np.pi *9* t)
summa = s1+s2+s3+s4+s5

N = len(t)

df = int(Fs/N)
print("Taajuusresoluutio on nyt = ", df)

F1 = (np.fft.fft(summa))/N

F1posit = F1[0:int(N/2)+1]
fakseli = np.arange(0,int(Fs/2)+df,df)
print("fakseli shape = ", fakseli.shape)
print("F1posit shape = ", F1posit.shape)


plt.figure(1)
plt.subplot(2,2,1),plt.plot(t,summa),plt.title('Aikatason Signaali')
plt.subplot(2,2,2),plt.plot(fakseli,F1posit.real),plt.title('Real Part')
plt.subplot(2,2,3),plt.plot(fakseli,F1posit.imag),plt.title('Imaginary Part')
plt.subplot(2,2,4),plt.plot(fakseli,abs(F1posit)),plt.title('abs real+imag')
plt.show()