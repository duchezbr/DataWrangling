# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:02:34 2019

PURPOSE: Create catagorical bins for continuous data

INPUTS:
    df: pandas DataFrame
        df containing the column that needs to be split
    q: int
        number of splits to be made to the data column
    col: str
        name of column to be split
    labels: bool
        True: returned series will contain catagorical labels
        False: returned series will contain the range used for binning data
        
OUTPUT:
    qcut: Series containing catagorical label for each value
    
@author: duchezbr
"""

def qcut_quantiles(df, q, col, labels):
    
    if labels==True:
        q_labels = np.arange(q)
        qcuts = pd.qcut(df[col], q, labels=q_labels) 
        
    else:
        qcuts = pd.qcut(df[col], q)
    
    qcuts.name='{}_{}'.format(q, col)                                                
    return qcuts