import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&sort=i"


def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.title.string)
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    #s-pagination class의 div 태그가 붙은 html 요소 중 a (anchor) 태그의 요소만 저장
    last_page = pages[-2].get_text(strip=True)
    #strip=True는 양 옆의 공백 등을 제거해줌
    return int(last_page)
    #get_text는 html 내의 모든 텍스트를 추출 (태그 제거 후 문자열만 반환)
    #string은 html 내의 텍스트 하나를 반환 (자식 태그가 여러개라 문자열이 여러개면 None 반환)
    

def extract_jobs(html):
    title = html.find("h2", {"class" : "mb4"}).find("a")["title"]
    company, location = html.find("h3", {"class": "mb4"}).find_all("span", recursive = False)
    #recursive = False : span 내의 span 내의 span... 을 반복적으로 가져오지 않게 함
    #(첫 번째 span에 해당하는 요소만 갖고오게 함)
    #list 내 요소가 2개라는 것을 이미 알고 있으면, 위와 같이 각각의 변수에 값 집어넣을 수 있다
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html["data-jobid"]
    return {"title": title, 
            "company": company, 
            "location": location,
            "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
            }


def save_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"☆Scrapping page {page} :")
        result = requests.get(f"{URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for res in results:
            jobs.append(extract_jobs(res))
    return jobs



def get_jobs():
    jobs = []
    max_pages = extract_pages()
    jobs = save_jobs(max_pages)
    return jobs