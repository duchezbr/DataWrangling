# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:56:56 2019

PURPOSE: Return a numpy array that contains binary labels for "male" and "female"

REQUIRES:
    import numpy as np
    from sklearn.preprocessing import LabelEncoder
    
INPUT: 
    df: pandas dataframe
    col: str
        name of column that contains male and female assignments
    male_female: list
        list of the two terms that are used to describe male and female in the source file
        
OUTPUT:
    binary_labels: numpy array that contains binarized male/female labels
    le:        
 

@author: duchezbr
"""

def binarize_male_female(df, col, male_female):

    le = LabelEncoder()
    le.fit(male_female)
    binary_labels = le.transform(df[col].values)
    
    return binary_labels, le


