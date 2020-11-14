from datetime import date
import boto3
import csv

def append_to_csv(amount_of_jobs, count, cnt):
    today = date.today()
    data = [today, amount_of_jobs, count, cnt]
    print(data)
    write_to_csv(data)

def write_to_csv(data):
    with open('/tmp/job_data.csv', 'a+', newline = '\n') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        linewriter.writerow(data)