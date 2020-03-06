#Segmentation done by Vishav
#Preprocessing by Gautham

import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from glob import glob
import wfdb
from ecgdetectors import Detectors

from preprcoessing import overall_preprocessing
from load_data import load_from_folder

fs=500
#def ecg_features(all_segments):
#    f_vec=[]
#    corr=[]
#    #correlate    
#    for i in range(len(all_segments)-1):
#        d1=all_segments[i]
#        d2=all_segments[i+1]
#        corr.append(np.correlate(d1,d2))
#    avgCorr=np.average(corr)
#    
#    f_vec.append(avgCorr)
#    #mean all segments
#    segment_mean=[]
#    for segment in all_segments[0:5]:
#        segment_mean.append(np.mean(segment))
#    for m in segment_mean:
#        f_vec.append(m)
#        
#    #Std
#    std_mean=[]
#    for segment in all_segments[0:5]:
#        std_mean.append(np.std(segment))
#    for s in std_mean:
#        f_vec.append(s)
#    return f_vec


#1. Read Data
def ECG_segment(dataset, channel_num=0):
    segments_per_ECG=[]
    all_preprocessed_datas=[]
    for rec in dataset:
        ecg_all_channel=rec[0]
        ecg_channel_1=ecg_all_channel[:,channel_num]
        #Done by gautham
        pre_precocessed_data= overall_preprocessing(ecg_channel_1)
        pre_precocessed_data=pre_precocessed_data[:-9]
        
        detectors=Detectors(fs)
        #Peak Detection
        r_peaks=detectors.engzee_detector(pre_precocessed_data)
        #Peak Segmentation
        all_segments=[]
        count=0
        for i in range(len(r_peaks)):
            data_segment=np.zeros((1,500),dtype=float)
            data_segment=data_segment.ravel()
            
            if((r_peaks[i]-250)>=0 and (r_peaks[i]+250)<len(pre_precocessed_data)):
                data_segment=pre_precocessed_data[r_peaks[i]-250:r_peaks[i]+250]
                count=count+1
            elif((r_peaks[i]-250)<0):
                    nZeros=250-r_peaks[i]
                    data_segment[nZeros:500]=pre_precocessed_data[0:r_peaks[i]+250]
                    count=count+1
            elif(r_peaks[i]+250>len(pre_precocessed_data)):
                nZeros=r_peaks[i]+250-len(pre_precocessed_data)
                data_segment[0:500-nZeros]=pre_precocessed_data[r_peaks[i]-250:len(pre_precocessed_data)]
                count=count+1
            all_segments.append(data_segment)
        
        all_preprocessed_datas.append(pre_precocessed_data)
        segments_per_ECG.append(all_segments)
        
    return segments_per_ECG,all_preprocessed_datas

#Example
#dataset=load_from_folder()
#s,apd=ECG_segment_and_features(dataset,0)
