
#Preprocessing testing

from load_data import load_from_folder
from Segmentation import ECG_segment

dataset=load_from_folder()

#: Segemtnation for  first channel per patient
#: all_preprocessed_signnals (apd)
#: all_R_peaks (arp)

s,apd,arp=ECG_segment(dataset,channel_num=0)


#Feature Extraction
x_rpeaks=arp[1]
import neurokit as nk
sampling_rate = 500
hrv_t = nk.bio_ecg.ecg_hrv(rpeaks=x_rpeaks, sampling_rate=sampling_rate, hrv_features=['time'])
hrv_f = nk.bio_ecg.ecg_hrv(rpeaks=x_rpeaks, sampling_rate=sampling_rate, hrv_features=['frequency'])
#hrv_nl = nk.bio_ecg.ecg_hrv(rpeaks=x_rpeaks, sampling_rate=sampling_rate, hrv_features=['nonlinear'])

fv=[]
fv.append(hrv_f['HF'])