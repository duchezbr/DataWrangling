# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:40:18 2019

PURPOSE: Normalize select DataFrame columns between 0 and 1

INPUT: 
    df: pandas DataFrame
    col_names: list
        column names of numerical columns that need to be normalized (columns can't contain nans)
        
OUTPUT:
    df: pandas DataFrame
        original dataframe with specified columns normalized
    

@author: duchezbr
"""

def normalize_df(df, col_names):
    
    from sklearn import preprocessing
    min_max_scaler = preprocessing.MinMaxScaler()
    
    # set_col_names to Index dtype so get_loc can be used to get numerical column index
    col_names = pd.Index(col_names)
    # numerical index for col_names
    col_idx = [df.columns.get_loc(c) for c in col_names if c in df.columns]
    # make sure selected columns are of 'float' dtype 
    val = df.iloc[:, col_idx].astype('float64').values    
    np_scaled = min_max_scaler.fit_transform(val)
    
    df_normalized = pd.DataFrame(np_scaled, columns = col_names)
    # loop through column names and set normalized values to original columns of dataframe
    for i in col_names:
        df.loc[::, i] = df_normalized[i]
        
    return df
    
