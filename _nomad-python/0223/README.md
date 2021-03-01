# 2월 23일 (화요일) Python 챌린지 2

## 직접 함수 만들기
- def funcname():
- 그리고 함수 내용은 indent (공백 4개) 를 주고 안쪽에 작성
- 한번 만들어두면 무한정 사용가능

## 함수에 argument (인자) 넣기
- def funcname(arg1, arg2, ...):
- 인자에 기본값을 주는 방법
    - def funcname(arg1 = 'default', arg2 = 'default')
    - 함수 사용 시에 인자를 제대로 넣지 않아도 default 값이 들어가므로 제대로 실행됨

## 함수에서 return값 받기
- 함수 끝에 return 변수명
- return 키워드 안 붙이면 default 값으로 None이 출력
- return은 함수를 종료시킴 (함수의 끝을 의미 - lifecycle 끝)

## Keyworded Arguments
- 인자의 위치에 따라서 정해지는 것이 아닌 인자의 이름으로 값이 지정됨
- funcname(arg2 = 5, arg1 = 3) -> 정상 작동 (arg2 위치에 5를, arg1 위치에 3을 넣는다)
- 인자의 순서를 기억하지 않아도 적절한 곳에 인자를 넣을 수 있어 좋음

## string 사이에 인자 넣기
- f"hello {arg1} is {arg2}" -> arg1과 arg2가 자동으로 들어감
    - 맨 앞의 f 붙이는 것 주의!
- "hello" + arg1 + "is" + arg2 보다 간편