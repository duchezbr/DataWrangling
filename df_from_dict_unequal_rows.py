# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:35:22 2019

PURPOSE: Creates a DataFrame from a dictionary where columns do not contain an equal number of values 

INPUT: dict

OUTPUT: 
    dataframe with containing contents of dictionary. Where values are not avaiablabe to populate the dataframe cells contain NaNs

Sample Dictionary:
my_dict = {'Services': ['Jumpstart', 'KickStart', 'Clinical Data Specialist', 'Stat programming and Analysis Services', 'Review Enhancement', 'CoreDF', 'Sevice Desk', 'Scientific Computing', 'Traning'], 'Tools': ['MAED', 'FDALabel', 'DataFit', 'Jreview', 'Analysis Toolbox', 'Janus Clinical', 'JMP/JMP Clinical', 'IND Smart Review Template', 'Janus Nonclinical', 'CISST', 'IRB SST', 'Complis', 'CBITE', 'Lorenz docuBridge', 'Reviewer Portal']}

@author: Brian DuChez
"""

def df_from_dict_unequal_rows(my_dict):

#import pandas as pd
#import numpy as np

    df = pd.DataFrame(data=dict([ (k,pd.Series(v)) for k,v in my_dict.items() ]))
    
    return df