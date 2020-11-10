from datetime import date
import csv

def load_csv(amount_of_jobs,count, cnt):
    today = date.today()
    data = [today, amount_of_jobs, count, cnt]
    print(data)
    write_to_csv(data)

def write_to_csv(data):
    with open('jobs.csv', 'a+', newline = '\n') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        linewriter.writerow(data)