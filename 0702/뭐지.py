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
print(samples)


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
















