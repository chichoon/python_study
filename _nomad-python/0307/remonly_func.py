import requests
from bs4 import BeautifulSoup

def extract_jobs(url):
    jobs = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.title.string)
    try:
        containers = soup.find_all("section", {"class": "jobs"})
        for container in containers:
            lists = container.find_all("li")
            for l in lists:
                link = l.find("a")["href"]
                title = l.find("span", {"class": "title"}).string
                company = l.find("span", {"class": "company"}).string
                location = l.find("span", {"class": "region"}).string
                jobs.append({
                    "title": title,
                    "link": link,
                    "company": company,
                    "location": location
                })
        return jobs
    except:
        print("No jobs in Remote Only!")
        return jobs
