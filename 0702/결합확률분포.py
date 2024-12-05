# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:04:08 2024

@author: campus4D037
"""

import numpy as np
import matplotlib.pyplot as plt
# 결합 확률 함수
x_set = np.arange(2,13)
y_set = np.arange(1,7)
# np.arange 함수는 특정 범위 내에서 일정한 간격으로 값을 생성하여 배열을 만드는 데 사용됩니다

def f_XY(x,y):
    if 1<=y<=6  and 1<=x-y<=6:
        return y * (x-y) / 100
    else:
        return 0
    
XY = [x_set, y_set, f_XY]

#히트맵 정보 확인
prob = np.array([[f_XY(x_i, y_j) for y_j in y_set] for x_i in x_set])

fig = plt.figure(figsize=(10,9))
ax = fig.add_subplot(111)

c = ax.pcolor(prob)

ax.set_xticks(np.arange(prob.shape[1]) + 0.5, minor=False)
ax.set_yticks(np.arange(prob.shape[0]) + 0.5, minor=False)
ax.set_xticklabels(np.arange(1,7) , minor=False)
ax.set_yticklabels(np.arange(2,13) , minor=False)

ax.invert_yaxis()
ax.xaxis.tick_top()
fig.colorbar(c, ax=ax)
plt.show()

print(np.all(prob>=0)) #prob의 전체(all)가 0 이상인가? TRUE


# x에 대한 주변확률값
# 특정 부분만 확률값 알고 싶을때
def f_X(x):
    return np.sum([f_XY(x, y_k) for y_k in y_set])
def f_Y(y):
    return np.sum([f_XY(x_k, y) for x_k in x_set])

X = [x_set, f_X]
Y = [y_set, f_Y]

prob_x = np.array([f_X(x_k) for x_k in x_set])
prob_y = np.array([f_Y(y_k) for y_k in y_set])

fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.bar(x_set, prob_x)
ax1.set_title('x-marginal probability dist.')
ax1.set_xlabel('x_value')
ax1.set_ylabel('probability')

ax2.bar(y_set, prob_y)
ax2.set_title('y-marginal probability dist.')
ax2.set_xlabel('y_value')
ax2.set_ylabel('probability')
plt.show()


# 1차원 기대값으로 2차원 확률변수 기대값 구하기
print(np.sum([x_i * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set]))

# 2차원 데이터(x,y)에서 1차원 기대값(x or y) 구하기
def E(XY ,g):
    x_set ,y_set, f_XY = XY 
    return np.sum([g(x_i,y_j) * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set])
    
# 기대값 구하기
mean_x = E(XY , lambda x,y : x)
mean_y = E(XY , lambda x,y : y)

print(mean_x)    
print(mean_y)

# 평균값 -> 분산 -> 공분산 -> 상관관계(상관계수)

# 평균을 이용해 분산값 구하기

def V2(XY ,g):
    x_set, y_set, f_XY =XY
    mean = E(XY, g)
    return np.sum([(g(x_i, y_j)-mean)**2 * f_XY(x_i , y_j) for x_i in x_set for y_j in y_set]) # xy값 가져와서 구하기


# 공분산값 구하기
def Cov(XY):
    x_set, y_set, f_XY = XY #XY값을 가져와서 3개로 분할
    mean_x = E(XY, lambda x,y: x)
    mean_y = E(XY, lambda x,y: y)
    return np.sum([(x_i-mean_x) * (y_j-mean_y) * f_XY(x_i, y_j) for x_i in x_set for y_j in y_set]) 
# 각 값에 가중치 곱해서 구하기

cov_xy = Cov(XY)
print(cov_xy)


# 공분산을 이용해 상관계수 구하기 at 히트맵
var_x = V2(XY, g=lambda x, y : x) # x의 분산
var_y = V2(XY, g=lambda x, y : y) # y의 분산
print(cov_xy/np.sqrt(var_x * var_y))  # 공분산 / sqrt[분산*분산](표준편차)







