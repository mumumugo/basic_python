from os import link
import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=PYTHON&{LIMIT}"

def extract_indeed_pages():
    result = requests.get(URL)
    #Using Soup package to find html part
    soup = BeautifulSoup(result.text,"html.parser")

    #Using soup to fInd pagination ,'a'
    pagination = soup.find("div",{"class":"pagination"})
    links = pagination.find_all('a')
    pages = []

    #Using loop to store all the 'a''s 자식( 'span') and then make string to int
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page
    for n  in range(max_page):
        print(f"start={n*50}")

# def extract_indeed_jobs(last_page):
#     jobs = []
#     for page in range(last_page):
#         result = requests.get(f"{URL}&start = {0*LIMIT}")
#         soup = BeautifulSoup(result.text, "html.parser")
#         results = soup.find_all("h2", {"class": "jobTitle"})
#     print(results)
#     return jobs
#     #for result in results:
#        # title  = result.find("div", {"class": "title"}).find("a")["title"]
#        # print(title)
#     #return jobs

    #print(result.status_code)