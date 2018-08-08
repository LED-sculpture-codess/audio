import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, fftshift


rate ,data = wav.read('file_example_WAV_1MG.wav')    #reading the data using scipy.io.wavfile module
nframe = data.shape[0] 		#no of frames in the audio file
x = np.arange(nframe)
T = 1/rate
#print(data)				#time diff between two samples
xf = fftfreq(nframe, T)     
print(xf)
yf = fft(data)
yf = np.abs(yf)     #from data it is removing imaginary part of the data
print(yf)
plt.plot(xf,yf)
plt.show()


#incase of wav file having two channels use this for plotting
'''
plt.subplot(211)
plt.plot(xf,yf[:,0])
plt.subplot(212)
plt.plot(xf,yf[:,1])
plt.show()
'''
