#Performing Statistics on Winds data
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

"""
#Generating Random data ONLY RUNS ONCE
date_strings = np.arange('2006-01-01','2024-01-01',dtype='datetime64') #All days between the dates 

#Splitting in diff arrays Year, Months, Days
years = (date_strings.astype('datetime64[Y]')).astype(int)+1970 
months= ((date_strings.astype('datetime64[M]')).astype(int)%12)+1
days= (((date_strings.astype('datetime64[D]')).astype(int)-9)%30)+1

#combining in one 2d array [[year,month,day].....]
result_array = np.column_stack((years,months,days))

#Initializing a ones huge array then filling it wiht dates and random speeds
data=np.ones((6574,15))
data[:,:3]=result_array

x=6574*12 #Flat size of speeds
cache=np.random.uniform(6,40,(x-5000))              #Most speeds between 6 to 4 MPH
temp=np.random.uniform(40,230,(5000))               #Few speeds highr than that
cache=np.concatenate((cache,temp))                  #Connecting all speeds
np.random.shuffle(cache)
cache=cache.reshape((6574,12))
data[:,3:]=cache                                    #Populating the array with the speeds
formats = ['%4.0f', '%2.0f', '%2.0f']               #Adjusting formatting for clean represntation
cache=['%6.2f']*12
formats=np.concatenate((formats,cache))
formats=" ".join(formats)
np.savetxt('Numpy/Wind_Data.txt',data,fmt=formats)   #Saving data to file with 2 decimals only
"""

#Loading the Data that we created randomly before
data=np.loadtxt('Numpy/Wind_Data.txt')
dates=data[:,:4]
speed=data[:,4:]

#Plotting the speed data to have an understanding of our data
plt.figure(figsize=[15,8])
plt.scatter(np.tile(dates[:,0],11),speed,alpha=0.055,)
plt.title('Wind Speed to Year Scatter Plot')
plt.xlabel('Years')
plt.ylabel('Speeds in MPH')
plt.xticks(np.arange(2006,2024))
plt.figure()
sns.kdeplot(speed.flatten(), fill=True, color='skyblue', label='Speeds KDE')
plt.show()
  

# Printing out the Max, Min, Mean and STD for all speeds
print(f'Max= {np.max(speed):.2f}, Min= {np.min(speed):.2f}, Mean= {np.mean(speed):.2f}, Std= {np.std(speed):.2f}\n')

# Printing out the same but location specific then Date specefic
print(f'Max= {np.round(np.max(speed,axis=0),2)},\nMin= {np.round(np.min(speed,axis=0),2)},\nMean= {np.round(np.mean(speed,axis=0),2)},\nStd= {np.round(np.std(speed,axis=0),2)}\n')
print(f'Max= {np.round(np.max(speed,axis=1),2)},\nMin= {np.round(np.min(speed,axis=1),2)},\nMean= {np.round(np.mean(speed,axis=1),2)},\nStd= {np.round(np.std(speed,axis=1),2)}\n')

#Location of the highes speed per day 
Y,X=np.unravel_index(np.argmax(speed,axis=1),speed.shape) 
print(f'Location of Max per day: \nRows= {Y}\nColumns= {X}\n')

#Date of Maximum Wind Speed
i_y,i_x=np.unravel_index(speed.argmax(),speed.shape)
print(f'Date where max speed was recorded: {dates[i_y,:3]}\n')

#Avg speeds in Jan for each location 
print(f'Avg speed for Jan per location:\n{np.round(np.mean(data[data[:,1]==1,3:],axis=0),2)}')

