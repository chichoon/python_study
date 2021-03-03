# 3월 3일 (수요일) Python 챌린지 9

vscode python 환경에서 templates 읽어오지 못하는 문제 때문에 jupyter notebook 사용

## Flask

- 파이썬으로 웹사이트를 만들 수 있게 해주는 micro framework
- app = Flask("홈페이지 타이틀") 로 불러옴
- 기본적으로 데코레이터와 함께 작동되며, 특정 페이지에 접속했을 때 어떤 화면이 표시될 지 html 태그나 문자열 등을 입력해줄 수 있음
- HTML을 사전에 작성해서 저장해뒀다면 render_template 이용하여 이것을 불러올 수도 있다

## Decorator

- **@** 기호
- 함수를 받아 명령을 추가한 뒤 함수의 형태로 반환하는 함수
- @ 뒤에 붙은 함수의 전처리를 진행하고, 바로 아래의 함수를 실행한 후 @ 뒤의 함수의 후처리를 진행한다
  - 예시: @app.route("/") def blabla(): return "hello"
  - Flask로 만든 간단한 홈페이지의 루트 폴더에 접근했을 때 blabla 함수를 실행한다
- @ 기호로 시작하는 데코레이터 라인 바로 아래 줄에는 함수만이 올 수 있으며, 함수 외의 것들을 적으면 에러가 난다

## Query arguments

- 주소 뒤에 _?word=example_ 식으로 붙은 항목들
- 이것들을 argument로 사용해서 함수 등을 실행하고 결과를 출력하거나 한다
- Placeholder와는 약간 다른 개념인데, 해당 값들을 받아올 땐 request를 사용
