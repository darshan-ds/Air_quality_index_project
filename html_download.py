# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:19:02 2021

@author: Darshan
"""

# Importing the necessary libraries
import os
import time
import requests
import sys

# Defining a function to retrieve the html page which contain the required data
# Here we won't get the cleaned data, the whole html page will be downloaded,
# and from that page we will scrape data using beautiful soup library.

def retrieve_html():
    # Selecting all the years from 2013 to 2018.
    for year in range(2013,2019):
        # Selecting all the months from 1 to 12
        for month in range(1,13):
            # Since we have to use a slightly varied url for months upto 9 and 
            # months after 9 we use an if statement.
            if month<10:
                url = f'https://en.tutiempo.net/climate/0{month}-{year}/ws-432950.html'
            else:
                url = f'https://en.tutiempo.net/climate/{month}-{year}/ws-432950.html'
            
            # We are requesting the html text to the url and assigning it to 
            # the variable texts. Also we should encode the whole texts.
            texts = requests.get(url)
            text_utf = texts.text.encode('utf-8')
            
            # Saving the data to local directory
            
            # We have to create a folder to save all the html files
            # Here this if statement will check if the path exists, if it doesn't
            # exists, then we will make a directory using 'os.makedirs' command.
            if not os.path.exists(f'Data/Html_data/{year}'):
                os.makedirs(f'Data/Html_data/{year}')
            
            # Writing the html to that path
            with open(f'Data/Html_data/{year}/{month}.html', 'wb') as output:
                output.write(text_utf)
            
            # Python's standard out is buffered (meaning that it collects some 
            # of the data "written" to standard out before it writes it to the
            # terminal). Calling sys.stdout.flush() forces it to "flush" the 
            # buffer, meaning that it will write everything in the buffer to the 
            # terminal, even if normally it would wait before doing so.
            
            sys.stdout.flush()
            

if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time = time.time()
    print('Time taken: ', stop_time-start_time)
    