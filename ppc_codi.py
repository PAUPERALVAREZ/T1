import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf


##EXERCICI 1

##Freq = 800Hz
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=800                               # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple1.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide de fx = 800Hz')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

#FFT
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformada, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


##Freq = 4kHz
T= 2.5                               # Durada de T segons
fm=8000                              # Freqüència de mostratge en Hz
fx=4000                              # Freqüència de la sinusoide
A=4                                  # Amplitud de la sinusoide
pi=np.pi                             # Valor del número pi
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
sf.write('so_exemple2.wav', x, fm)   # Escriptura del senyal a un fitxer en format wav

Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(2)                             # Nova figura
plt.plot(t[0:Ls], x[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide de fx = 4kHz')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

#FFT
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤k<N

plt.figure(3)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformada, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


#_________________________________________________________________________________________________________________________________________________ 

##EXERCICI 2
x_r, fm = sf.read('so_exemple2.wav')      #Agafem el fitxer creat abans de freq = 4kHz


#Per trobar fx:
plt.figure(4)
plt.xlabel('Hz')
ms = plt.magnitude_spectrum(x_r, fm) 
fx = ms[1][np.argmax(ms[0])] 
print(f'La freqüència fonamental del senyal: {fx} Hz')
plt.show()

#Gràfic 5 periodes
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(5)                             # Nova figura
plt.plot(t[0:Ls], x_r[0:Ls])              # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide')   # Títol del gràfic
plt.show()                                # Visualització de l'objecte gràfic. 

#FFT
from numpy.fft import fft     # Importem la funció fft
N=5000                        # Dimensió de la transformada discreta
X=fft(x_r[0 : Ls], N)         # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤k<N

plt.figure(6)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X)))    # Representació de la fase de la transformada, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics


#_________________________________________________________________________________________________________________________________________________ 

##EXERCICI 3
#Agafem les dades de l'apartat anterior, és a dir, de 'so_exemple1.wav': fx = 800Hz 

x, fm = sf.read('so_exemple1.wav')

#Per trobar fx:
plt.figure(7)
plt.xlabel('Hz')
ms = plt.magnitude_spectrum(x, fm) 
fx = ms[1][np.argmax(ms[0])] 
print(f'La freqüència fonamental del senyal: {fx} Hz')
plt.show()

T= 2.5                               # Durada de T segons
L = int(fm * T)                      # Nombre de mostres del senyal digital
Tm=1/fm                              # Període de mostratge
t=Tm*np.arange(L)                    # Vector amb els valors de la variable temporal, de 0 a T
x = A * np.cos(2 * pi * fx * t)      # Senyal sinusoidal
Ls=int(fm*5*Tx)

N = fm
X=fft(x[0 : Ls], N)         # Càlcul de la transformada de 5 períodes de la sinusoide

#Mòdul transformada en dB:    
X_dB = 20*(np.log10(np.abs(X)/(max(np.abs(X)))))

#Càlcul de fk:
k = np.arange(N)
kk = k/N * fm

plt.figure(8)                         # Nova figura
plt.plot(kk[0:int(fm/2)],X_dB[0:int(fm/2)])                  # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]| en dB')                # Etiqueta de mòdul
plt.show()

A = 10**int(max(X_dB)/20)
print(f'Amplitud del senyal: {A}')

#_________________________________________________________________________________________________________________________________________________ 

##EXERCICI 4
import sounddevice as sd     

xx, fm = sf.read('Quevedo-WANDA.wav')
numMostres = len(xx)
print(f'''
    - Freqüència de mostratge: {fm} Hz
    - Nombre de mostres: {numMostres}
    ''')

#Inici de l'anàlisis
t0 = 40             
L1 = int(fm * t0)

#25ms després:
tf = 40.025
L2 = int(fm * tf)

Tm = 1/fm
t = Tm*np.arange(L1, L2)

plt.figure(9)
plt.title('5ms de la cançó') 
plt.plot(t, xx[L1:L2])
plt.show()

N = fm
XX = fft(xx[L1:L2], N)
kkk = ((np.arange(N))/N) * fm
XX_dB = 20*np.log10(np.abs(XX)/(max(np.abs(XX))))

plt.figure(10)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(kkk/2,XX_dB)                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={L2-L1} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]| en dB')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(kkk/2,np.unwrap(np.angle(XX_dB)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

