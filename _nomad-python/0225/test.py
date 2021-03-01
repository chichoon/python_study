import math

print(math.ceil(1.5623626))
#올림
print(math.floor(1.35135126))
#내림
print(math.fabs(-5.5))
#절대값

from math import ceil
#math 내의 ceil 함수만을 불러옴
print(ceil(1.55555))
#math.ceil 대신 ceil로 바로 사용 가능

print("-------------requests-------------")
import requests
indeed_result = requests.get("https://github.com/chichoon")
print(indeed_result)
#response[200] -> 통신이 되었다는 의미

print(indeed_result.text)
#주소에 해당하는 모든 html 소스를 출력함