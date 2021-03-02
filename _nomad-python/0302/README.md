# 3월 1일 (월요일) Python 챌린지 7
   
## Django
- Python 기반 웹 프레임워크
- 파이썬만 사용해서 Frontend에 Backend API를 만들 수 있음
- 커뮤니티 규모가 크고 툴 성능이 좋다

## *args, **kwargs
- positional arguments, keyword arguments
- argument 개수를 정해놓지 않고 원하는 만큼 무제한으로 argument를 넣고 싶다면?
- *args를 인자로 받는 함수는 여러 개의 argument를 tuple로 받아옴
- **kwargs를 인자로 받는 함수는 여러 개의 argument와 keyword를 dictionary로 받아옴

## 객체지향 프로그래밍
- 코드를 정리하는 형식
- Class를 사용
    - 설계도를 하나 만들어 두면 제품을 여러 개 만들 수 있는 것처럼, Class를 하나 만들어 두면 Instance를 여러 개 찍어낼 수 있다
- Java, Dart, Swift 등이 객체지향

## Method
- Class 안에 정의된 함수
- Instance를 정의 후 함수를 사용할 때 자동으로 argument가 하나 들어간다
    - 해당 argument 자리에는 함수를 호출한 Instance가 들어감
- Class 내에는 기본적으로 내장된 method들이 몇 개 있음 (__어쩌구저쩌구__같은 형태)
    - 예를 들면 __init__은 Instance가 처음 생성될 때 실행
    - __str__은 Instance를 string처럼 이용하려 할 때 실행 (print(Instance) 등)
    - 이러한 기본 method들은 override해서 자기가 원하는 방식대로 동작하도록 재정의할 수 있음