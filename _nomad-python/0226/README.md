# 2월 26일 (금요일) Python 챌린지 5

## BeautifulSoup
- from bs4 import BeautifulSoup
- soup = BeautifulSoup(html_doc, 'html-parser')
    - html에서 데이터를 추출하는 역할
    - soup를 만들어두면 soup.find를 이용해서 특정 키워드를 찾을 수 있다
- soup.find("키워드") : 해당 키워드를 가진 값 찾아서 return
    - {"class": "클래스명"} 식으로 클래스명을 이용해서 결과를 좁힐 수도 있음
- soup.find_all("키워드") : 해당 키워드를 가진 모든 값 찾아서 리스트 형태로 return