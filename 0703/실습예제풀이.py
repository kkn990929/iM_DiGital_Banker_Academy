# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:07:08 2024

@author: campus4D037
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(1111)
# 예제 = 감튀무게 130g(모평균)이어야 하는데 5일동안 사본 감튀 평균 무게가 128.45(표본평균)임 이건 우연일까?
en_f = pd.read_csv('potato.csv')
en_df = np.array(en_f['무게'])

s_mean = en_df.mean()  # 128.45

# 모평균 130g  표본평균 14개

# n(130,9) => N(130, 9/14)

# 표본평균 P(bar X <= X) = 0.05

rv = stats.norm(130, np.sqrt(9/14))
print(rv.isf(0.95))  # 상위 5% => 128.6

# 결론 = p(bar X <= 128.68) 은 5%확률
# 귀무가설 기각역 p -value < 0.05
# 귀무가설 채택역 p -value > 0.05

# 검정통계량과 임계량


# 검정통계량
z = (s_mean - 130) / np.sqrt(9/14) # -1.93
print(z)

# 임계량
rv = stats.norm()
print(rv.interval(0.95)) # (-1.95 , 1.95)

# 검정통계량 > 임계값 => 귀무가설 채택

# P 값 기준 문제 해결하기
# 1. 문제제기
# 2. 가설 설정
# 3. 유의수준 파악 
# 4. 검정통계량 계산
# 5. p-value 계산 (stat.cdf())
        # 귀무가설 기각역 p -value < 0.05
        # 귀무가설 채택역 p -value > 0.05


# 양측검정
# 기각역이 정규분포 양쪽에 위치


# 양측검정의 p값
print(rv.cdf(z)*2) #cdf는 x가 주어지면 y값을 반환 0.053


# 가설검정의 오류
# 1종 오류
# 실제로 ‘평균이 130g’인데도 ‘평균은 130g보다 작다’라는 결론을 내리는 상황
# 본래 검출하지 말아야 할 것을 검출한 것이므로 오탐(false positive) 안 걸렸는데 걸렸다고 하는거
# 위험률 : 제 1종 오류를 범하는 확률 a
# False Positive = Predict -> Positive / Acutal -> Negative
# 1종 오류를 위한 계산
rv = stats.norm(130, 3)
c = stats.norm().isf(0.95)
n_samples = 10000
cnt = 0
for _ in range(n_samples):
    sample_ = np.round(rv.rvs(14), 2)
    s_mean_ = np.mean(sample_)
    z = (s_mean_ - 130) / np.sqrt(9/14)
    if z < c:
        cnt += 1
print(cnt / n_samples) # 0.0528 False Negative


# 제 2종 오류
# 실제로 ‘평균이 130g보다 작다’인데도 ‘평균은 130g보다 작다’라는 결론을 얻을 수 없는 상황
# 본래 검출해야 하는 것을 검출하지 못했으므로 미탐(false negative)
# False Negative = Predict -> Negative / Acutal -> Positive
rv = stats.norm(128,3) # 정규분포의 크기 128, 표준표차값 3
c = stats.norm().isf(0.95) # 상위 5%값 계산
n_samples = 10000 # 샘플갯수
cnt = 0 # 카운트값
for _ in range(n_samples):
    sample_ = np.round(rv.rvs(14), 2) # 크기가 14인 샘플 추출 후 소수점 둘째 자리까지 반올림
    s_mean_ = np.mean(sample_) # 샘플 평균 추출
    z = (s_mean_ - 130) / np.sqrt(9/14) # z검정 통계량 계산
    if z >= c: # 검정통계량이 상위 5%보다 크면
        cnt += 1 # 카운트 +1
print(cnt / n_samples) #0.197 10000개 중 1970개





# 혼동  행렬 (Confusion Matrix)
# Sensitivity 결과는 Positive 인데 Negative / Positive로 예측한 것중 Positive -> 민감도 (재현율) ex) 사람목숨(암진단) 
# Precision  결과는 Positive / Negative인데 Positive로 예측한 것 중 결과가 Positive인것 -> 정밀도


# F!-score

# {재현율 * 정밀도 / (재현율 + 정밀도)} * 2




















