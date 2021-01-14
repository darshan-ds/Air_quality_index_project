# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 15:21:35 2021

@author: Darshan
"""

import pandas as pd
import sys
import requests
import os
from bs4 import BeautifulSoup
import csv


def description_df():
    
    file_html = open('Data/Html_data/2013/1.html', 'rb')
    plain_text = file_html.read()
    
    tempD = []
    finalD = []
    
    soup = BeautifulSoup(plain_text, 'lxml')
    
    for table in soup.findAll('table', {'class': 'info'}):
        for tbody in table:
            for tr in tbody:
                for tb in tr:
                    tempD.append(tb)
    for item in tempD:
        if item=='\n':
            ls=[]
            count = 0
            continue
        else:
            ls.append(item)
            if count == 0:
                count += 1
                continue
            finalD.append(ls)
    return finalD

if __name__=="__main__":
    
    df = pd.DataFrame(description_df(), columns=['column_name','description'])
    df.index = df['column_name']    
    df.drop('column_name',axis=1,inplace=True)
    df.head()    
    df.to_csv('Data/Real-data/data_description.csv')
    
df = pd.read_csv('Data/Real-Data/data_description.csv',index_col='column_name')
df.head()
