# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:49:31 2024

@author: campus4D037
"""

# encoding
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
data1 = pd.read_csv('scores_reg.csv')
n = len(data1)

formula = 'final_test ~ quiz + sleep_time + school_method' #school_method는 Series형태라 회귀분석 어려움
result = smf.ols(formula, data1).fit()
print(result.summary()) # summary를 보는 이유 -> 적합한 Algorithm를 찾으려고


