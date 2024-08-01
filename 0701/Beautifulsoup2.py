# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 17:18:57 2024

@author: campus4D037
"""

import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text,'lxml')

print(soup.title)
print(soup.title.get_text())

print('---------------------------------')

print(soup.a) # HTML문서에서 첫번째 a태그 값을 가져옴
print('---------------------------------')

print(soup.a.attrs) # 첫번째 a href의 attribute 가져옴

print('---------------------------------')

print(soup.a["href"])
print(soup.a["class"])
print(soup.a["tabindex"])