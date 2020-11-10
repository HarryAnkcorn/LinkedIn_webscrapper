from os import system
from collections import Counter
import os.path
from func_extract import web_scrap, load_white_list
from func_transform import get_number_of_results, transform_job, on_zi_list
from func_load import load_csv

system('cls')

url = 'https://www.linkedin.com/jobs/search/?f_E=2&f_TP=1&geoId=101165590&keywords=junior%2Bdata%2Bengineer&location=United%2BKingdom&sortBy=R&redirect=false&position=1&pageNum=0'

page_soup = web_scrap(url)

results_number = get_number_of_results(page_soup)

white_list = load_white_list()

count = 0
complete_tally = []

url_check = [] # this can go soon

containers = page_soup.findAll("li",{"class":"result-card job-result-card result-card--with-hover-state"})

for container in containers:   
    temp_url = container.a["href"]

    url_check.append(temp_url)# this can go soon

    try:
        page_soup = web_scrap(temp_url)
        count += 1
    except:
        continue

    print(count)

    job_description = page_soup.find("div",{"class":"show-more-less-html__markup show-more-less-html__markup--clamp-after-5"})
    job_description = job_description.get_text('\n')
    job_description = transform_job(job_description)

    tally = on_zi_list(job_description, white_list)
    complete_tally.extend(tally)

cnt = Counter(complete_tally)
load_csv(results_number, count, cnt)

# this can go soon
f = open("job_sample.txt", "a", encoding="utf-8")
for url in url_check:
    f.write(f"{url}\n")
f.close()