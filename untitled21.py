# -*- coding: utf-8 -*-
"""Untitled21.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OuUm-DyXOv8gDmDnRKUAgS0fm0ekPLIT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train = pd.read_csv("/content/drive/MyDrive/Train.csv")
test = pd.read_csv("/content/drive/MyDrive/Test.csv")
riders = pd.read_csv("/content/drive/MyDrive/Riders.csv")

train.head()

Training_Feature_Eng = train.copy()
Testing_Feature_Eng  = test.copy()

from datetime import datetime as dt
# Variable " Placement Time of Day "
# converting time in hours 

Training_Feature_Eng['Placement - Time'] = Training_Feature_Eng['Placement - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Training_Feature_Eng['Placement Time of Day'] = Training_Feature_Eng['Placement - Time'].dt.hour

Testing_Feature_Eng['Placement - Time'] = Testing_Feature_Eng['Placement - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Testing_Feature_Eng['Placement Time of Day'] = Testing_Feature_Eng['Placement - Time'].dt.hour

Testing_Feature_Eng['Placement Time of Day'].head()

print(Training_Feature_Eng['Placement Time of Day'].min())
print(Training_Feature_Eng['Placement Time of Day'].max())

print(Testing_Feature_Eng['Placement Time of Day'].min())
print(Testing_Feature_Eng['Placement Time of Day'].max())

def get_part_hr(hour):
    if (hour > 4) and (hour <= 8):
        return 'Early Morning'
    elif (hour > 8) and (hour < 12 ):
        return 'Morning'
    elif (hour >= 12) and (hour <= 16):
        return'Noon'
    elif (hour > 16) and (hour <= 20):
        return 'Evening'
    elif (hour > 20) and (hour <= 22):
        return'Night'
    else:
        return'Late Night'

Training_Feature_Eng['Placement Time of Day'] = Training_Feature_Eng['Placement Time of Day'].apply(get_part_hr)
Testing_Feature_Eng['Placement Time of Day'] = Testing_Feature_Eng['Placement Time of Day'].apply(get_part_hr)

Training_Feature_Eng.head()

print(Training_Feature_Eng['Placement Time of Day'].head(2))
print(Testing_Feature_Eng['Placement Time of Day'].head(2))

# converting time in hours 
# Variable " Confirmation Time of Day "
Training_Feature_Eng['Confirmation - Time'] = Training_Feature_Eng['Confirmation - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Training_Feature_Eng['Confirmation Time of Day'] = Training_Feature_Eng['Confirmation - Time'].dt.hour

Testing_Feature_Eng['Confirmation - Time'] = Testing_Feature_Eng['Confirmation - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Testing_Feature_Eng['Confirmation Time of Day'] = Testing_Feature_Eng['Confirmation - Time'].dt.hour

Training_Feature_Eng['Confirmation Time of Day'] = Training_Feature_Eng['Confirmation Time of Day'].apply(get_part_hr)
Testing_Feature_Eng['Confirmation Time of Day'] = Testing_Feature_Eng['Confirmation Time of Day'].apply(get_part_hr)

# converting time in hours 
# Varibale " Pickup Time of Day "
Training_Feature_Eng['Pickup - Time'] = Training_Feature_Eng['Pickup - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Training_Feature_Eng['Pickup Time of Day'] = Training_Feature_Eng['Pickup - Time'].dt.hour

Testing_Feature_Eng['Pickup - Time'] = Testing_Feature_Eng['Pickup - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Testing_Feature_Eng['Pickup Time of Day'] = Testing_Feature_Eng['Pickup - Time'].dt.hour

Training_Feature_Eng['Pickup Time of Day'] = Training_Feature_Eng['Pickup Time of Day'].apply(get_part_hr)
Testing_Feature_Eng['Pickup Time of Day'] = Testing_Feature_Eng['Pickup Time of Day'].apply(get_part_hr)

print(Training_Feature_Eng['Pickup Time of Day'].head(5))
print(Testing_Feature_Eng['Pickup Time of Day'].head(5))

# converting time in hours
# Variable " Arrival at Pickup Time of Day "
Training_Feature_Eng['Arrival at Pickup - Time'] = Training_Feature_Eng['Arrival at Pickup - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Training_Feature_Eng['Arrival at Pickup Time of Day'] = Training_Feature_Eng['Arrival at Pickup - Time'].dt.hour

Testing_Feature_Eng['Arrival at Pickup - Time'] = Testing_Feature_Eng['Arrival at Pickup - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Testing_Feature_Eng['Arrival at Pickup Time of Day'] = Testing_Feature_Eng['Arrival at Pickup - Time'].dt.hour

Training_Feature_Eng['Arrival at Pickup Time of Day'] = Training_Feature_Eng['Arrival at Pickup Time of Day'].apply(get_part_hr)
Testing_Feature_Eng['Arrival at Pickup Time of Day'] = Testing_Feature_Eng['Arrival at Pickup Time of Day'].apply(get_part_hr)

print(Training_Feature_Eng['Arrival at Pickup Time of Day'].head(5))
print(Testing_Feature_Eng['Arrival at Pickup Time of Day'].head(5))

# converting time in hours from the Training Feature Eng
# Variable " Arrival at Destination - Time "
Training_Feature_Eng['Arrival at Destination - Time'] = Training_Feature_Eng['Arrival at Destination - Time'].apply(lambda x: dt.strptime(x,'%I:%M:%S %p'))
Training_Feature_Eng['Arrival at Destination Time of Day'] = Training_Feature_Eng['Arrival at Destination - Time'].dt.hour

Testing_Feature_Eng['Arrival at Destination - Time'] = Training_Feature_Eng['Arrival at Destination - Time']
Testing_Feature_Eng['Arrival at Destination Time of Day'] = Training_Feature_Eng['Arrival at Destination - Time'].dt.hour

Training_Feature_Eng['Arrival at Destination Time of Day'].head()
Testing_Feature_Eng["Arrival at Destination Time of Day"].head()

Training_Feature_Eng['Arrival at Destination Time of Day']= Training_Feature_Eng['Arrival at Destination Time of Day'].apply(get_part_hr)
Testing_Feature_Eng['Arrival at Destination Time of Day'] = Testing_Feature_Eng['Arrival at Destination Time of Day'].apply(get_part_hr)

print(Training_Feature_Eng['Arrival at Destination Time of Day'].head(5))
print(Testing_Feature_Eng['Arrival at Destination Time of Day'].head(5))

"""**Grouping the variable "Weekday (Mo=1)" into Weekday and Weekend¶**"""

# Variable " Placement_-_Weekday_(Mo_=_1) " 
Training_Feature_Eng['Actual Day of Placement'] = np.where(Training_Feature_Eng['Placement - Weekday (Mo = 1)']< 6,
                                                   'Weekday','Weekend')

Testing_Feature_Eng['Actual Day of Placement'] = np.where(Testing_Feature_Eng['Placement - Weekday (Mo = 1)']< 6,
                                                   'Weekday','Weekend')

print(Training_Feature_Eng['Actual Day of Placement'].head(2))
print(Testing_Feature_Eng['Actual Day of Placement'].head(2))

# Variable " Confirmation_-_Weekday_(Mo_=_1) " 
Training_Feature_Eng['Actual Day of Confirmation'] = np.where(Training_Feature_Eng['Confirmation - Weekday (Mo = 1)']< 6,
                                                      'Weekday','Weekend')

Testing_Feature_Eng['Actual Day of Confirmation'] = np.where(Testing_Feature_Eng['Confirmation - Weekday (Mo = 1)']< 6,
                                                       'Weekday','Weekend')

print(Training_Feature_Eng['Actual Day of Confirmation'].tail(2))
print(Testing_Feature_Eng['Actual Day of Confirmation'].tail(2))

# Varibale " Pickup_-_Weekday_(Mo_=_1) "
Training_Feature_Eng['Actual Day of Pickup'] = np.where(Training_Feature_Eng['Pickup - Weekday (Mo = 1)'] < 6, 
                                       'Weekday', 'Weekend')

Testing_Feature_Eng['Actual Day of Pickup'] = np.where(Testing_Feature_Eng['Pickup - Weekday (Mo = 1)'] < 6, 
                                       'Weekday', 'Weekend')

print(Training_Feature_Eng['Actual Day of Pickup'].head(2))
print(Testing_Feature_Eng['Actual Day of Pickup'].head(2))

# Varibale " Arrival_at_Destination_-_Weekday_(Mo_=_1) "
Training_Feature_Eng['Actual Day of Arrival at Destination'] = np.where(Training_Feature_Eng['Arrival at Destination - Weekday (Mo = 1)'] < 6, 
                                                                 'Weekday', 'Weekend')

Testing_Feature_Eng['Arrival at Destination - Weekday (Mo = 1)'] = Training_Feature_Eng['Arrival at Destination - Weekday (Mo = 1)']
Testing_Feature_Eng['Actual Day of Arrival at Destination'] = np.where(Testing_Feature_Eng['Arrival at Destination - Weekday (Mo = 1)'] < 6, 
                                                                 'Weekday', 'Weekend')

print(Training_Feature_Eng['Actual Day of Arrival at Destination'].head(2))
print(Testing_Feature_Eng['Actual Day of Arrival at Destination'].head(2))

#Variable " Arrival_at_Pickup_-_Weekday_(Mo_=_1) "
Training_Feature_Eng['Actual Day of Arrival at Pickup'] = np.where(Training_Feature_Eng['Arrival at Pickup - Weekday (Mo = 1)'] < 6, 
                                                            'Weekday', 'Weekend')

Testing_Feature_Eng['Actual Day of Arrival at Pickup'] = np.where(Testing_Feature_Eng['Arrival at Pickup - Weekday (Mo = 1)'] < 6, 
                                                            'Weekday', 'Weekend')

print(Training_Feature_Eng['Actual Day of Arrival at Pickup'].tail(2))
print(Testing_Feature_Eng['Actual Day of Arrival at Pickup'].tail(2))

import sys
import webbrowser
from geopy.distance import geodesic

from geopy.distance import geodesic

Training_Feature_Eng['Proximity to Pickup Point'] = np.nan
Testing_Feature_Eng['Proximity to Pickup Point'] = np.nan

CBD_Nairobi=(-1.299719, 36.816097)

for i, row in Training_Feature_Eng.iterrows():
    Training_Feature_Eng.loc[i, 'Proximity to Pickup Point'] = geodesic((Training_Feature_Eng.loc[i, 'Pickup Lat'],
                                                                  Training_Feature_Eng.loc[i, 'Pickup Long']),CBD_Nairobi).km 
for i, row in Testing_Feature_Eng.iterrows():
    Testing_Feature_Eng.loc[i, 'Proximity to Pickup Point'] = geodesic((Testing_Feature_Eng.loc[i, 'Pickup Lat'],
                                                                  Testing_Feature_Eng.loc[i, 'Pickup Long']),CBD_Nairobi).km

print(Training_Feature_Eng['Proximity to Pickup Point'].head(2))
print(Testing_Feature_Eng['Proximity to Pickup Point'].head(2))

from geopy.distance import geodesic

Training_Feature_Eng['Proximity to Destination'] = np.nan
Testing_Feature_Eng['Proximity to Destination'] = np.nan

CBD_Nairobi=(-1.299719, 36.816097)

for i, row in Training_Feature_Eng.iterrows():
    Training_Feature_Eng.loc[i, 'Proximity to Destination'] = geodesic((Training_Feature_Eng.loc[i, 'Destination Lat'],
                                                                  Training_Feature_Eng.loc[i, 'Destination Long']),CBD_Nairobi).km
    
for i, row in Testing_Feature_Eng.iterrows():
    Testing_Feature_Eng.loc[i, 'Proximity to Destination'] = geodesic((Testing_Feature_Eng.loc[i, 'Destination Lat'],
                                                                  Testing_Feature_Eng.loc[i, 'Destination Long']),CBD_Nairobi).km

print(Training_Feature_Eng['Proximity to Destination'].head(2))
print(Testing_Feature_Eng['Proximity to Destination'].head(2))

Temperature_Deg = []

for Degree in Training_Feature_Eng['Temperature']:
    if (Degree >= 15) and (Degree <= 27):
        Temperature_Deg.append('Average High Temperature')
    elif (Degree >= 12) and (Degree <= 22 ):
        Temperature_Deg.append('Average Low Temperature')
    else:
        Temperature_Deg.append('Normal Temperature')

Temperature_Deg_1 = []

for Degree in Testing_Feature_Eng['Temperature']:
    if (Degree >= 15) and (Degree <= 27):
        Temperature_Deg_1.append('Average High Temperature')
    elif (Degree >= 12) and (Degree <= 22 ):
        Temperature_Deg_1.append('Average Low Temperature')
    else:
        Temperature_Deg_1.append('Normal Temperature')


Training_Feature_Eng['Temperature Condition'] = Temperature_Deg
Testing_Feature_Eng['Temperature Condition'] = Temperature_Deg_1

print(Training_Feature_Eng['Temperature Condition'].head(2))
print(Testing_Feature_Eng['Temperature Condition'].head(2))

Place_Day_Month = []

for Each_Day in Training_Feature_Eng['Placement - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Place_Day_Month.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Place_Day_Month.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Place_Day_Month.append('3rd Week')
    else:
        Place_Day_Month.append('4th Week')

Place_Day_Month_1 = []

for Each_Day in Testing_Feature_Eng['Placement - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Place_Day_Month_1.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Place_Day_Month_1.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Place_Day_Month_1.append('3rd Week')
    else:
        Place_Day_Month_1.append('4th Week')
            
Training_Feature_Eng['Placement_Day into Weeks'] = Place_Day_Month
Testing_Feature_Eng['Placement_Day into Weeks'] = Place_Day_Month_1

print(Training_Feature_Eng['Placement_Day into Weeks'].head(2))
print(Testing_Feature_Eng['Placement_Day into Weeks'].head(2))

Confirm_Day_Month = []

for Each_Day in Training_Feature_Eng['Confirmation - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Confirm_Day_Month.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Confirm_Day_Month.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Confirm_Day_Month.append('3rd Week')
    else:
        Confirm_Day_Month.append('4th Week')

Confirm_Day_Month_1 = []

for Each_Day in Testing_Feature_Eng['Confirmation - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Confirm_Day_Month_1.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Confirm_Day_Month_1.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Confirm_Day_Month_1.append('3rd Week')
    else:
        Confirm_Day_Month_1.append('4th Week')  

Training_Feature_Eng['Confirmation_Day into Weeks'] = Confirm_Day_Month
Testing_Feature_Eng['Confirmation_Day into Weeks'] = Confirm_Day_Month_1

print(Training_Feature_Eng['Confirmation_Day into Weeks'].head(2))
print(Testing_Feature_Eng['Confirmation_Day into Weeks'].head(2))

Arrival_Pickup_Day_Month = []

for Each_Day in Training_Feature_Eng['Arrival at Pickup - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Arrival_Pickup_Day_Month.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Arrival_Pickup_Day_Month.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Arrival_Pickup_Day_Month.append('3rd Week')
    else:
        Arrival_Pickup_Day_Month.append('4th Week')

Arrival_Pickup_Day_Month_1 = []

for Each_Day in Testing_Feature_Eng['Arrival at Pickup - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Arrival_Pickup_Day_Month_1.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Arrival_Pickup_Day_Month_1.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Arrival_Pickup_Day_Month_1.append('3rd Week')
    else:
        Arrival_Pickup_Day_Month_1.append('4th Week')
        
Training_Feature_Eng['Arrival_Pickup_Day into Weeks'] = Arrival_Pickup_Day_Month
Testing_Feature_Eng['Arrival_Pickup_Day into Weeks'] = Arrival_Pickup_Day_Month_1

print(Training_Feature_Eng['Arrival_Pickup_Day into Weeks'].head(2))
print(Testing_Feature_Eng['Arrival_Pickup_Day into Weeks'].head(2))

Pickup_Day_Month = []

for Each_Day in Training_Feature_Eng['Pickup - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Pickup_Day_Month.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Pickup_Day_Month.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Pickup_Day_Month.append('3rd Week')
    else:
        Pickup_Day_Month.append('4th Week')

Pickup_Day_Month_1 = []

for Each_Day in Testing_Feature_Eng['Pickup - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Pickup_Day_Month_1.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Pickup_Day_Month_1.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Pickup_Day_Month_1.append('3rd Week')
    else:
        Pickup_Day_Month_1.append('4th Week')
                        
Training_Feature_Eng['Pickup_Day into Weeks'] = Pickup_Day_Month
Testing_Feature_Eng['Pickup_Day into Weeks'] = Pickup_Day_Month_1

print(Training_Feature_Eng['Pickup_Day into Weeks'].head(2))
print(Testing_Feature_Eng['Pickup_Day into Weeks'].head(2))

Arrival_Destn_Day_Month = []

for Each_Day in Training_Feature_Eng['Arrival at Destination - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Arrival_Destn_Day_Month.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Arrival_Destn_Day_Month.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Arrival_Destn_Day_Month.append('3rd Week')
    else:
        Arrival_Destn_Day_Month.append('4th Week')

Arrival_Destn_Day_Month_1 = []
Testing_Feature_Eng['Arrival at Destination - Day of Month']=Training_Feature_Eng['Arrival at Destination - Day of Month']

for Each_Day in Testing_Feature_Eng['Arrival at Destination - Day of Month']:
    if (Each_Day > 0 and Each_Day <=7):
        Arrival_Destn_Day_Month_1.append('1st Week')        
    elif (Each_Day > 7 and Each_Day <=15):
        Arrival_Destn_Day_Month_1.append('2nd Week')
    elif (Each_Day > 15 and Each_Day <=23):
        Arrival_Destn_Day_Month_1.append('3rd Week')
    else:
        Arrival_Destn_Day_Month_1.append('4th Week')

Training_Feature_Eng['Arrival_Destination_Day into Weeks'] = Arrival_Destn_Day_Month
Testing_Feature_Eng['Arrival_Destination_Day into Weeks'] = Arrival_Destn_Day_Month_1

print(Training_Feature_Eng['Arrival_Destination_Day into Weeks'].head(2))
print(Testing_Feature_Eng['Arrival_Destination_Day into Weeks'].head(2))

Training_Feature_Eng.columns

Weekend_Weekday = Training_Feature_Eng.groupby(['Actual Day of Placement'], as_index=False).mean()
Weekend_Weekday[['Actual Day of Placement','Time from Pickup to Arrival']].sort_values('Time from Pickup to Arrival',ascending=False)

Pickup_Week = Training_Feature_Eng.groupby(['Pickup_Day into Weeks'], as_index=False).mean()
Pickup_Week[['Pickup_Day into Weeks','Time from Pickup to Arrival']].sort_values('Time from Pickup to Arrival',ascending=False)

Placement_Day_Time = Training_Feature_Eng.groupby(['Placement Time of Day'], as_index=False).mean()
Placement_Day_Time[['Placement Time of Day','Time from Pickup to Arrival']].sort_values('Time from Pickup to Arrival',ascending=False)

Testing_Feature_Eng.head(2)

Training_Feature_Eng.head(2)

Training_Feature_Eng['Precipitation in millimeters'].fillna(0, inplace = True)
Training_Feature_Eng['Temperature'].fillna((Training_Feature_Eng['Temperature'].mean()), inplace=True)

Testing_Feature_Eng['Precipitation in millimeters'].fillna(0, inplace = True)
Testing_Feature_Eng['Temperature'].fillna((Training_Feature_Eng['Temperature'].mean()), inplace=True)

Numeric_Train = Training_Feature_Eng._get_numeric_data()
Numeric_Test = Testing_Feature_Eng._get_numeric_data()

Categorical_Train = Training_Feature_Eng.select_dtypes(include=['object'])
Categorical_Test = Testing_Feature_Eng.select_dtypes(include=['object'])

Categorical_Train.head(2)

Droppers = ['Order No','User Id','Vehicle Type','Rider Id']

Categorical_Train = Categorical_Train.drop(Droppers, axis=1)
Categorical_Test = Categorical_Test.drop(Droppers, axis=1)

Encod_Cate_Train = pd.get_dummies(Categorical_Train)
Encod_Cate_Test = pd.get_dummies(Categorical_Test)

Encod_Cate_Train.head()

from statsmodels.stats.outliers_influence import variance_inflation_factor

def VIF(Numeric_Train, thresh=15):
    variables = list(range(Numeric_Train.shape[1]))
    dropped = True
    while dropped:
        dropped = False
        vif = [variance_inflation_factor(Numeric_Train.iloc[:, variables].values, ix)
               for ix in range(Numeric_Train.iloc[:, variables].shape[1])]
        maxloc = vif.index(max(vif))
        if max(vif) > thresh:
            print('dropping \'' + Numeric_Train.iloc[:, variables].columns[maxloc] + '\' at index: ' + str(maxloc))
            del variables[maxloc]
            dropped = True

    print('Remaining Variables are :')
    print(Numeric_Train.columns[variables])
    return Numeric_Train.iloc[:, variables]

Cleaned_Train = VIF(Numeric_Train,15)

def VIF(Numeric_Test, thresh=15):
    variables = list(range(Numeric_Test.shape[1]))
    dropped = True
    while dropped:
        dropped = False
        vif = [variance_inflation_factor(Numeric_Test.iloc[:, variables].values, ix)
               for ix in range(Numeric_Test.iloc[:, variables].shape[1])]
        maxloc = vif.index(max(vif))
        if max(vif) > thresh:
            print('dropping \'' + Numeric_Test.iloc[:, variables].columns[maxloc] + '\' at index: ' + str(maxloc))
            del variables[maxloc]
            dropped = True

    print('Remaining Variables are :')
    print(Numeric_Test.columns[variables])
    return Numeric_Test.iloc[:, variables]

Cleaned_Test = VIF(Numeric_Test)

Cleaned_Train = Cleaned_Train.drop(['Placement - Weekday (Mo = 1)'],axis=1)

Cleaned_Test = Cleaned_Test.drop(["Arrival at Destination - Weekday (Mo = 1)",'Pickup - Day of Month',
                                 "Pickup - Weekday (Mo = 1)"],axis=1)

Training_Cleaned = pd.concat([Encod_Cate_Train, Cleaned_Train], axis=1)
Testing_Cleaned = pd.concat([Encod_Cate_Test, Cleaned_Test], axis=1)

Training_Cleaned = Training_Cleaned.drop(['Placement Time of Day_Late Night',
                                         'Confirmation Time of Day_Late Night',
                                         'Arrival at Pickup Time of Day_Late Night'], axis=1)

Training_Cleaned.head(2)

"""**Modeling**"""

from sklearn.model_selection import train_test_split

New_Train = Training_Cleaned.copy()
X = New_Train.drop('Time from Pickup to Arrival', axis = 1)
Y = New_Train['Time from Pickup to Arrival']

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.2, random_state=42)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.linear_model import LinearRegression

linear_regress = LinearRegression()
linear_regress.fit(X_Train, Y_Train)
y_pred_train_lr = linear_regress.predict(X_Test)

print('RMSE:\t',np.sqrt(mean_squared_error(Y_Test,y_pred_train_lr)))
print('MSE:\t', mean_squared_error(Y_Test,y_pred_train_lr))
print("R2: \t", r2_score(Y_Test, y_pred_train_lr))