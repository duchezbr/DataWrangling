# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 17:48:07 2019

PURPOSE: Converts a Wide dataframe to a new 2 column Long dataframe.  The first column of the new df contains the column headers from the Wide table adjacent to the values that were listed under said headers in column 2

df: pandas DataFrame
    Wide table to be converted to Long table

column1_name: str
    Name of the Long table column that contains column headers from original Wide table

column2_name: str
    Name of the Long table column that contains values from the original Wide table

@author: Brian DuChez
"""

def wide_to_long_headers_inSeperate_column(df, column1_name, column2_name):

    df1 = df.transpose()
    df2 = df1.stack()
    df3 = df2.reset_index(level=1, drop=True)
    df4 = df3.reset_index()
    df5 = df4.rename(columns={'index':column1_name, 0:column2_name})
    
    return df5