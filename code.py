import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
import math

health_data = pd.read_csv("heart.csv")

##Checking the shape of DataFrame
print('Number of rows are',health_data.shape[0], 'and number of columns are ',health_data.shape[1])

##Checking for null values
health_data.isnull().sum()/len(health_data)*100

##Checking For datatypes of the attributes(u19cs022)
health_data.info()

##Cheaking for duplicate rows
health_data[health_data.duplicated()]

##Data wrangling
##removing the duplicated data
health_data.drop_duplicates(keep='first',inplace=True)

##checking new shape of data
print('Number of rows are',health_data.shape[0], 'and number of columns are ',health_data.shape[1])

##data analysis 
sns.countplot(x="sex",data=health_data)

health_data["age"].plot.hist()

health_data.isnull()

health_data.isnull().sum()

#break down of rest ecg (u19cs022)
sns.countplot(x="restecg",data=health_data)

#Breakdown for chest pain

x=(health_data.cp.value_counts())
print(x)
p = sns.countplot(data=health_data, x="cp")
plt.show()

#Breakdown of FBS
x=(health_data.fbs.value_counts())
print(x)
p = sns.countplot(data=health_data                                                                                                                                                                                                                                                          , x="fbs")
plt.show()

#Breakdown for Exercise Induced Angina

x=(health_data.exng.value_counts())
print(x)
p = sns.countplot(data=health_data, x="exng")
plt.show()

#Breakdown for Thalium Stress Test

x=(health_data.thall.value_counts())
print(x)
p = sns.countplot(data=health_data, x="thall")
plt.show()

#Density distribution for Age                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
plt.figure(figsize=(10,10))                                                                                                                                     
sns.displot(heart.age, color="red", label="Age", kde= True)
plt.legend()                                                                   