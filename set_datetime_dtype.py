# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 14:02:23 2018

Purpose: 
    Change select columns of a pandas DataFrame to a datetime64[D] datatype.  The dates will be altered to a ISO 8601 date or datetime format.  Precision may be reduced to datetime64[D].

Requirements: 
    pandas as pd and numpy as np 

Input:
    df: pandas DataFrame
    columns: list
        names of columns that contain 'objects' that can be converted to a datetime datatype
    date_format: str
        format of 'object' that is to be converted to a datetime64[D]
    
Output:
    df - pandas DataFrame with the specified columns converted to a datetime64[D] dtype
    
Commonly used formats:
    %d Day of the month as a zero-padded decimal number. 30
    %b Month as locale’s abbreviated name. Sep
    %B Month as locale’s full name. September
    %m Month as a zero-padded decimal number. 09
    %y Year without century as a zero-padded decimal number. 13
    %Y Year with century as a decimal number. 2013
  

@author: Brian DuChez
"""

def set_datetime_dtype(df, columns, date_format):
    
    import pandas as pd
    import numpy as np

    for col in columns:
        
        if date_format != []:
            t_stamps = pd.to_datetime(df[col], format=date_format).values
            t_stamps = t_stamps.astype('datetime64[D]')
            df[col] = t_stamps
        else:
            df[col] = df[col].apply(pd.to_datetime)
        
    return df



#df['difference'] = df['sample.date'].sub(df['bloodtest.recdate'], axis=0)
## can set datetime as integer following an arethmatic operation
#df['difference'] = df['difference']/np.timedelta64(1,'D')
#df['difference'][df['difference'] <= 0].count()
