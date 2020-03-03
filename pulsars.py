# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 14:28:44 2020

@author: Erik
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


#First open and read the data to examine it:
pulsars = pd.read_csv('pulsar_stars.csv')

print(pulsars.head())
print(pulsars.info())
print(pulsars.describe())