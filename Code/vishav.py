# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:34:10 2020

@author: Vishavpreet
"""
import numpy as np
import time
from load_data import load_from_folder
from Segmentation import ECG_segment
from biosppy.signals.ecg import ecg
import matplotlib.pyplot as plt


dataset=load_from_folder()
start=time.time()
s,apd,arp=ECG_segment(dataset[0:100],channel_num=0)
end=time.time()
duration=end-start
print(""+str(duration))
#Feature Extraction
for i in range(len(apd)):
    signal=apd[i]
    fs=500
    ts,filtered,rpeaks,templates_ts, templates, heart_rate_ts, heart_rate=ecg(signal=signal, sampling_rate=fs, show=False)
    plt.axis('off')
    plt.plot(templates.T)
    plt.savefig('G:/Vishav/TestData/CinC2020imagedata/patient_templates_'+str(i))
    plt.clf()