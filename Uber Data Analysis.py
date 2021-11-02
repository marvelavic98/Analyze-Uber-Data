#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the libraries that we will use

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Load the dataset
uber_data = pd.read_csv('D:/Data analysis/codes/dataset/uber-raw-data-apr14.csv')
uber_data.head(5) #show upper upper 5 rows from the dataset


# In[3]:


#Show the information about the data
uber_data.info()


# In[5]:


#Check if there are missing values in the dataset
def num_missing(x):
    return sum(x.isnull())
print("Number of miisng values per column : ")
print(uber_data.apply(num_missing, axis=0))


# In[6]:


#other way to show missing values
print(uber_data.isnull().sum())


# In[7]:


#Analytical summary of the dataset
uber_data.describe(include='all')


# In[12]:


#Extract additional information
uber_data['Date/Time'] = pd.to_datetime(uber_data['Date/Time'], format="%m/%d/%Y %H:%M:%S")
uber_data['DayofWeekNum'] = uber_data['Date/Time'].dt.dayofweek
uber_data['DayOfWeek'] = uber_data['Date/Time'].dt.weekday_name
uber_data['DayNum'] = uber_data['Date/Time'].dt.day
uber_data['HourOfDay'] = uber_data['Date/Time'].dt.hour


# In[13]:


uber_data.head(5)


# In[14]:


# show the shape of the dataset
uber_data.shape


# In[15]:


# show the unique base codes
uber_data['Base'].unique()


# In[16]:


#show the total rides based on the base codes
sns.catplot(x='Base', data=uber_data, kind='count')


# In[23]:


# Create a pivot table
uber_weekly_data = uber_data.pivot_table(index=['DayofWeekNum', 'DayOfWeek'], values='Base', aggfunc='count')
uber_weekly_data


# In[26]:


#show the data in pivot table from the maximum to minimum order
uber_weekly_data_sort = uber_weekly_data.reindex(uber_weekly_data['Base'].sort_values(ascending=False).index)
uber_weekly_data_sort


# In[27]:


#Visualize the pivot table data
uber_weekly_data.plot(kind='bar', figsize=(16,10))


# In[34]:


#visualize the total trip of uber driver based on hour
uber_hourly_data = uber_data.pivot_table(index=['HourOfDay'], values='Base', aggfunc='count')
uber_hourly_data.plot(kind='line', figsize=(16,10))
plt.title("Graph of Uber Trip Each Hour")
plt.ylabel("Total Trip")
plt.xlabel("Number or Hours");


# In[38]:


#visualize the number of booking uber driver
uber_day_booking = uber_data.pivot_table(index=['DayNum'], values='Base', aggfunc='count')
uber_day_booking.plot(kind='bar', figsize=(16,10))
plt.title("Number of Booking Uber Driver Each Day")
plt.xlabel("Day")
plt.ylabel("Number of Booking");


# In[40]:


#list the number of trip in a month using groupby
def count_rows(rows):
    return len(rows)

by_date = uber_data.groupby('DayNum').apply(count_rows)
by_date


# In[44]:


# Sort the Day based on minimum number of order to maximum number of order
    #if want to sort from max to min use sort_values(ascending=False)
total_trip_sort = by_date.sort_values()
total_trip_sort


# In[64]:


#Analyze the hours data
def count_rows(rows):
    return len(rows)

by_hour = uber_data.groupby('HourOfDay').apply(count_rows)
by_hour
#by_hour.hist(bins=24, range=(.5, 24))


# In[68]:


#Visualize the data based on trip each hour
plt.hist(uber_data.HourOfDay, bins=24, range=(.5, 24))
plt.title("Trip in Each Hour")
plt.xlabel("Hour")
plt.ylabel("Number of Trip")
plt.show()


# In[71]:


#Create a cross table to analyze uber booking based on day and hour
count_rows(uber_data)
by_hour_weekday = uber_data.groupby('HourOfDay DayofWeekNum'.split()).apply(count_rows).unstack()
by_hour_weekday


# In[72]:


#heat map the brightest spot shows the day/hour with the highest frequency
plt.figure(figsize=(20,10))
sns.heatmap(by_hour_weekday)


# In[ ]:




