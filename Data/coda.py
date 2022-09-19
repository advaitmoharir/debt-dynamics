# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:32:03 2020

@author: Student
"""

import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv("Fig12.csv")
x='g-i'
df.plot(kind='scatter',x='g-i',y='d')