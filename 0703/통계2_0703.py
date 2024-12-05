# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:09:49 2024

@author: campus4D037
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('ch4_scores400.csv')

scores = np.array(df['score'])

p_mean = np.mean(scores) # 평균
p_var = np.var(scores) # 분산

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

xs = np.arange(101)
rv = stats.norm(p_mean, np.sqrt(p_var)) # 점수에 대한 평균, 표준편차
ax.plot(xs, rv.pdf(xs), color='gray') # 확률 밀도 함수를 계산
ax.hist(scores, bins=100, range=(0, 100), density=True)
plt.show()


# 시드값 설정
np.random.seed(1)

# 추출할 표본갯수
n = 20

# 표본추출
sample = np.random.choice(scores,n)
print(sample)

# unbiased estimator 불편 추출
np.random.seed(50)
n_sample = 10000
samples = np.random.choice(scores,(n_sample,n)) # n개 값 무작위 추출
# print(samples)


for i in range(5):
    s_mean = np.mean(samples[i])
    print(f'{i+1}번째 표본평균 : {s_mean:.3f}') # 소수 세 번째 까지 표시
    
    # 결과
    # 1번째 표본평균 : 72.900
    # 2번째 표본평균 : 64.750
    # 3번째 표본평균 : 70.200
    # 4번째 표본평균 : 70.450
    # 5번째 표본평균 : 75.350


# 표본평균이 모평균을 잘 추정하는지 확인
sample_means = np.mean(samples, axis=1) # 축값 1 = 열로 설정
print(np.mean(sample_means))
print(np.mean(np.random.choice(scores, int(1e6)))) # 백만개(1e6)를 뽑는다면
# 결과 69.54619 / 69.510282
# 거의 일치

# 표본평균이 최종적으로 좋은 일치성과 불편성을 가지고 있다.
s_mean = np.mean(sample)
print(s_mean)
# 결과 68.3



# 표본 분산

for i in range(5):
    s_var = np.var(samples[i])
    print(f'{i+1}번째 표본분산 : {s_var:.3f}') # 소수 세 번째 까지 표시

# 결과
# 1번째 표본분산 : 271.728
# 2번째 표본분산 : 242.648
# 3번째 표본분산 : 271.988
# 4번째 표본분산 : 257.460
# 5번째 표본분산 : 256.127

# 모분산 확인
# 표본분산이 모분산을 잘 추정하는지 확인

sample_vars = np.var(samples, axis=1) # 축값 1 = 열로 설정
print(np.mean(sample_vars))

# 결과 195.872875 결과과 상이 할 경우 seed값 조절하기

# 불편분산 추출
u_var = np.var(sample, ddof=1)
# ddof = 자유도 조정 파라미터로, n-1로 나누어 표본 분산을 계산
# 모집단 분산의 불편 추정량을 제공
print(u_var)


# -------------------------0703-------------------------

print('-------------------------07/03-------------------------')

# 점추정을 바탕으로 한 모수값 포함 예상 구간(신뢰구간)추정 

# ex) 사전투표

from scipy import stats
# 모평균을 알고 있는 상태에서 Upper Lower을 구하는 경우
rv = stats.norm()
lcl = s_mean - rv.isf(0.025) * np.sqrt(p_var/n) # 신뢰 하한(Lower)구간 = 0.025
ucl = s_mean - rv.isf(0.975) * np.sqrt(p_var/n) # 신뢰 상한(Upper(구간 = 0.975

print(lcl, ucl)

# 모평균 포함 여부 확인
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
rv1 = stats.norm()# 정규 분포 객체를 생성
n_samples = 20
ax.vlines(p_mean, 0, 21)
for i in range(n_samples):
    sample_ = samples[i] # 추출
    s_mean_ = np.mean(sample_) # 평균계산
    lcl = s_mean_ - rv1.isf(0.025) * np.sqrt(p_var/n) # 신뢰하한(Lower)구간
    ucl = s_mean_ - rv1.isf(0.975) * np.sqrt(p_var/n) # 신뢰상한(Upper)구간
    if lcl <= p_mean <= ucl: # 신뢰구간 내
        ax.scatter(s_mean_, n_samples-i, color='gray')
        ax.hlines(n_samples-i, lcl, ucl, color='gray')
    else: # 신뢰구간 외
        ax.scatter(s_mean_, n_samples-i, color='b')
        ax.hlines(n_samples-i, lcl, ucl, color='b')
ax.set_xticks([p_mean])
ax.set_xticklabels(['population mean'])
plt.show()

# 파란선(이상치) = 모평균을 추청하고 있지 않음


# 추가 setting
      

# rv1 = stats.norm()
# cnt = 0
# for sample_ in samples:
#     s_mean_ = np.mean(sample_)
#     lcl = s_mean_ - rv.isf(0.025) * np.sqrt(p_var/n)
#     ucl = s_mean_ - rv.isf(0.975) * np.sqrt(p_var/n)
#     if lcl <= p_mean <= ucl:
#         cnt += 1
# print(cnt / len(samples) )  # 0.9483 => 약 95%의 모평균 추정




# 모평균을 모르는 상태
# 표본분산을 카이제곱 분포로 변환 + 확률밀도함수로 변환
sample_u_vars = np.var(samples, axis=1, ddof=1)
np.mean(sample_u_vars)
sample_y = sample_u_vars * (n-1) / p_var


fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)

xs = np.linspace (0,40,100)
rv2 = stats.chi2(df = n-1)
ax.plot(xs, rv2.pdf(xs), color = 'gray')
hist,_,_ = ax.hist(sample_y, bins = 100, range = (0,40) , density = True)

plt.show()




# 모평균을 모르는 경우 신뢰 하한, 상한구하는 경우
rv3 = stats.chi2(df=n-1)
lcl = (n-1) * u_var / rv3.isf(0.025)
hcl = (n-1) * u_var / rv3.isf(0.975)
print(lcl, hcl)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111)
rv3 = stats.chi2(df=n-1) # 카이제곱 검정
n_samples = 20
ax.vlines(p_var, 0, 21)
for i in range(n_samples):
    sample_ = samples[i]
    u_var_ = np.var(sample_, ddof=1)
    lcl = (n-1) * u_var_ / rv3.isf(0.025) # 신뢰하한(Lower) 구간
    ucl = (n-1) * u_var_ / rv3.isf(0.975) # 신뢰상한(Upper) 구간
    if lcl <= p_var <= ucl:
        ax.scatter(u_var_, n_samples-i, color='gray')
        ax.hlines(n_samples-i, lcl, ucl, 'gray')
    else:
        ax.scatter(u_var_, n_samples-i, color='b')
        ax.hlines(n_samples-i, lcl, ucl, 'b')
ax.set_xticks([p_var])
ax.set_xticklabels(['population variance'])
plt.show()



# 모분산을 모르는 상황 -> 모평균의 구간추정을 통해 신뢰구간추정
# 
rv4 = stats.chi2(df=n-1)
cnt = 0
for sample_ in samples:
    u_var_ = np.var(sample_, ddof=1)
    lcl = (n-1) * u_var_ / rv4.isf(0.025) # 자유도 n-1 LOWER
    ucl = (n-1) * u_var_ / rv4.isf(0.975) # 자유도 n-1 UPPER 
    if lcl <= p_var <= ucl:
        cnt += 1
print(cnt / len(samples)) # 0.9623


# 모분산을 알지 못할 때의 신뢰구간 구하는 방법
rv5 = stats.t(df=n-1)
lcl = s_mean_ - rv.isf(0.025) * np.sqrt(p_var/n)
ucl = s_mean_ - rv.isf(0.975) * np.sqrt(p_var/n)

print(lcl, ucl)


















