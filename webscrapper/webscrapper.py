from os import link
import requests
from bs4 import BeautifulSoup

#Using request package to call URL 
URL ="https://www.indeed.com/jobs?q=Python&limit=60"
indeed_result = requests.get(URL)

#Using Soup package to find html part
indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

#Using soup to fInd pagination ,'a'
pagination = indeed_soup.find("div",{"class":"pagination"})
links = pagination.find_all('a')
pages = []

#Using loop to store all the 'a''s 자식( 'span') and then make string to int
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]

for n  in range(max_page):
    print(f"start={n*50}")


