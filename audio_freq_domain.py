import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift


rate ,data = wav.read('file_example_WAV_1MG.wav')    #reading the data using scipy.io.wavfile module
nframe = data.shape[0] 		#no of frames in the audio file
print(data)
T = 1/rate	#time diff between two samples
dt = 0.05       #sample timewidth for window of shortFFT
nsamp = int((dt)/T)   #no of sample taken in one window
print(nsamp)
for i in np.arange(0,nframe,nsamp):	#loop for drawing graph of each window
	d = data[i:(i+nsamp)]	
	plt.hold(True)         #draw the graph in the background
	plt.clf()
	plt.subplot(211)
	plt.plot(d)
	f = fftfreq(nsamp, T)     
	print(f)
	Y = fft(d)
	Y = fftshift(Y)		#used for converting array from [0, ...(n/2 - 1),...  (-n/2)] to [(-n/2).....,0,.....(n/2-1)]	
	f = fftshift(f)
	Y = np.abs(Y)     #from data it is removing imaginary part of the data
	print(Y)
	plt.subplot(212)
	plt.plot(f,Y)
	plt.pause(0.01)
	plt.hold(False)    #shows the data now
