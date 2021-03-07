import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def save_jobs(url):
    job_list = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.title.string)
    container = soup.find("div", {"class": "page"}).find("table", {"id": "jobsboard"})

    jobs = container.find_all("tr", {"class": "job"})

    for job in jobs:
        td = job.find("td", {"class": "company_and_position_mobile"})
        title = td.find("h2").get_text(strip=True)
        if title != None:
            company = td.find("h3").string
            link = "https://remoteok.io/l/"+job["data-id"]
            job_list.append({
                "title": title,
                "company": company,
                "link": link,
                "site" : "♠ Remote Only"
                })
    return job_list

def get_jobs(word):
    url = f"https://remoteok.io/remote-{word}-jobs"
    jobs = save_jobs(url)
    return jobs