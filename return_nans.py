# -*- coding: utf-8 -*-
"""
Impute values to pandas DataFrame 

Returns a dataframe that replaces NaN values with either the mean, median, or mode for specified columns.  If catagorical variables are present the 'mode' function must be used to impute values.

Input: 
    df - pandas DataFrame 
    columns - list of columns where NaNs will be replaced
    n_nans - an integer that represents the maximum number of nans that can exist in the column for replacement to occur 
    func - set to 'mean', 'median', or 'mean' to determine the function that will be used for each column when computing an imputed value
    
Output:
    df - pandas DataFrame containing imputed values for NaNs"""
    
def replace_nans(df, columns, n_nans, func='mode'):
    
    for col in columns:  
        if df[col].isnull().sum() < n_nans:
            if func=='mean':             
                stat = df[col].mean()
            elif func=='median':
                stat = df[col].median()
            elif func=='mode':
                stat = df[col].mode()

            df[col].fillna(stat[0], inplace=True)
           
    return df