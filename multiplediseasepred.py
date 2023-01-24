# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:57:18 2023

@author: Asus
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("C:/Users/Asus/Desktop/diseases project/diabetes_model.sav",'rb'))
heart_model=pickle.load(open("C:/Users/Asus/Desktop/diseases project/heart_disease_model.sav",'rb'))
parkinsons_model=pickle.load(open("C:/Users/Asus/Desktop/diseases project/parkinsons_model.sav",'rb'))

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
#diabetes page
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML') #title
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')
    
    #code for prediction
    diab_diagnosis=""
    #creating predict button
    if st.button("Diabetes Test Result"):
        a=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        b=[float(i) for i in a]
        diab_prediction= diabetes_model.predict([b])
        if (diab_prediction[0])==1 :
            diab_diagnosis= 'The person is Diabetic'
        else:
            diab_diagnosis= 'The person is Not Diabetic'
    st.success(diab_diagnosis)

#heart page
if (selected == 'Heart Disease Prediction'):
    st.title('Heart Disease Prediction using ML') #title
    
    col1, col2, col3 = st.columns(3) 
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')
    
    heart_diagnosis=""
    #creating predict button
    if st.button("Heart disease Test Result"):
        a=[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]
        b=[float(i) for i in a]
        heart_prediction= heart_model.predict([b])
        if (heart_prediction[0]==1) :
            heart_diagnosis= 'The person has heart disease'
        else:
            heart_diagnosis= 'The person does not have heart disease'
    st.success(heart_diagnosis)
    
#parkinsons page
if (selected == "Parkinsons Prediction"):
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        fo = st.text_input('MDVP:(Fo Hz)')
    with col2:
        fhi = st.text_input('MDVP:(Fhi Hz)')
    with col3:
        flo = st.text_input('MDVP:(Flo Hz)')
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        RAP = st.text_input('MDVP:RAP')
    with col1:
        PPQ = st.text_input('MDVP:PPQ')
    with col2:
        DDP = st.text_input('Jitter:DDP')
    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        APQ = st.text_input('MDVP:APQ')
    with col2:
        DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    with col1:
        PPE = st.text_input('PPE')
    
    parkinsons_diagnosis=""
    #creating predict button
    if st.button("Parkinson\'s disease Test Result"):
        a=[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        b=[float(i) for i in a]
        parkinsons_prediction= parkinsons_model.predict([b])
        if (parkinsons_prediction[0]==1) :
            parkinsons_diagnosis= 'The person has parkinson\'s disease'
        else:
            parkinsons_diagnosis= 'The person does not have parkinson\'s disease'
    st.success(parkinsons_diagnosis)