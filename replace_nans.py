# -*- coding: utf-8 -*-
"""
Impute values to pandas DataFrame 

Returns a dataframe that replaces NaN values with either the mean, median, or mode for specified columns.  If catagorical variables are present the 'mode' function must be used to impute values.

Input: 
    df - pandas DataFrame 
    columns - list of columns where NaNs will be replaced
    func - set to 'mean', 'median', or 'mean' to determine the function that will be used for each column when computing an imputed value
    
Output:
    df - pandas DataFrame containing imputed values for NaNs"""
    
def replace_nans(df, columns, func='mode'):
    
    for col in columns:  
        
        if func=='mean':             
            stat = df[col].mean()
        elif func=='median':
            stat = df[col].median()
        elif func=='mode':
            stat = df[col].mode()

        df[col].fillna(stat[0], inplace=True)
           
    return df
