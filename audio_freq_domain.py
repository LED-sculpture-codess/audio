import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift


rate ,data = wav.read('1kHz_44100Hz_16bit_05sec.wav')    #reading the data using scipy.io.wavfile module
nframe = data.shape[0] 		#no of frames in the audio file
print(data)
T = 1/rate	#time diff between two samples
dt = 0.005
nsamp = int((dt)/T)
print(nsamp)
for i in np.arange(0,nframe,nsamp):	
	d = data[i:(i+nsamp)]	
	plt.hold(True)
	plt.clf()
	plt.subplot(211)
	plt.plot(d)
	f = fftfreq(nsamp, T)     
	print(f)
	Y = fft(d)
	Y = np.abs(Y)     #from data it is removing imaginary part of the data
	print(Y)
	plt.subplot(212)
	plt.plot(f,Y)
	plt.pause(0.01)
	plt.hold(False)
