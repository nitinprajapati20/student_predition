# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
import pickle

df=pd.read_csv("D:/predction/student analysis.csv");

lb_make=LabelEncoder()
df['genders']=lb_make.fit_transform(df['gender'])
finaldf=df.drop(['gender'],axis='columns')
finaldf.head(10)
finaldf.rename(columns={'math score':'mathscore','chemistry score':'chemistryscore','physics score':'physicsscore'},inplace=True)
finaldf
x=finaldf[['Enrolled','Present','Absent','genders','chemistryscore','mathscore']]
x
y=finaldf[['physicsscore']]
y  

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.3)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,y_train)

pickle.dump(model,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))