# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:34:10 2020

@author: Vishavpreet
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from glob import glob
import wfdb
from ecgdetectors import Detectors


# sampling frequency
fs=500


path='G:/Github/TestCode/CinC2020/data'

def get_records():
    """ Get paths for data in directory """  
    os.path.dirname(path)
    paths = glob(path+'/*.hea')
    return paths

def make_dataset(records):
    """ Inside an array """
    dataset=[]
    for file_path in (records):        
        file_path=file_path.replace('.hea','')
        record = wfdb.io.record.rdsamp(file_path)
        dataset.append(record)
    return dataset

def ecg_features(all_segments):
    f_vec=[]
    #correlate    
    for i in range(len(all_segments)-1):
        d1=all_segments[i]
        d2=all_segments[i+1]
        corr.append(np.correlate(d1,d2))
    avgCorr=np.average(corr)
    
    f_vec.append(avgCorr)
    #mean all segments
    segment_mean=[]
    for segment in all_segments[0:5]:
        segment_mean.append(np.mean(segment))
    for m in segment_mean:
        f_vec.append(m)
        
    #Std
    std_mean=[]
    for segment in all_segments[0:5]:
        std_mean.append(np.std(segment))
    for s in std_mean:
        f_vec.append(s)
    return f_vec


#1. Read Data
def ECG_segment_and_features(channel_num=0):
    records=get_records()
    dataset=make_dataset(records)
    segments_per_ECG=[]
    features=[]
    for rec in dataset:
        ecg_all_channel=rec[0]
        ecg_channel_1=ecg_all_channel[:,0]
        detectors=Detectors(fs)
        r_peaks=detectors.engzee_detector(ecg_channel_1)
        all_segments=[]
        count=0
        for i in range(len(r_peaks)):
            data_segment=np.zeros((1,500),dtype=float)
            data_segment=data_segment.ravel()
            
            if((r_peaks[i]-250)>=0 and (r_peaks[i]+250)<len(ecg_channel_1)):
                data_segment=ecg_channel_1[r_peaks[i]-250:r_peaks[i]+250]
                count=count+1
            elif((r_peaks[i]-250)<0):
                    nZeros=250-r_peaks[i]
                    data_segment[nZeros:500]=ecg_channel_1[0:r_peaks[i]+250]
                    count=count+1
            elif(r_peaks[i]+250>len(ecg_channel_1)):
                nZeros=r_peaks[i]+250-len(ecg_channel_1)
                data_segment[0:500-nZeros]=ecg_channel_1[r_peaks[i]-250:len(ecg_channel_1)]
                count=count+1
            all_segments.append(data_segment)

        features.append(ecg_features(all_segments))
        segments_per_ECG.append(all_segments)
        
    return segments_per_ECG, features

s,f=ECG_segment_and_features(0)


#read one channel ECG
#rec_num_1=dataset[0]
#ecg_all_channel=rec_num_1[0]
#ecg_channel_1=ecg_all_channel[:,0]
#
##detect peak
#detectors=Detectors(fs)
#r_peaks=detectors.engzee_detector(ecg_channel_1)
#
##segment beats
#all_segments=[]
#count=0
#for i in range(len(r_peaks)):
#    data_segment=np.zeros((1,500),dtype=float)
#    data_segment=data_segment.ravel()
#    
#    if((r_peaks[i]-250)>=0 and (r_peaks[i]+250)<len(ecg_channel_1)):
#        data_segment=ecg_channel_1[r_peaks[i]-250:r_peaks[i]+250]
#        count=count+1
#    elif((r_peaks[i]-250)<0):
#            nZeros=250-r_peaks[i]
#            data_segment[nZeros:500]=ecg_channel_1[0:r_peaks[i]+250]
#            count=count+1
#    elif(r_peaks[i]+250>len(ecg_channel_1)):
#        nZeros=r_peaks[i]+250-len(ecg_channel_1)
#        data_segment[0:500-nZeros]=ecg_channel_1[r_peaks[i]-250:len(ecg_channel_1)]
#        count=count+1
#    all_segments.append(data_segment)