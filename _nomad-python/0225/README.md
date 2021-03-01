# 2월 25일 (목요일) Python 챌린지 4

## Modules
- 파이썬에 내장된 모듈들이 있고 아니면 pip 이용하여 다운받기도 함
- from 라이브러리명 import 모듈
- 예시) 파이썬 기본 내장 모듈인 **math** 사용 시엔 import math
- pip 이용하여 다운받은 모듈은 from matplotlib import pyplot 등
- import한 모듈 명이 너무 길으면 import matplotlib.pyplot **as plt** 처럼 줄임말을 설정 가능
- 모듈을 한번에 불러오면 묵직하므로 필요한 함수만 쏙쏙 불러와서 사용하는 것이 좋다
- 내가 만든 py 파일 내의 함수들도 from 파일명 import 함수명 으로 불러올 수 있음 (같은 폴더 내에 저장할 시)

## Web scrapper 
- url을 받았을 때 해당 웹 상의 데이터를 추출하는 기능
- 동작 과정
    1. url을 입력 시 사이트에 접속
    2. 해당 사이트에 존재하는 페이지 개수 긁어오기
    3. 모든 페이지를 한 번씩 접속하도록 설정
    4. 원하는 결과를 엑셀 파일로 정리