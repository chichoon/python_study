from flask import Flask, render_template, request, redirect, send_file
from sof_func import get_jobs as sof_get_jobs
from remonly_func import get_jobs as remote_get_jobs
from wwr_func import get_jobs as wework_get_jobs
from indeed_func import get_jobs as indeed_get_jobs
from save_func import save_to_file

app = Flask("Python")

db = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return "contact me"

@app.route("/<username>")
def usr(username):
    return f"hello, {username}!"

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.lower()
        existing_jobs = db.get(word)
        if existing_jobs:
            jobs = existing_jobs
        else:
            jobs = sof_get_jobs(word) + indeed_get_jobs(word) + wework_get_jobs(word) + remote_get_jobs(word)
        db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", 
        SearchingBy=word, 
        resultsNum=len(jobs),
        jobs=jobs)

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return send_file(word + ".csv")
    except:
        return redirect("/")

app.run(host="0.0.0.0")
