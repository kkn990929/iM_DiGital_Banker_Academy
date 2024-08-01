# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 13:50:01 2024

@author: campus4D037
"""

# 회귀분석

# 단순 회귀분석


# 데이터의 패턴

# y = ax + b 
# y = Label , x = 특징
#
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


# 독립변수가 2개 이상일때의 초기 설정방법
# x1 = df['quiz']
# x2 = df['sleep_time']
# y = df['final_test']
# p = 2

# X = np.array([np.ones_like(x1), x1, x2]).T
# beta0_hat, beta1_hat, beta2_hat = np.linalg.lstsq(X, y)[0]
# beta0_hat, beta1_hat, beta2_hat





# 산점도
# x,y축에 대한 관계 파악
poly_fit = np.polyfit(x, y, 1) # X Y의 1차 선형 다향식
poly_1d = np.poly1d(poly_fit) # 차원을 처리함 1d, 2d ,3d ...

# poly_fit : 다항식 계수 찾기
# poly1d : 연산처리
xs = np.linspace(x.min(), x.max()) # X 최소값 최대값으로 선 그어줌 linspace
ys = poly_1d(xs)


fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.set_xlabel('quiz')
ax.set_ylabel('final test')
ax.plot(xs, ys, color='gray',
        label=f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x')
ax.scatter(x, y)
ax.legend() # 범례 추가
plt.show()



# 오차계산 with 오차항
formula = 'final_test ~ quiz'
result = smf.ols(formula, data1).fit()
print(result.summary()) # OLS 회귀 결과(OLS Regression Results)

# Dep. Variable: 종속변수 이름
# Model : Ordinary list Squerars
# Method: Least Squares (회귀방법 = 최소 제곱법)
# No. Observations: 데이터 갯수
# Df Residuals: : 잔차 / df = 자유도 = 독립변수의 수
# R-squared : 결정계수 독립변수가 종속변수의 변동성 설명
# Adj. R-squared : 조정 결정계수 
# F-statistic : 모델 전체의 유의성 검정 F-통계량
# Prob (F-statistic): F-통계량에 p값 (확률) 추가 값이 작다 = 모델이 유의미하다


# Intercept : quiz가 0일때의 값들
# std err : 절편에 대한 error
# t : 절편에 대한 t값
# [0.025      0.975] : 신뢰구간 LOWER/UPPER
# Omnibus: 잔차에 대한 정규성 검정하는 비통계량 수치 =/Prob(Omnibus)
# coef : 회귀계수
# Durbin-Watson: 자기상관의 실체 at 잔차
# Jarque-Bera (JB): 잔차의 정규성
# Skew: 왜도값 측정 (편향도 측정) /Skewness
# Kurtosis : 첨도
# Cond. No. : 다중공선성 확인

# 잔차 : data와 직선간의 거리값



X = np.array([np.ones_like(x), x]).T # 데이터 array값으로 transform

# 회귀계수를 넣고 각각의 절편과 기울기 값
beta0_hat, beta1_hat = np.linalg.lstsq(X, y, rcond=None)[0] # lstsq최소 제곱법
print(beta0_hat, beta1_hat) # 23.6994 / 6.553
# beta0_hat : 절편
# beta1_hat : 기울기
# y = 6.5x + 23.6

# 선형회귀를 이용한 예측값과 잔차 y_hat =예측값
y_hat = beta0_hat + beta1_hat * x # 예측값과 잔차를 계산
eps_hat = y - y_hat 
# 잔차가 작을수록 예측값 정확해짐

# 모분산 추정 with  var
s_var = np.var(eps_hat, ddof = p+1)
print('모분산 추정치 : ' , s_var) # 134.290


# C0절편, C1기울기
C0, C1 = np.diag(np.linalg.pinv(np.dot(X.T, X)))
print(C0, C1)

# C0절편, C1기울기에 대한 실제 표준오차 (작을수록 좋다)
print(np.sqrt(s_var * C0), np.sqrt(s_var * C1)) # 4.71, 1.06


# 신뢰구간 구하기
rv = stats.t(n-2) # 여기 원래 n-2인데 n값 정의 안됨
lcl = beta0_hat - rv.isf(0.025) * np.sqrt(s_var * C0) # 신뢰구간 상한선 33.609
hcl = beta0_hat - rv.isf(0.975) * np.sqrt(s_var * C0) # 신뢰구간 하한선 13.79
print(lcl, hcl)


# beta1_hat(선형회귀를 사용한 기울기 예측값)
# 귀무가설 : beta1_hat = 0
# 대립가설 : beta1_hat != 0


# t 검정통계량
t = beta1_hat / np.sqrt(s_var * C1)
print(t) # 6.13

# p value

p = (1-(rv.cdf(t))) * 2

print(p) # 8.590875866687497e-06


# p-value < 0.05
# 귀무가설(귀무가설 : beta1_hat = 0) 기각!

# 설명변수 2개이상 일때의 OLS회귀 결과
formula2 = 'final_test ~ quiz + sleep_time'
result2 = smf.ols(formula2, data1).fit()
print(result2.summary()) # OLS 회귀 결과(OLS Regression Results)
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# Intercept     -1.8709     11.635     -0.161      0.874     -26.420      22.678
# quiz           6.4289      0.956      6.725      0.000       4.412       8.446
# sleep_time     4.1917      1.778      2.357      0.031       0.440       7.943

# 여기를 주로 보면 됨






