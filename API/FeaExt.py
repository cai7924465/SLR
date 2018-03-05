#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 14:06:46 2018

@author: rocky
"""
import scipy.io.wavfile as wav
import librosa  as lb
import numpy as np 

def MFCC(sig,rate,n_mfcc=13,hop_length=512,n_fft=1024):
    mfcc=lb.feature.mfcc(sig,rate,n_mfcc=n_mfcc,hop_length=hop_length,n_fft=n_fft)
    mfcc_delta = lb.feature.delta(mfcc)
    mfcc_delta_delta = lb.feature.delta(mfcc_delta)
    mfcc_39=np.vstack([mfcc, mfcc_delta,mfcc_delta_delta])
    h_mfcc_39=np.reshape(mfcc_39,(mfcc_39.shape[0]*mfcc_39.shape[1]),order='F') 
    return h_mfcc_39


# Using the Test Wav excutes MFCC function.
if __name__ == '__main__':
    rate , sig = wav.read("a-0001.wav")
    MFCC_39 = MFCC(sig,rate)
    #x = lb.core.stft(sig,n_fft=1024,hop_length=512)