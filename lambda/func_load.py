from datetime import date
import boto3
import csv

def load_csv(amount_of_jobs,count, cnt):
    today = date.today()
    data = [today, amount_of_jobs, count, cnt]
    print(data)
    get_csv()
    write_to_csv(data)
    save_to_bucket()

def get_csv():
    bucketname = 'linkedinwebscrap' # replace with your bucket name
    s3 = boto3.resource('s3')
    newfile = f'/tmp/job_data.csv'
    s3.Bucket(bucketname).download_file('job_data.csv', newfile)

def write_to_csv(data):
    with open('/tmp/job_data.csv', 'a+', newline = '\n') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        linewriter.writerow(data)

def save_to_bucket():
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/job_data.csv', 'linkedinwebscrap', 'job_data.csv')