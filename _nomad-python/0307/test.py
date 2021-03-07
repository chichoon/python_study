from flask import Flask, render_template, request, redirect, send_file
from sof_func import get_jobs as sof_get_jobs
from remonly_func import get_jobs as remote_get_jobs
from wwr_func import get_jobs as wework_get_jobs
from indeed_func import get_jobs as indeed_get_jobs
from save_func import save_to_file

app = Flask("Python")

db = {}
#fake db

@app.route("/")
def home():
    return render_template("index.html")
#root에 접근했을 때 출력되는 텍스트 (html 형식으로 적으면 html 태그대로 출력됨)
#@는 데코레이터로, 이것이 사용된 라인 바로 아래 줄에서 함수를 찾아서 실행시킴

@app.route("/contact")
def contact():
    return "contact me"
#contact에 접근했을 때 텍스트가 출력되도록 함
#함수 이름은 접근할 페이지 이름과 상관없음

@app.route("/<username>")
def usr(username):
    return f"hello, {username}!"
#<> 는 Placeholder로, 안에 들은 값이 밑의 함수의 인자로 들어간다
#이렇게 입력했을 경우, 127.0.0.1:5000/이름 입력하면 hello, 이름! 이라고 화면에 표시됨

@app.route("/report")
def report():
    word = request.args.get("word")
    #word 에 해당하는 query argument를 가져옴 (form에서 입력받은 값)
    #request.args는 dictionary를 return하므로, get 이용하여 key에 해당하는 value 추출
    if word:
        word = word.lower()
        #word에 값이 존재할 때 소문자로 변환
        existing_jobs = db.get(word)
        if existing_jobs:
            #이미 데이터베이스에 word가 존재할 경우
            jobs = existing_jobs
        else:
            #데이터베이스에 자료가 없을 경우
            jobs = sof_get_jobs(word) + indeed_get_jobs(word) + wework_get_jobs(word) + remote_get_jobs(word)
        db[word] = jobs
        #데이터베이스에 등록
    else:
        return redirect("/")
        #값이 없으면 root로 리다이렉트
    return render_template(
        "report.html", 
        SearchingBy=word, 
        resultsNum=len(jobs),
        jobs=jobs)
    #SearchingBy 변수를 report.html에 넘겨주며 실행시킴

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
            #try문에서 빠져나가 except문으로 감
        word = word.lower()
        #검색한 값 소문자로 변환
        jobs = db.get(word)
        #어차피 result 화면에서 export로 이동할 것이기 때문에 
        #또 크롤링할 필요 없이 이미 값이 데이터베이스에 존재
        if not jobs:
            raise Exception()
            #위와 같은 에러 처리
        save_to_file(jobs, word)
        return send_file(word + ".csv")
    except:
        return redirect("/")
        #word에 값이 없을 경우 (빈칸일 경우) 홈으로 되돌아감
        #if word: else: 와 같은 역할함

app.run()
#repl.it 사용 시에는 host="0.0.0.0"
#vscode 이용하여 localhost 접속시에는 127.0.0.1 (기본값)
