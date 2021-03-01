import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python&sort=i"


def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    print(soup.title.string)
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    print(pages)


def get_jobs():
    jobs = []
    max_pages = extract_pages()
    #jobs = save_jobs(max_pages)
    return jobs