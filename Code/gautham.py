
#Preprocessing testing

from load_data import load_from_folder
from Segmentation import ECG_segment

dataset=load_from_folder()
s,apd=ECG_segment(dataset,0)

#Feature Extraction