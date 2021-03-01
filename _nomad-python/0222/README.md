# 2월 22일 (월요일) Python 챌린지 1

## python python python
- 웹 개발, GUI 개발, 수학/과학 분야, 소프트웨어 개발, 머신러닝, 데이터 시각화 등
- 파이썬 최고

## Django
- Python을 이용해 웹사이트를 만드는 프레임워크

## 자료형
- **Integer** (정수형)
- **String** (문자열)
- **Float** (부동소수)
- **Boolean** (참/거짓)
- **None** (없음)
- 변수 선언 시 이름 규칙 : hello_i_am_chichoon
    - 언더바를 붙여가면서 소문자로 표기
    - 자바스크립트 규칙에 의하면 -> HelloIAmChichoon

## 열거형 자료형
- **List** (리스트 : ['hello', 'byebye']) 가변자료형 _(mutable)_
    - common operation, mutable sequence operation 사용 가능
    - 값에 접근 : list1[0], list1[1], ...
    - 리스트에 값이 있는지 확인 : 'hello' in list1 _(return: bool)_
    - 리스트 길이 확인 : len(list1) _(return: int)_
    - 리스트에 추가 : list1.append('haha')
    - 리스트 항목 삭제 : del(list1[0])
    - 리스트 순서 뒤집기 : list1.reverse()
- **Tuple** (튜플 : ('hello', 'byebye')) 불변자료형 _(immutable)_
    - 리스트와 다르게 common operation만 사용가능
- **Dictionary** (딕셔너리 : {'label1' : 'hello', 'label2' : 'byebye'}) key는 불변, value는 가변
    - Javascript의 Object와 비슷한 느낌
    - 값에 접근 : dict1[label1] ...
    - value 출력 : dict1.get('name')
    - 값 삭제 : del dict1[label1]

## Built-in 함수들
- **함수** : 어떠한 기능을 수행하는 역할을 하며, 어느 때나 반복하여 사용가능
- **Built-in 함수** : 언어 내에 기본적으로 내장된 함수 (따로 라이브러리를 안 불러와도 막 쓸 수 있다)