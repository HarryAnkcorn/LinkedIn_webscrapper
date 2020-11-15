# linkedin_webscraper
A web scrapping app to track terms in linkedin job adverts.

It runs on 2 separate lambdas and is deployed through serverless and git actions.

1. job scrape lambda

    Purpose: Samples the 25 most relevant junior data engineering roles listed on LinkedIn and tallies the words from words_to_track.csv that is then updated on a job_data.csv. Both files are on a S3 bucket  
    Trigger: 0530 everyday  
    Reads: words_to_track.txt  
    Writes: job_data.csv  

2. plot lambda

   Purpose: Creates and saves a matplotlib graph as a image. The graph plots the frequency of words in the words_to_plot.txt and job_data.csv against the date  
   Trigger: updating of job_data.csv  
   Reads: job_data.csv, words_to_plot.txt  
   Writes: plot.png  
