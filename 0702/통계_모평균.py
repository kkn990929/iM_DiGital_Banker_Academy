# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 10:19:17 2024

@author: campus4D037
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 그래프 서식 조절



data1 = pd.read_csv('ch4_scores400.csv')


data2 = np.array(data1['score'])

data2_means = [np.random.choice(data2,20).mean() for _ in range(10000)]

fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot(111) # 이미지를 넣는 방법?
ax.hist(data2 , bins=100, range=(0,100),density=True ) 
# bins 는 계열막대별 범위 range는 값 범위 density는 정규화
ax.vlines(np.mean(data2) ,0 ,1,'gray' )
ax.set_xlim(20,100)
ax.set_ylim(0,0.042)
ax.set_xlabel('score')
ax.set_ylabel('re_freg')
plt.show()


