import requests
from bs4 import BeautifulSoup
from indeed_func import get_jobs as get_indeed_jobs
from sof_func import get_jobs as get_sof_jobs
#자주 쓸 코드를 함수화하여 불러옴
from save_func import save_to_file

indeed_jobs = get_indeed_jobs()
sof_jobs = get_sof_jobs()
jobs = indeed_jobs + sof_jobs
#return 받은 두 list 합치기
save_to_file(jobs)
#csv 형식으로 데이터 저장
print("Done saving files!")