# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 09:04:58 2024

@author: campus4D037
"""

import numpy as np
import pandas as pd
# 표본추출
print(np.random.choice([1,2,3],3)) # 리스트 안의 숫자를 n개 만큼 무작위 추출 (무작위 추출)

print(np.random.choice([1,2,3],3 , replace = False)) # 비복원 무작위 추출

# Random Seed 값
np.random.seed(0)

print(np.random.choice([1,2,3],3)) # 숫자는 랜덤 but 배열은 고정


data1 = pd.read_csv('ch4_scores400.csv')


data2 = np.array(data1['score'])


# 확률분포 구하기 with 공정한 주사위, 불공정한 주사위

# 공정한 주사위
dice1 = [1,2,3,4,5,6]

# 불공정한 주사위
dice2 = [1/21, 2/21, 3/21, 4/21, 5/21, 6/21]

# 시도횟수
trial = 100
sample = np.random.choice(dice1, trial, p=dice2)
print(sample)

import matplotlib as mpl #한글로 표현
import matplotlib.pyplot as plt # 그래프 서식 조절
import seaborn as sns # 시각화
import pandas as pd


fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot(111) # 이미지를 넣는 방법?
ax.hist(data2 , bins=100, range=(0,100),density=True ) 
# bins 는 계열막대별 범위 range는 값 범위 density는 정규화
ax.set_xlim(20,100)
ax.set_ylim(0,0.042)
ax.set_xlabel('score')
ax.set_ylabel('re_freg')
# plt.show()




import numpy as np
# 주사위 확률 구하기
x_set = np.array([1,2,3,4,5,6])
def f(x):
    if x in x_set:
        return x/21
    else :
        return 0
    
    
x_in = [x_set, f]

prob = np.array([f(x_k) for x_k in x_set])    
    

dict1 = dict(zip(x_set,prob))

print(dict1)

x_data = list(dict1.keys())
y_data = list(dict1.values())

fig,ax = plt.subplots(figsize = (8,5))
# histogram은 숫자세기 bar는 x수치 y 수치 나타내기
ax.bar(x_data, y_data, width = 0.5, align= 'center', alpha = 0.5)
# alpha = 투명도
ax.set_xlabel('Scores')
ax.set_ylabel('Probability')
ax.set_title('Histogram of Scores with Relation')


# 기대값
print(np.sum([x_k * f(x_k) for x_k in x_set]))
plt.show()


# choice로 기대값 구하기 at 실무
sample = np.random.choice(x_set, int(1e6), p = prob)
print(sample.mean())



# shuffle -> 일차적인 편향제거를 위해 사용 at choice

#------------분산--------------
# 람다 함수 이름이 없는 함수를 만들때 사용 lambda
# lambda 매개변수 : 출력값

def E(x, g=lambda x:x): # X는 주사위의 눈 + 각 주사위 눈 별 확률
    x_set , f = x
    return np.sum(g(x_k) * f(x_k) for x_k in x_set)

# 기본 확률변수 계산
E(x_in, g=lambda x:2*x +3)
# 2**2V(x)= V(2X+3)
# 분산값 계산
def V(x, g=lambda x:x): # g = lambda 매개변수 : 출력값(return) 람다함수를 V()의 매개변수로 사용
    x_set, f = x
    mean = E(x , g)
    return np.sum([(g(x_k)-mean)**2 * f(x_k) for x_k in x_set])

mean = E(x_in) 
print(V(x_in, lambda x:2*x +3)) 
# 람다함수 정의해놓고 값을 받아서 리턴값을 받아서 함수 선언 반복 필요없이 
# 같은 함수 내의 매개변수에 lambda삽입
# 합수 변경시 해당 함수내의 Lambda와 최종 출력값 Lambda 변경


# 상관관계 확인 1. 상관계수 2. Scatter(산점도)


# 공분산 Cov(Covariation)
def Cov(XY):
    x_set, y_set, f_XY = XY #XY값을 가져와서 3개로 분할
    mean_x = E(XY, lambda x,y: x)
    mean_y = E(XY, lambda x,y: y)
    return np.sum([(x_i-mean_x) * (y_j-mean_y) * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set])




# for문이 2개 => 중첩for문 2차원
# 중첩for문
# 이중for문
# ex) for -> 행담당
    #   for -> 열담당
    # 열 구분 우선 반복 후 -> 행 구분 반복 실행
    # ex) 9x9 구구단 표
















