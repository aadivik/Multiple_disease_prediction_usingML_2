#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 02:24:35 2023

@author: aadivikram
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('/Users/aadivikram/Desktop/project/multiple_disease_prediction/saved models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('/Users/aadivikram/Desktop/project/multiple_disease_prediction/saved models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('/Users/aadivikram/Desktop/project/multiple_disease_prediction/saved models/parkinsons_model.sav','rb'))


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multiple disease Prediction using ML', 
                           ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                           
                           icons = ['activity','heart','person'],
                           
                           default_index=0)
    
# Diabetes prediction page
if(selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user 
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose level')
        
    with col3:
        BloodPressure = st.text_input('Blood pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin value')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
    with col2:
        Age = st.text_input('Age of the Person')
        
        #code for Prediction
        diab_diagnosis = ''
          
        
        #creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
            
        if(diab_prediction[0] == 1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'the person is not Diabetic'
            
        st.success(diab_diagnosis)
            
    
    
if(selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
if(selected == 'Parkinson Disease Prediction'):
    
    # page title
    st.title('Parkinson Prediction using ML')
    
    
    