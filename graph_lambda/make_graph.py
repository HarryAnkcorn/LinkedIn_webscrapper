# import matplotlib
# import csv
# from datetime import date
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import ast
# from collections import defaultdict
# import boto3
from bucket_functions import get_file_from_s3, save_to_bucket
from reading import make_list_from_csv, make_list_from_txt, tally_skills, make_graph

def graphing(event, context):
    bucketname = 'linkedinwebscrap'
    data_file_name = 'job_data.csv'
    graph_file_name = 'plot.png'
    words_file_name = 'words_to_plot.txt'

    get_file_from_s3(bucketname, data_file_name)
    get_file_from_s3(bucketname, words_file_name)

    data = make_list_from_csv(data_file_name)
    skills = make_list_from_txt(words_file_name)

    dates, skill_results = tally_skills(data, skills)

    make_graph(dates, skill_results, graph_file_name)

    save_to_bucket(bucketname, graph_file_name)