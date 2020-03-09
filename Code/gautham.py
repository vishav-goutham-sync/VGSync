#Preprocessing testing

from load_data import load_from_folder
from Segmentation import ECG_segment
import numpy as np
import neurokit as nk

dataset=load_from_folder()

#: Segemtnation for  first channel per patient
#: all_preprocessed_signnals (apd)
#: all_R_peaks (arp)

s,apd,arp=ECG_segment(dataset,channel_num=0)

def feat_array(ht,hf):
    fv=[]
    # time features
    fv.append(ht['CVSD'])
    fv.append(ht['RMSSD'])
    fv.append(ht['cvNN'])
    fv.append(ht['madNN'])
    fv.append(ht['mcvNN'])
    fv.append(ht['meanNN'])
    fv.append(ht['medianNN'])
    fv.append(ht['n_Artifacts'])
    fv.append(ht['pNN20'])
    fv.append(ht['pNN50'])
    fv.append(ht['sdNN'])
    fv.append(np.mean(ht['RR_Intervals']))
    # frequency features
    fv.append(hf['HF'])
    fv.append(hf['HF/P'])
    fv.append(hf['HFn'])
    fv.append(hf['LF'])
    fv.append(hf['LF/HF'])
    fv.append(hf['LF/P'])
    fv.append(hf['LFn'])
    fv.append(hf['Shannon_h'])
    fv.append(hf['Total_Power'])
    fv.append(hf['Triang'])
    fv.append(hf['ULF'])
    fv.append(hf['VHF'])
    fv.append(hf['VLF'])
    return fv

#Feature Extraction
feature_array=[]    
sampling_rate = 300
for i in range(len(arp)):
    x_rpeaks=arp[i]
    x_rpeaks=np.asarray(x_rpeaks)
    hrv_t = nk.bio_ecg.ecg_hrv(rpeaks=x_rpeaks, sampling_rate=sampling_rate, hrv_features=['time'])
    hrv_f = nk.bio_ecg.ecg_hrv(rpeaks=x_rpeaks, sampling_rate=sampling_rate, hrv_features=['frequency'])
    #hrv_nl = nk.bio_ecg.ecg_hrv(rpeaks=x_rpeaks, sampling_rate=sampling_rate, hrv_features=['nonlinear'])
    temp_fa=feat_array(hrv_t,hrv_f)
    feature_array.append(temp_fa)