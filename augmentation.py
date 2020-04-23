import tensorflow.compat.v1 as tf
import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import scipy.interpolate as spi
from scipy import interpolate
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv1D
from keras.layers import AveragePooling1D,GaussianDropout
from keras.layers import Dropout
from keras.utils import np_utils
from keras.callbacks import EarlyStopping
from keras.callbacks import ModelCheckpoint
from keras import optimizers
from keras.models import load_model
import matplotlib.pyplot as plt
from numpy import random

def augment(train_data,train_label,a,b,c,d,num_pair,sigma=0.01):

    #train data augmentation
    len(train_data)
    len(train_label)
    def number_label(train_label):
        num_att=0
        num_el=0
        num_ex=0
        num_io=0
        for i in range(len(train_label)):
            if train_label[i]=='0':
                num_att+=1
            elif train_label[i]=='1':
                num_el+=1
            elif train_label[i]=='2':
                num_ex+=1
            elif train_label[i]=='3':
                num_io+=1
        #print('attchment=%04d'%num_att)
        #print('elastic=%04d'%num_el)
        #print('excitation=%04d'%num_ex)
        #print('ionization=%04d'%num_io)
        return num_att,num_el,num_ex,num_io
    num_label=number_label(train_label)
    train_data_num=num_label[0]+num_label[1]+num_label[2]+num_label[3]
    #data augmentation,training data
    train_data_aug=np.zeros((num_label[0]*a+num_label[1]*b+num_label[3]*d+num_label[2]*c,num_pair))
    train_label_aug=np.zeros((num_label[0]*a+num_label[1]*b+num_label[3]*d+num_label[2]*c,1))
    ind=0
    for i in range(train_data_num):
        #print('i=%02d'%i)
        if(train_label[i]=='0'):
            k=0
            #print('attachment%03d'%i)
            num_aug=a
            while True:
                #print("augmenting...x%03d"%k)
                Noise=np.random.normal(loc=0,scale=sigma,size=train_data[i].shape)
                Noise[num_pair-1]=0
                if k==0 : train_data_aug[ind]=train_data[i]
                elif k!=0 : train_data_aug[ind]=train_data[i]+Noise
                train_label_aug[ind]=0
                #print("array index=%05d"%ind)
                ind+=1
                if k==num_aug-1 : break
                k+=1
        if(train_label[i]=='1'):
            k=0
            #print('elastic%03d'%i)
            num_aug=b
            while True:
                #print("augmenting...x%03d"%k)
                Noise=np.random.normal(loc=0,scale=sigma,size=train_data[i].shape)
                Noise[num_pair-1]=0
                if k==0 : train_data_aug[ind]=train_data[i]
                elif k!=0 : train_data_aug[ind]=train_data[i]+Noise
                train_label_aug[ind]=1
                #print("array index=%05d"%ind)
                ind+=1
                if k==num_aug-1 : break
                k+=1
        if(train_label[i]=='2'):
            k=0
            #print('excitation%03d'%i)
            num_aug=c
            while True:
                #print("augmenting...x%03d"%k)
                Noise=np.random.normal(loc=0,scale=sigma,size=train_data[i].shape)
                Noise[num_pair-1]=0
                if k==0 : train_data_aug[ind]=train_data[i]
                elif k!=0 : train_data_aug[ind]=train_data[i]+Noise
                train_label_aug[ind]=2
                #print("array index=%05d"%ind)
                ind+=1
                if k==num_aug-1 : break
                k+=1
        if(train_label[i]=='3'):
            k=0
            #print('ionization%03d'%i)
            num_aug=d
            while True:
                #print("augmenting...x%03d"%k)
                Noise=np.random.normal(loc=0,scale=sigma,size=train_data[i].shape)
                Noise[num_pair-1]=0
                if k==0 : train_data_aug[ind]=train_data[i]
                elif  k!=0 : train_data_aug[ind]=train_data[i]+Noise
                train_label_aug[ind]=3
                #print("array index=%05d"%ind)
                ind+=1
                if k==num_aug-1 : break
                k+=1
    #training data_augmented   
    return train_data_aug,train_label_aug

   