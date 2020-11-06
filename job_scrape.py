from os import system
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from collections import Counter
import re
import os.path
from func_extract import *
from func_transform import *
system('cls')

path = r'C:\Users\Harry\Desktop\Personal_Projects\LinkedIn_webscrapping\job_folder'
url = 'https://www.linkedin.com/jobs/search?keywords=Junior%2BData%2BEngineer&location=United%2BKingdom&geoId=101165590&trk=public_jobs_jobs-search-bar_search-submit&f_E=2&f_TP=1&redirect=false&position=1&pageNum=0&sortBy=DD&currentJobId=2268720529'

page_html = web_scrap(url)
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li",{"class":"result-card job-result-card result-card--with-hover-state"})

white_list = load_white_list()
complete_tally = []
count = 0

for container in containers:
    count += 1
    print(count)
    
    temp_url = container.a["href"]
    
    time = container.div.div.time
    time_test = container.div.div.time['datetime']

    page_html = web_scrap(temp_url)

    page_soup = soup(page_html, "html.parser")

    job_description = page_soup.find("div",{"class":"show-more-less-html__markup show-more-less-html__markup--clamp-after-5"})
    job_description = job_description.get_text('\n')
    job_description = transform_job(job_description)
    
    for word in white_list:
        if word in job_description:
            complete_tally.append(word)

cnt = Counter(complete_tally)
print(cnt)

# file_name = f"file_{count}.txt"
# file_name = os.path.join(path, file_name) 
# f = open(file_name, "a", encoding="utf-8")
# f.write(f"{temp_url} \n{time} \n{time_test} \n{job_description}")
# f.close()


# words_list = all_words.split(' ')
# black_list = ['','THE', 'A', 'TO', 'FROM', 'AN', 'THIS', 'OF', 'OR', 'AND', 'A']
# for word in words_list:
#     if word in black_list:
#         words_list.remove(word)

# cnt = Counter(words_list)
# cnt = cnt.items()
# first_30 = list(cnt)[:30]
# print(cnt)

# f = open("test_list.txt", "a",encoding="utf-8")
# for word in cnt.keys():
#     f.write(f"{word}\n")
# f.close()