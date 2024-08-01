# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:09:56 2024

@author: campus4D037
"""
from selenium  import webdriver
from selenium.webdriver.chrome.service import Service as ChormeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome(service=ChormeService(ChromeDriverManager().install()))

driver.get('https://finance.naver.com/marketindex/?tabSel=exchange#tab_section')

# 페이지 특징 파악
# iframe 개체는 반드시 스위칭 후에 UI Element로 접근
driver.switch_to.frame('frame_ex1')

# X-PATH로 환율 정보 추출
currency_body = driver.find_element(By.XPATH, '/html/body/div/table')

for i in currency_body.find_elements(By.TAG_NAME , 'tr'):
    print(i.text)
    
    
# 데이터를 리스트에 저장
list_currency = []
for tr in currency_body.find_elements(By.TAG_NAME ,'tr'):
    list_currency.append(tr.text.split())
    
    