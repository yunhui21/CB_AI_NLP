# Day_02_03_kma.py

import requests
import re

url = 'https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId-100'
recvd = requests.get(url)
# print(recvd)
# print(recvd.text)

# temp = re.findall(r'<province>.+</province>', recvd.text)
# print(temp)
# print(len(temp))

# 문제
# loacation 데이터를 갖고 오세요.
# 기본 : 탐욕적 greedy,(.+)
#       비탐욕적 non-greedy(.+?)
location = re.findall(r'<location wl_ver="3">.+?</location>', recvd.text, re.DOTALL)
# print(len(location))

for loc in location:
    # print(loc)
    # 문제
    # province를 찾아서 출력해 보세요.
    # city 를 찾아서 출력해 보세요.

    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    print(prov[0], prov)
    print(city[0])

    # data를 찾아 보세요.
    data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
    # print(data)
    # print(len(data))

    for datum in data:
        # print(datum)
        # 문제
        # mode를 비롯한 나머지를 찾아 보세요.
        mode = re.findall(r'<mode>(.+)</mode>', datum)
        tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
        wf   = re.findall(r'<wf>(.+)</wf>', datum)
        tmn  = re.findall(r'<tmn>(.+)</tmn>', datum)
        tmx  = re.findall(r'<tmx>(.+)</tmx>', datum)
        # reli = re.findall(r'<reliability>(.+)</reliability>', datum)
        rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)
        print(mode[0], tmEf[0], wf[0], tmn[0],tmx[0],rnSt[0])
        # print(mode[0])
        # print(tmEf[0])
        # print(  wf[0])
        # print( tmn[0])
        # print( tmx[0])
        # # print(reli[0])
        # print( rnSt[0])