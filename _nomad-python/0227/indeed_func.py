import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = "https://kr.indeed.com/jobs?q=python"

def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.title.string) #page title
    pagination = soup.find("div", {"class": "pagination"})
    #div라는 키워드를 포함하고, class가 pagination인 요소 검색

    links = pagination.find_all("a")
    #결과값이 담긴 list

    pages = []
    for link in links[:-1]: #맨 끝의 값 제외
        pages.append(int(link.find("span").string))
    #span이 포함된 page 내의 값들에 들어있는 string을 int로 변환하여 리스트에 저장

    max_page = pages[-1]
    #총 페이지 수 (가장 큰 페이지 넘버)
    return max_page


def extract_job(html):
    '''
    title = html.find("h2", {"class": "title"})
    actual_title = title.find("a")["title"]
    print(actual_title)
    '''
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    #한줄로 뭉쳐줌
    company = html.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        #회사명에 링크가 달려있는 것과 아닌 것을 구분
        if company_anchor is not None:
            company = company_anchor.string
            #링크가 있을 때
        else:
            company = company.string
            #링크가 없을 때
        company = company.strip()
        #\n 삭제 (줄옮김 삭제)
    else:
        company = None
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    #[] 괄호 안에 있는 것 : attribute
    return {"title" : title, "company" : company, "location" : location, "link" : f"https://www.indeed.com/viewjob?jk={job_id}"}
    #딕셔너리 return
    

def save_jobs(last_page):
    jobs = [] #빈 리스트 선언
    for page in range(last_page):
        print(f"★Scrapping page {page} :")

        result = requests.get(f"{URL}&start={LIMIT * page}")
        soup = BeautifulSoup(result.text, "html.parser")
        #각 페이지마다 soup 이용해서 html 파싱
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
        for res in results:
            #results는 soup 내의 soup 요소들이 들어있는 list이므로, 
            #results 내의 원소 res는 모두 soup와 같이 쓸 수 있다
            jobs.append(extract_job(res))
    return jobs


def get_jobs():
    max_pages = extract_pages()
    jobs = save_jobs(max_pages)
    return jobs