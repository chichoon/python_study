import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def save_jobs(url):
    jobs = []
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    
    print(soup.title.string)
    containers = soup.find_all("section", {"class": "jobs"})
    for container in containers:
        lists = container.find_all("li")
        for l in lists:
            title = l.find("span", {"class": "title"})
            if title:
                title = title.get_text()
                anchors = l.find_all("a")
                if len(anchors) == 1:
                    link = "https://weworkremotely.com" + l.find_all("a")[0]["href"]
                else:
                    link = "https://weworkremotely.com" + l.find_all("a")[1]["href"]
                company = l.find("span", {"class": "company"}).get_text()
                jobs.append({
                    "title": title,
                    "company": company,
                    "link": link,
                    "site" : "☆ WeWorkRemotely"
                })
    return jobs


def get_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    jobs = save_jobs(url)
    return jobs