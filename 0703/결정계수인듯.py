# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:48:27 2024

@author: campus4D037
"""



"""

                            OLS Regression Results                            
==============================================================================
Dep. Variable:             final_test   R-squared:                       0.676
Model:                            OLS   Adj. R-squared:                  0.658
Method:                 Least Squares   F-statistic:                     37.61
Date:                Wed, 03 Jul 2024   Prob (F-statistic):           8.59e-06
Time:                        16:35:36   Log-Likelihood:                -76.325
No. Observations:                  20   AIC:                             156.7
Df Residuals:                      18   BIC:                             158.6
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     23.6995      4.714      5.028      0.000      13.796      33.603
quiz           6.5537      1.069      6.133      0.000       4.309       8.799
==============================================================================
Omnibus:                        2.139   Durbin-Watson:                   1.478
Prob(Omnibus):                  0.343   Jarque-Bera (JB):                1.773
Skew:                           0.670   Prob(JB):                        0.412
Kurtosis:                       2.422   Cond. No.                         8.32
==============================================================================

"""
# 결정계수 = R-squared
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.formula.api as smf
from sklearn.model_selection import train_test_split
data1 = pd.read_csv('scores_reg.csv')

n = len(data1)
x = np.array(data1['quiz'])
y = np.array(data1['final_test'])
p = 1  


# 오차계산 with 오차항
formula = 'final_test ~ quiz'
result = smf.ols(formula, data1).fit()
# print(result.summary()) # OLS 회귀 결과(OLS Regression Results)

# 예측값 잔차값
# 각각 학생에 대한 예측값
y_hat = np.array(result.fittedvalues)

# 잔차값 eps = 엡실론
eps_hat = np.array(result.resid)
np.sum(eps_hat ** 2)

# 총 변동성
total_var = np.sum((y-np.mean(y))**2)
# 설명 가능한 변동성 = 회귀변동성
exp_var = np.sum((y_hat - np.mean(y)) ** 2)
# 잔차변동
unexp_var = np.sum(eps_hat ** 2)

# 결정계수 구하기
# exp_var / total_var


# 아래 2개 각각 비교
print(exp_var / total_var) # 0.676

print(np.corrcoef(x,y)[0,1] ** 2) # 결정계수 구하는 함수 # 0.676


# 자유도를 조정해서 조정 결정계수 구하기
print(1 - (unexp_var / (n - p - 1)) / (total_var / (n - 1))) # 0.658 각 분모는 자유도를 조정한것


# F-statistic
f = (exp_var / p)  / (unexp_var / (n - p - 1))
print(f) # 37.6
# 잔차위험  = 비체계적위험 = 분산가능 = 설명가능 = exp? = 회귀계수

# Prob (F-statistic)
rv= stats.f(p, n-p-1)
print(1-rv.cdf(f)) # 8.590875866687497e-06 귀무가설 기각


# 우도값 계산
prob = 0.3 # 0의 확률
coin_result = [0, 1, 0, 0, 1]
rv = stats.bernoulli(prob) # 베르누이 확률분포 생성 for 이진 data
L = np.prod(rv.pmf(coin_result)) # 우도확률값 계산
print(L) # 0.03087



# 우도값에 로그를 취하기 우도값은 곱의 연산이라서 우도함수가 최대가 되면 숫자가 작아짐
prob = 0.4 # 0의 확률
rv = stats.bernoulli(prob) # 베르누이 확률분포 생성 for 이진 data
mll2 = np.sum(np.log(rv.pmf([0, 1, 0, 0, 1])))# 우도값에 로그취하기
print(mll2) # -3.365


# 최대 로그우도 계산(함수)
rv = stats.norm(y_hat, np.sqrt(unexp_var / n))
mll = np.sum(np.log(rv.pdf(y)))
print(mll) # -76.32


# AIC(Akaike information criterion) 데이터 품질 평가
# estimator of prediction error
# 2* 회귀계수의 개수 -2 * 최대 로그우도


# BIC(Bayesian information criterion)

# 회귀계수 표본크기에도 가중치 부여 (penalty term for the number of parameters)

aic = -2 * mll + 2 * (p+1) # mll = 최대로그우도 함수  156.65
print(aic)
bic = -2 * mll + np.log(n) * (p+1) # mll = 최대로그우도 함수  158.64
print(bic)

# 왜도 skew
'''
왜도는 분포의 비대칭도를 나타내는 통계량이다. 정규분포, T분포와 같이 대칭인 분포의 경우 왜도가 0이다. 
카이제곱분포와 같이 오른쪽으로 긴 꼬리를 가진 경우(skewed to the right) 왜도는 양수이다. 
왼쪽으로 긴 꼬리를 가지면(skewed to the left) 왜도는 음수
'''

# 첨도 Kurtosis
'''
첨도값(K)이 3에 가까우면 산포도가 정규분포에 가깝다. 
3보다 작을 경우에는(K<3) 산포는 정규분포보다 꼬리가 얇은 분포로 생각할 수 있다, 
첨도값이 3보다 큰 양수이면(K>3) 정규분포보다 꼬리가 두꺼운 분포로 판단할 수 있다.
'''

# 다중공선성 Cond. No.
# 회귀계수에서 분산이 커짐 -> 다중공선성 증가



























