# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:38:02 2024

@author: campus4D037
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
data1 = pd.read_csv('scores_reg.csv')
n = len(data1)
x1 = data1['quiz']
x2 = data1['sleep_time']
y = data1['final_test']
p = 2


# 독립변수 1,2 절편값 추정
X = np.array([np.ones_like(x1), x1, x2]).T
beta0_hat, beta1_hat, beta2_hat = np.linalg.lstsq(X, y ,rcond=None)[0]
beta0_hat, beta1_hat, beta2_hat

# 예측값 및 잔차
y_hat = beta0_hat + beta1_hat * x1 + beta2_hat * x2
eps_hat = y - y_hat


# 모분산 추정 with  var
s_var = np.sum((eps_hat ** 2) / (n-p-1))


C0, C1, C2 = np.diag(np.linalg.pinv(np.dot(X.T, X)))


# 신뢰구간 구하기
rv = stats.t(n-p-1) # 여기 원래 n-2인데 n값 정의 안됨
lcl = beta0_hat - rv.isf(0.025) * np.sqrt(s_var * C2) # 신뢰구간 상한선 -5.62
hcl = beta0_hat - rv.isf(0.975) * np.sqrt(s_var * C2) # 신뢰구간 하한선 1.880
print(lcl, hcl)

# t test
t = beta1_hat / np.sqrt(s_var * C2)
print(t) # 3.615
# p-value
p = (1-(rv.cdf(t))) * 2
print(p) # 0.002135369988011



