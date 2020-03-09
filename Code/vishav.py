# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:34:10 2020

@author: Vishavpreet
"""
import numpy as np
import time
import os
from load_data import load_from_folder,read_annotations
from Segmentation import ECG_segment
from biosppy.signals.ecg import ecg
import matplotlib.pyplot as plt

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

dataset=load_from_folder()
def saveData(c_num):
    start=time.time()
    s,apd,arp=ECG_segment(dataset,channel_num=c_num)
    annotations=read_annotations()
    end=time.time()
    duration=end-start
    print(""+str(duration))
    #Feature Extraction
    
    for i in range(len(apd)):
        print(i)
        signal=apd[i]
        fs=500
        ts,filtered,rpeaks,templates_ts, templates, heart_rate_ts, heart_rate=ecg(signal=signal, sampling_rate=fs, show=False)
        plt.axis('off')
        plt.plot(templates.T)
        ensure_dir('G:/Vishav/TestData/CinC2020imagedata/patient_templates_'+str(c_num)+'/'+annotations[i]+'/')
        plt.savefig('G:/Vishav/TestData/CinC2020imagedata/patient_templates/'+annotations[i]+'/'+str(i))
        plt.clf()

for i in range(12):
    saveData(i)