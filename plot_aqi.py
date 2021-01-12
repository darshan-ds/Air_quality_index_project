# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 18:43:00 2021

@author: Darshan
"""

# We are going to read the Air Quality Index data (dependant variable) and 
# select only the relevant columns from it. Also in that data, one day is further
# divided into 24 hours and for each hour, the quantity of Particulate Matter 2.5
# (PM2.5) is given. So we should take the mean PM2.5 for each day.

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import time

# The Air Quality Index data from year 2013 to 2018 is given in 6 csv files. So
# we have to create a function to read the data and modifying the data.


def avg_data(year):
    temp_i = 0
    average = []
    # Since one day in the data is divided into 24 parts we are selecting the 
    # data by chunks of 24. Hence in each chunk there will be one day. From that 
    # we can calculate the mean aqi for each day.
    for rows in pd.read_csv(f'Data/AQI/aqi{year}.csv',chunksize=24):
        # We are adding each hour PM2.5 level to a variable - 'add_var'.
        add_var = 0
        # for each iteration we are calculating the 'avg', so at the start of
        # each iteration we have to reset the 'avg' value to 0.
        avg = 0
        # We are creating an empty list called 'data'.
        data = []
        df = pd.DataFrame(data=rows)
        for index, rows in df.iterrows():
            # We are populating 'data' with all the 24 values in this iteration.
            data.append(rows['PM2.5'])
        for i in data:
            # There are some string in 'data', we are extracting only the integers
            # from that.
            if type(i) is float or type(i) is int:
                add_var += i
            elif type(i) is str:
                if i != 'NoData' and i != 'PwrFail' and i !='InVld' and i != '---':
                    temp = float(i)
                    add_var += temp
        # To find the 'avg' we are dividing the 'add_var' by 24.            
        avg = round(add_var/24,3)
        temp_i +=1
        # We are appending the 'avg' value to the main list.
        average.append(avg)
        
    return average


if __name__=="__main__":
    st_time = time.time()
    lst13 = avg_data(2013)
    lst14 = avg_data(2014)
    lst15 = avg_data(2015)
    
    # Here we are ploting the PM2.5 valus of 2013,2014,2015.
    plt.plot(range(0,len(lst13)),lst13,label='2013 data')
    plt.plot(range(0,len(lst14)),lst14,label='2014 data')
    plt.plot(range(0,len(lst15)),lst15,label='2015 data')
    plt.show()
    sp_time = time.time()
    print('Total time: ', sp_time-st_time)