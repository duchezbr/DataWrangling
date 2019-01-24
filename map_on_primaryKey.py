# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:10:58 2018

Purpose: Take column values from source DataFrame and map them to destination DataFrame based on the primaryKey.
Source columns must be entered as a list and not include the key. The key must be entered as a string.

source_df: pandas DataFrame
    contains the primaryKey used to map data to destination DataFrame and additional columns to be merged with the destination DataFrame
destination_df: pandas DataFrame
    contains the primaryKey that will be used as an index for merging data from the source file
key: string
    column name that contains the primaryKey that is used to map information between DataFrames
source_columns: list
    contains the names of columns that will be mapped to the destination file
    
Output: pandas DataFrame
    destination_df: pandas DataFrame
        contains the destination DataFrame with columns from the source file merged on the primaryKey
        
@author: duchezbr
"""

def map_on_primaryKey(source_df, destination_df, key, source_columns):
    
    source_columns.append(key)
    
    destination_df = source_df[source_columns].merge(destination_df, on=key, how='inner')

    return destination_df

