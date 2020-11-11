import matplotlib
import csv
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ast
from collections import defaultdict
import boto3

data = []

def graphing(event, context):
    bucketname = 'linkedinwebscrap' # replace with your bucket name
    s3 = boto3.resource('s3')
    newfile = f'/tmp/job_data.csv'
    s3.Bucket(bucketname).download_file('job_data.csv', newfile)

    print('here')
    
    with open('/tmp/job_data.csv', 'r') as csvfile: # make this /tmp/ in lambda
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            data.append(row)

    dates = []
    amount_of_jobs = []
    skills = ['PYTHON', 'SQL', 'AWS']
    skill_results = defaultdict(list)

    for row in data:
        date_lst = row[0].split('-')
        dates.append(date(int(date_lst[0]),int(date_lst[1]),int(date_lst[2])))
        
        amount_of_jobs.append(int(row[1]))

        day_tally = row[3].strip('"Counter()')
        day_tally = ast.literal_eval(day_tally)
        for word in skills:
            if word not in day_tally:
                skill_results[word].append(0)
            else:
                skill_results[word].append(day_tally[word])

    plt.figure(figsize=(9, 4))
    ax = plt.gca()
    formatter = mdates.DateFormatter("%Y-%m-%d")
    ax.xaxis.set_major_formatter(formatter)
    locator = mdates.DayLocator()
    ax.xaxis.set_major_locator(locator)
    plt.xlabel('Date')

    plt.ylabel('Results')
    for word in skill_results:
        plt.plot(dates, skill_results[word], label = word)       
    plt.legend(skill_results.keys())

    plt.grid()
    plt.savefig('/tmp/plot.png', bbox_inches = 'tight')
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/plot.png', 'linkedinwebscrap', 'plot.png')