# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:20:05 2024

@author: campus4D037
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
df1 = pd.read_csv('scores_reg.csv')
n = len(df1)

df1['mid_test']  = df1['quiz'] * 2 # 중간고사 = 기말고사 * 2
print(df1)

formula = 'final_test ~ quiz + mid_test'
result = smf.ols(formula, df1).fit()
print(result.summary()) # Cond. No. : 1.22e+17 -> 값이 커짐 -> 다중공선성 의심

# 그럴경우 한쪽 변수를 제거 해야 or 새로운 파생변수를 만들기 ex)두 변수의 평균값 만들기

