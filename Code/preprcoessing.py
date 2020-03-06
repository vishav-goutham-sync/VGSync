#Data Preprocessing by Gautham (5 march 2020)

import numpy as np
from ecgdetectors import Detectors
from sklearn.preprocessing import minmax_scale
from scipy.signal import medfilt
import matplotlib.pyplot as plt

#Step-1: Normailzation
def normalization(x):
    x_n = minmax_scale(x,feature_range=(0,1), axis=0, copy=True)
    return x_n

#Step-2: Smoothening (This method is based on the convolution of a scaled window with the signal)
def smoothen(x,window_len,window):
    if x.ndim != 1:
        raise ValueError#, "smooth only accepts 1 dimension arrays."
    if x.size < window_len:
        raise ValueError#, "Input vector needs to be bigger than window size."
    if window_len<3:
        return x
    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError#, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"

    s=np.r_[x[window_len-1:0:-1],x,x[-2:-window_len-1:-1]]
    #print(len(s))
    if window == 'flat': #moving average
        w=np.ones(window_len,'d')
    else:
        w=eval('np.'+window+'(window_len)')

    y=np.convolve(w/w.sum(),s,mode='valid')
    return y

#Step-3: Baseline_Correction
def Baseline_correction(x):
    h1=medfilt(x,199) 
    h2=medfilt(h1,599)
    h3=x-h2
    return h3

#Step-4: R peak Detection
def Rpeak_detect(x):
    fs=500
    detectors = Detectors(fs)
    x_rpeaks = detectors.engzee_detector(x)
    return x_rpeaks

def overall_preprocessing(x1):
    xn=normalization(x1) # normalized signal
    xs=smoothen(xn,10,'hanning') # smoothened signal with hanning window
    xb=Baseline_correction(xs) # Baseline corrected signal
    return xb

#- main - code -------------------