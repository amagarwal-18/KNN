#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 10:39:31 2018

@author: amitagarwal
"""

import os
import pandas as pd
os.getcwd()


df = pd.read_csv('dc_airbnb.csv')
print(df.head())