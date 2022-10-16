import numpy as np
import matplotlib.pyplot as plt

taajuustaso = np.zeros((128),dtype=complex)
j = complex(0,1)
taajuustaso[3] = 1+j;  # Tässä on nyt moduloitu yksi alikantoaalto
# Moduloi tähän myös alikantoaallot 10 ja 30 QPSK-modulaatiota käyttäen
# Eli tarkoittaa siis sitä, että sinulla on käytettävissäsi 00 => 1+j, 11 => -1-j, 01 => -1+j ja 
# 10 => 1-j vaihtoehdot.
taajuustaso[10] = -1+j
taajuustaso[30] = 1-j

print(taajuustaso[:])

aikataso = np.fft.ifft(taajuustaso[:]);
print(aikataso.real)
print(aikataso.imag)

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(aikataso.real)
plt.title('Moduloidun signaalin kosinihaara')
plt.subplot(3,1,2)
plt.plot(aikataso.imag)
plt.title('Moduloidun signaalin sinihaara')


# Ja tänne pitäisi opiskelijan sitten osata tehdä bittipäätökset
# Eli sinun pitää tulla aikatason signaalista takaisin taajuustasoon
# ja tehdä bittipäätökset alikantoaaltojen 3, 10, 30 osalta.

taso = np.fft.ifft(aikataso)

if(taso[3] > 0):
    print("Alikantoaalto 3 bitti on 1")
if(taso[3] < 0):
    print("Alikantoaalto 3 bitti on 0")

if(taso[10] > 0):
    print("Alikantoaalto 10 bitti on 1")
if(taso[10] < 0):
    print("Alikantoaalto 10 bitti on 0")

if(taso[30] > 0):
    print("Alikantoaalto 30 bitti on 1")
if(taso[30] < 0):
    print("Alikantoaalto 30 bitti on 0")

plt.subplot(3,1,3)
plt.plot(taso)
plt.title('Tajuustason bitit')
plt.show()