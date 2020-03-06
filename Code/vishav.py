# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:34:10 2020

@author: Vishavpreet
"""
import numpy as np
from load_data import load_from_folder
from Segmentation import ECG_segment
from biosppy.signals.ecg import ecg

dataset=load_from_folder()
s,apd,arp=ECG_segment(dataset,channel_num=0)

#Feature Extraction
signal=apd[9]
fs=500
ts,filtered,rpeaks,templates_ts, templates, heart_rate_ts, heart_rate=ecg(signal=signal, sampling_rate=fs, show=True)

import matplotlib.pyplot as plt
plt.plot(templates.T)