import requests
from bs4 import BeautifulSoup
from indeed_func import extract_indeed_pages, extract_indeed_jobs
#자주 쓸 코드를 함수화하여 불러옴

max_indeed_pages = extract_indeed_pages()
print(max_indeed_pages)

extract_indeed_jobs(max_indeed_pages)