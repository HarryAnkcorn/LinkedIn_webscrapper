import boto3

def get_file_from_s3(bucketname, file_name):
    s3 = boto3.resource('s3')
    tmp_file = f'/tmp/{file_name}'
    s3.Bucket(bucketname).download_file(file_name, tmp_file)

def save_to_bucket(bucketname, file_name):
    s3 = boto3.resource('s3')
    tmp_file = f'/tmp/{file_name}'
    s3.meta.client.upload_file(tmp_file, bucketname, file_name)

def make_list_from_txt(file_name):
    lst = []
    tmp_file = f'/tmp/{file_name}'
    f = open(tmp_file, 'r', encoding="utf-8")
    for line in f:
        if line != '':
            if line.isupper(): 
                lst.append(line.strip())
    f.close()
    return lst