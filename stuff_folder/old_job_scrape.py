from os import system
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from collections import Counter
import re

system('cls')

url = 'https://www.linkedin.com/jobs/search/?f_E=2&geoId=101165590&keywords=junior%20data%20engineer&location=United%20Kingdom'

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
    job_description = job_description.get_text()
    # job_description = re.sub(r'[^\w]', ' ', job_description.upper())
    job_description = job_description.upper()
    job_description = job_description.replace('.','')
    all_words += job_description

words_list = all_words.split(' ')
# black_list = ['','THE', 'A', 'TO', 'FROM', 'AN', 'THIS', 'OF', 'OR', 'AND', 'A']
# for word in words_list:
#     if word in black_list:
#         words_list.remove(word)

cnt = Counter(words_list)
# cnt = cnt.items()
# first_30 = list(cnt)[:30]
# print(cnt)

f = open("test_list.txt", "a",encoding="utf-8")
for word in cnt.keys():
    f.write(f"{word}\n")
f.close()