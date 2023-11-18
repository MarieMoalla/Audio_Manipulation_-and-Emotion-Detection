#!/usr/bin/env python
# coding: utf-8

# #### Read me
# 
# After deviding an audio into chunks (response).
# This code will treat A QUESTION AT ONCE.
# Thats mean for each question (devided into chunks) we will treat each chunk hear and figure it emotion that we will generate an overall result that will return the emotion/emotions it figured from this audio.

# In[1]:


import librosa
import librosa.display
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

import joblib
from joblib import load

from IPython.display import Audio

import scipy.stats

import os


# In[2]:


data_path = "F:\\data-for-training\\Emotion_Detection_Model\\Interview_Questions\\One_Question_Chunks_PCQ8"
directory = os.listdir(data_path)
file_path = []

for file in directory:
        file_path.append(data_path + '\\' + file)

# dataframe for path of files.
path_df = pd.DataFrame(file_path, columns=['Path'])
path_df


# In[3]:


data_path = pd.concat( [path_df])
data_path.head()


# In[4]:


def noise(data):
    noise_amp = 0.035*np.random.uniform()*np.amax(data)
    data = data + noise_amp*np.random.normal(size=data.shape[0])
    return data
def stretch(data, rate=0.8):
    return librosa.effects.time_stretch(data, rate=rate)

def shift(data):
    shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
    return np.roll(data, shift_range)

def pitch(data, sampling_rate, pitch_factor=0.7):
    return librosa.effects.pitch_shift(data, sr=sampling_rate, n_steps=pitch_factor)

# taking any example and checking for techniques.
path = np.array(data_path.Path)[1]
data, sample_rate = librosa.load(path)


# In[5]:


def extract_features(data):
    # ZCR
    result = np.array([])
    zcr = np.mean(librosa.feature.zero_crossing_rate(y=data).T, axis=0)
    result=np.hstack((result, zcr)) # stacking horizontally

    # Chroma_stft
    stft = np.abs(librosa.stft(data))
    chroma_stft = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
    result = np.hstack((result, chroma_stft)) # stacking horizontally

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally

    # Root Mean Square Value
    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    
    return result

def get_features(path):
    # duration and offset are used to take care of the no audio in start and the ending of each audio files as seen above.
    data, sample_rate = librosa.load(path)
    
    # without augmentation
    res1 = extract_features(data)
    result = np.array(res1)
    
    # data with noise
    noise_data = noise(data)
    res2 = extract_features(noise_data)
    result = np.vstack((result, res2)) # stacking vertically
    
    # data with stretching and pitching
    new_data = stretch(data)
    data_stretch_pitch = pitch(new_data, sample_rate)
    res3 = extract_features(data_stretch_pitch)
    result = np.vstack((result, res3)) # stacking vertically
    
    
    return result


# In[6]:


X= []

for path in data_path.Path:
    feature = get_features(path)
    for ele in feature:
        X.append(ele)     
len(X)


# In[7]:


scaler = load("F:\\data-for-training\\Emotion_Detection_Model\\scaler.joblib")
X = scaler.transform(X)
X.shape


# In[8]:


X = np.expand_dims(X, axis=2)
X.shape


# In[9]:


#import trained model
test_model = joblib.load('F:\\data-for-training\\Emotion_Detection_Model\\model_filename.joblib')


# In[10]:


#prediction
encoder = joblib.load('F:\\data-for-training\\Emotion_Detection_Model\\encoder.joblib')

pred_test = test_model.predict(X)
y_pred = encoder.inverse_transform(pred_test)
print(y_pred.shape)


# In[11]:


df = pd.DataFrame(columns=['Predictions'])
df['Predictions'] = y_pred.flatten()
df.head()


# In[12]:


import statistics

# Assuming df['Predictions'] is your Pandas DataFrame column
predictions = df['Predictions']

# Use the mode function to get the most frequent element(s)
most_frequent = statistics.multimode(predictions)

# Convert the result to an array
result_array = np.array(most_frequent)

# Print or use the result_array as needed
print("Most Frequent Predictions:", result_array)


# In[ ]:




