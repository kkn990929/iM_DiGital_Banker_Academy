# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 13:16:54 2024

@author: campus4D037
"""

# https://search.naver.com/search.naver?nso=&page=페이지 넘버&query=검색어sm=tab_pge&start페이지번호*15+11&where=web

from bs4 import BeautifulSoup
import requests

input_search = input('검색어 입력 : ')
page = int(input('검색할 페이지 : '))


# 페이지 지정시 계산 부분
new_page = 0
if page == 1:
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={input_search}'
elif page == 0:
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={input_search}'
else:
    new_page = (page-2) * 15 + 1
    url = f'https://search.naver.com/search.naver?nso=&page={page}&query={input_search}&sm=tab_pge&start={new_page}&where=web'
print(url)

# 헤더  
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
# User-Agent = 브라우저가 웹 서버에 자신을 식별
search_url = requests.get(url, headers = header)

# Beautifulsoup
html = BeautifulSoup(search_url.text, "html.parser")

# 태그 정보 확인
data = html.find_all('div')
for i in data:
    t = i.find('a')
# ext_data = html.select("li.sp_nnews> div.news_wrap > div.dsc_wrap >div.dsc_txt_wrap")


# div.group_news > ul.list_news > li.news_wrap_api_ani_send >div.news_area> div.news_contents > a.news_dsc










