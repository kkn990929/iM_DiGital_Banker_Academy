# 도로교통공단_결빙사고 다발지역  https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests
import json
from bs4 import BeautifulSoup
#-------------------------------------------------인코딩-------------------------------------------------
# 인코딩 할때는 encoding KEY
# service_key = "go0bibZ87csOHnFB4cntqyibhgCeNnCsWN9Su9WCS7WJ9teykuU1tkybs7KvHLRNApFpKHjNSq23uSdCNO9aaw%3D%3D"
# url = f"http://apis.data.go.kr/B552061/frequentzoneFreezing/getRestFrequentzoneFreezing?ServiceKey=인증키&type=json&searchYearCd=2017&siDo=11&guGun=110&numOfRows=10&pageNo=1"
# response = requests.get(url)
# content = response.json()
# parsed_data = json.loads(response.text)
# print(parsed_data,type(parsed_data))
#-------------------------------------------------디코딩-------------------------------------------------
# 디코딩 할때는 Decoding KEY
url = 'http://apis.data.go.kr/B552061/frequentzoneFreezing/getRestFrequentzoneFreezing'
service_key = "go0bibZ87csOHnFB4cntqyibhgCeNnCsWN9Su9WCS7WJ9teykuU1tkybs7KvHLRNApFpKHjNSq23uSdCNO9aaw=="
params ={'serviceKey' : service_key,
          'type' : 'json',
          'searchYearCd' : 2017,
          'siDo' : 11,
          'guGun' : 110,
          'numOfRows' : 10,
          'pageNo' : 1 }
response = requests.get(url, params=params)
parsed_data = json.loads(response.text)
print(parsed_data,type(parsed_data))

body = parsed_data['items']['item']
print(body)

import pandas as pd
# from pandas.io.json import json_normalize
data = pd.json_normalize(body)
print(data)