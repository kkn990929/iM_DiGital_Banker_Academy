# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:25:46 2024

@author: campus4D037
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



# 그래프 선의 종류
linestyles = ['-', '--', ':']
def E(X, g=lambda x: x):
    x_set, f = X
    return np.sum([g(x_k) * f(x_k) for x_k in x_set])
def V(X, g=lambda x: x):
    x_set, f = X
    mean = E(X, g)
    return np.sum([(g(x_k)-mean)**2 * f(x_k) for x_k in x_set])
def check_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    assert np.all(prob >= 0), 'minus probability'
    prob_sum = np.round(np.sum(prob), 6)
    assert prob_sum == 1, f'sum of probability{prob_sum}'  
    print(f'expected value {E(X):.4}')
    print(f'variance {(V(X)):.4}')
    
    
def plot_prob(X):
    x_set, f = X
    prob = np.array([f(x_k) for x_k in x_set])
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111)
    ax.bar(x_set, prob, label='prob')
    ax.vlines(E(X), 0, 1, label='mean')
    ax.set_xticks(np.append(x_set, E(X)))
    ax.set_ylim(0, prob.max()*1.2)
    ax.legend()
    plt.show()
    
# 베르누이 분포
# 확률이 0(false) or 1(true)
    
def Bern(p): # p => 기댓값 분산 -> 0.3*(1-0.3)
    x_set = np.array([0,1])
    def f(x):
        if x in x_set :
            return p ** x * (1-p) ** (1-x)
        else:
            return 0
    return x_set, f

p= 0.3
X = (Bern(p))
check_prob(X)
plot_prob(X)
# expected value 0.3
# variance 0.21



# lib를 이용한 베르누이 분포
from scipy.stats import bernoulli
vr = bernoulli(p)
print(vr.pmf(0), vr.pmf(1))

# lib를 이용한 누적밀도함수
print(vr.cdf([0,1]))

# lib를 이용한 평균값 구하기
print(vr.mean())

# lib를 이용한 분산 구하기
print(vr.var())

# 이항분포 = 일정한 확률 p를 가진 독립시행을 n번 반복할 때의 확률분포.
from scipy.special import comb # nCm 같은 조합

def Bin(n,p):
    x_set = np.arange(n+1)
    def f(x):
        if x in x_set :
            return comb(n,x) * p ** x * (1-p) ** (n-x)
        else:
            return 0
    return x_set, f
    

n=10
p=0.3
X = Bin(n,p)
check_prob(X) # expected value 3.0
              # variance 2.1
plot_prob(X)

# p값의 조합(zip)으로 각각 다른 이항 분포 binom(n, p)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
x_set = np.arange(n+1)
for p, ls in zip([0.3, 0.5, 0.7], linestyles):
    rv = stats.binom(n, p)
    ax.plot(x_set, rv.pmf(x_set),
            label=f'p:{p}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()
plt.show()

# 기하분포

def Ge(p):
    x_set = np.arange(1, 30)
    def f(x): # 확률질량함수을 구하는 함수
        if x in x_set : # X 값이 x_set에 있는지 확인
            return p * (1-p) ** (x-1) # 확률질량함수를 구하는 부분 
        else:
            return 0
    return x_set, f


p=0.5
X = Ge(p)
check_prob(X)
plot_prob(X)


# scipy lib 사용한 기하분포 다른 p들의 조합 geom(p)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
x_set = np.arange(1, 15)
for p, ls in zip([0.2, 0.5, 0.8], linestyles):
    rv = stats.geom(p)
    ax.plot(x_set, rv.pmf(x_set),
            label=f'p:{p}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()
plt.show()


# 포아송
# 실패비율을 알고있고 임의의 시점에 실패할 경우의 발생횟수

from scipy.special import factorial
def Poi(lam):
    x_set = np.arange(20)
    def f(x):
        if x in x_set:
            return np.power(lam, x) / factorial(x) * np.exp(-lam)
        else:
            return 0
    return x_set, f



lam = 3
X = Poi(lam)

check_prob(X)
plot_prob(X)

# scipy lib 사용한 포아송 분포 다른 p들의 조합 stats.poisson(lam)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
x_set = np.arange(20)
for lam, ls in zip([3, 5, 8], linestyles):
    rv = stats.poisson(lam)
    ax.plot(x_set, rv.pmf(x_set),
            label=f'lam:{lam}', ls=ls, color='gray')
ax.set_xticks(x_set)
ax.legend()
plt.show()









