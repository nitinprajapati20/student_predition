# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:39:16 2020

@author: admin
"""

import requests

url= 'http://localhost:5000/predict_api'
r= requests.post(url,json={'Enrolled':2, 'Present':7, 'Absent':5, 'genders':0, 'chemistryscore':5, 'mathscore':2})

print(r.json())
