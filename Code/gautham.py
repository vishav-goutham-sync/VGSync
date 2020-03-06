
#Preprocessing testing

from load_data import load_from_folder
from Segmentation import ECG_segment

dataset=load_from_folder()

#: Segemtnation for  first channel per patient
#: all_preprocessed_signnals (apd)
#: all_R_peaks (arp)

s,apd,arp=ECG_segment(dataset,channel_num=0)

#Feature Extraction