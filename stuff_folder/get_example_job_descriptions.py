from os import system
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from collections import Counter
import re

system('cls')

url = 'https://www.linkedin.com/jobs/search?keywords=Junior%2BData%2BEngineer&location=United%2BKingdom&geoId=101165590&trk=public_jobs_jobs-search-bar_search-submit&f_E=2&f_TP=1&redirect=false&position=1&pageNum=0&sortBy=DD&currentJobId=2268720529'

uclient = urlopen(url)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li",{"class":"result-card job-result-card result-card--with-hover-state"})

all_words = ""
count = 0

for container in containers:
    count += 1
    print(count)
    
    temp = container.a["href"]

    uclient = urlopen(temp)
    page_html = uclient.read()
    uclient.close()

    page_soup = soup(page_html, "html.parser")

    job_description = page_soup.find("div",{"class":"show-more-less-html__markup show-more-less-html__markup--clamp-after-5"})
    job_description = job_description.get_text('\n')

    all_words += job_description
    all_words += '\n'

f = open("new_example_text.txt", "a", encoding="utf-8")
f.write(f"{all_words}")
f.close()