from collections import Counter
# import os.path
from bucket_functions import get_file_from_s3, save_to_bucket, make_list_from_txt
from web_scraping import web_scrape
from func_transform import get_number_of_results, transform_job, on_zi_list
from func_load import append_to_csv

def lambda_handler(event, context):
    url = 'https://www.linkedin.com/jobs/search/?f_E=2&f_TP=1&geoId=101165590&keywords=junior%2Bdata%2Bengineer&location=United%2BKingdom&sortBy=R&redirect=false&position=1&pageNum=0'
    bucketname = 'linkedinwebscrap'
    data_file_name = 'job_data.csv'
    words_file_name = 'words_to_track.txt'

    page_soup = web_scrape(url)

    results_number = get_number_of_results(page_soup)

    get_file_from_s3(bucketname, data_file_name)
    get_file_from_s3(bucketname, words_file_name)
    white_list = make_list_from_txt(words_file_name)

    count = 0
    complete_tally = []

    containers = page_soup.findAll("li",{"class":"result-card job-result-card result-card--with-hover-state"})

    for container in containers:   
        temp_url = container.a["href"]

        try:
            page_soup = web_scrape(temp_url)
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
    append_to_csv(results_number, count, cnt)
    save_to_bucket(bucketname, data_file_name)