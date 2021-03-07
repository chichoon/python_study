import requests
from bs4 import BeautifulSoup


def extract_pages(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.title.string)
    try:
        pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
        last_page = pages[-2].get_text(strip=True)
        return int(last_page)
    
    except:
        print("No pages found in StackOverflow!")
        return 0
    

def extract_jobs(html):
    title = html.find("h2", {"class" : "mb4"}).find("a")["title"]
    company, location = html.find("h3", {"class": "mb4"}).find_all("span", recursive = False)
    company = company.get_text(strip=True)
    job_id = html["data-jobid"]
    return {"title": title, 
            "company": company, 
            "link": f"https://stackoverflow.com/jobs/{job_id}",
            "site" : "★ StackOverFlow"
            }


def save_jobs(url, last_page):
    jobs = []
    for page in range(last_page):
        print(f"☆Scrapping page {page} :")
        result = requests.get(f"{url}&pg={page + 1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class":"-job"})
        for res in results:
            jobs.append(extract_jobs(res))
    return jobs


def get_jobs(word):
    url = f"https://stackoverflow.com/jobs?q={word}&sort=i"
    jobs = []
    max_pages = extract_pages(url)
    if max_pages != 0:
        jobs = save_jobs(url, max_pages)
    return jobs