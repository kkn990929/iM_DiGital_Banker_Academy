# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:23:00 2024

@author: campus4D037
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate # 적분

x_range = np.array([0,1])

def f(x):
    if x_range[0] <= x <= x_range[1]:
        return 2 * x # 0~1 구간에서는 2X
    else:
        return 0 # 0~1 구간 넘어가면 0으로 반환
    
X = [x_range, f] # f = 확률변수에 대한 함수
xs = np.linspace(x_range[0], x_range[1], 100)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(xs, [f(x) for x in xs], label='f(x)', color='gray')
ax.hlines(0, -0.2, 1.2, alpha=0.3) # 가로선, alpha = 투명도
ax.vlines(0, -0.2, 2.2, alpha=0.3) # 세로선, alpha = 투명도
ax.vlines(xs.max(), 0, 2.2, linestyles=':', color='gray')
# 0.4부터 0.6 까지 x좌표를 준비
xs = np.linspace(0.4, 0.6, 100)
# xs의 범위로 f(x)와 x축으로 둘러싸인 영역을 진하게 칠함
ax.fill_between(xs, [f(x) for x in xs], label='prob')
ax.set_xticks(np.arange(-0.2, 1.3, 0.1))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.2, 2.1)
ax.legend()
plt.show()



print(integrate.quad(f, 0.4, 0.6)) # 확률밀도함수 구하는 식


# https://matplotlib.org/
# https://scipy.org/


from scipy.optimize import minimize_scalar # 최소값 0값으로 설정되어있음
res = minimize_scalar(f)
print(res.fun)
print(integrate.quad(f, -np.inf, np.inf)[0])

# 누적 적분
def F(x):
    return integrate.quad(f, -np.inf, x)[0]

print(F(0.6) - F(0.4)) 

xs = np.linspace(x_range[0], x_range[1], 100)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(xs, [F(x) for x in xs], label='F(x)', color='gray')
ax.hlines(0, -0.1, 1.1, alpha=0.3)
ax.vlines(0, -0.1, 1.1, alpha=0.3)
ax.vlines(xs.max(), 0, 1, linestyles=':', color='gray')
ax.set_xticks(np.arange(-0.1, 1.2, 0.1))
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 1.1)
ax.legend()
plt.show()




# y의 확률밀도함수
y_range = [3,5]
def g(y):
    
    if y_range[0] <= y <= y_range[1]:
        return (y-3) / 2
    else:
        return 0

# 확률분포함수
def G(y):
    return integrate.quad(g, -np.inf, y)[0]
ys = np.linspace(y_range[0], y_range[1], 100)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
ax.plot(ys, [g(y) for y in ys],
        label='g(y)', color='gray')
ax.plot(ys, [G(y) for y in ys],
        label='G(y)', ls='--', color='gray')
ax.hlines(0, 2.8, 5.2, alpha=0.3)
ax.vlines(ys.max(), 0, 1, linestyles=':', color='gray')
ax.set_xticks(np.arange(2.8, 5.2, 0.2))
ax.set_xlim(2.8, 5.2)
ax.set_ylim(-0.1, 1.1)
ax.legend()
plt.show()