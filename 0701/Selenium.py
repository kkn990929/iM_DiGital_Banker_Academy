# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:34:38 2024

@author: campus4D037
"""

from selenium  import webdriver
from selenium.webdriver.chrome.service import Service as ChormeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChormeService(ChromeDriverManager().install()))


# 원하는 사이트의 url 정보입력 (get함수)
driver.get('https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0014780158')

# find_element를 사용하여 조건제시
fir_data = driver.find_element(By.id, 'ID')

# fir_data내의 모든 요소들을 리스트 저장
sec_data = fir_data.find_elements(By.XPATH , '//*[@id="main_content"]/div[2]/div/dl/dt[2]/a')


