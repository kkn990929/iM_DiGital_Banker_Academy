# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:51:25 2024

@author: campus4D037
"""
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('life_expectancy.csv')

# df2= pd.read_csv('C:/users/campus4D037/iM DiGital Bank/DATAS/life_expectancy.csv')
# 파일 주소로도 불러올 수 있음

print(df1.describe())   # 수치확인
print(df1.info()) # 구조, 타입, 결측치 확인


extract_df = df1[['Life expectancy', 'Year' , 'Alcohol' , 'Percentage expenditure']]
print(extract_df.shape) # (2938, 4)

print(extract_df.isnull().sum()) # 결측치 갯수 확인
# isnull은 T/F로 변환 sum은 T값의 총합 계산


print('-----------결측치 처리 후-----------')
extract_df.dropna(inplace = True)
print(extract_df.isnull().sum())

# 상관관계 lib
import seaborn as sns
sns.set(rc = {'figure.figsize':(12, 10)})
correlation_matrix= extract_df.corr().round(2)
sns.heatmap(data = correlation_matrix, annot = True) # annot => 주석
plt.show()

# pairplot
sns.pairplot(extract_df)
plt.show()














