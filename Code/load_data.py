#LOAD challenge data

import numpy as np
import matplotlib.pyplot as plt
import os
import shutil
from glob import glob
import wfdb
from ecgdetectors import Detectors


# sampling frequency
fs=500


#path='C:/Users/Vishavpreet/Downloads/PhysioNetChallenge2020_Training_CPSC/Training_WFDB/'
path='data'
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

def load_from_folder():
    records=get_records()
    dataset=make_dataset(records)
    return dataset

def read_annotations():
    annotations=[]
    records=get_records()
    dataset=make_dataset(records)

    for i in range(len(dataset)):
        data_desc=dataset[i][1]
        comments=data_desc['comments']
    
    
        if(comments[2].find('Dx:')==0):
            annotation=comments[2]
        else:
            for cmnt in comments:
                if(cmnt.find('Dx')==0):
                    annotation=cmnt
    
          
        annotations.append(annotation.replace('Dx:','').replace(' ',''))
    return annotations