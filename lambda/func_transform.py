import re

def get_number_of_results(page_soup):
    try:
        results_number = page_soup.find("meta",{"content":"website"})
        results_number = results_number.link.title.get_text('')
        results_number = int(results_number[:3].strip()) # this is technical debt
    except:
        results_number = 0
    return results_number

def transform_job(job_description):
    job_description = job_description.replace('\n',' ')
    job_description = job_description.replace(' go ',' ')
    job_description = job_description.upper()
    job_description = job_description.replace("E.G",'EG')
    job_description = job_description.replace("'RE",'RE')
    job_description = job_description.replace("'T",'T')
    job_description = job_description.replace("'S",'S')
    job_description = job_description.replace("'LL",'LL')
    job_description = job_description.replace("'VE",'VE')
    job_description = job_description.replace("'M",'M')
    job_description = job_description.replace("'D",'D')
    job_description = job_description.replace("’RE",'RE')
    job_description = job_description.replace("’T",'T')
    job_description = job_description.replace("’S",'S')
    job_description = job_description.replace("’LL",'LL')
    job_description = job_description.replace("’VE",'VE')
    job_description = job_description.replace("’M",'M')
    job_description = job_description.replace("’D",'D')
    job_description = job_description.replace('C#','CSHARP')
    job_description = job_description.replace('+','PLUS')
    job_description = re.sub(r'[^\w]', ' ', job_description)
    job_description = job_description.replace(' PL SQL ',' PLSQL ')
    job_description = job_description.replace(' BIG DATA ',' BIGDATA ')
    job_description = job_description.replace(' POWER BI ',' POWERBI ')
    job_description = job_description.replace(' MACHINE LEARNING ',' ML ')
    job_description = job_description.replace(' DATA WAREHOUSE ',' DATAWAREHOUSING ')
    job_description = job_description.replace(' DATA WAREHOUSING ',' DATAWAREHOUSING ')
    job_description = job_description.replace(' DATA MINING ',' DATAMINING ')
    job_description = job_description.replace(' GRADIENT BOOST',' GRADIENTBOOSTING ')
    job_description = job_description.replace(' NEURAL NETWORK',' NEURALNETWORK ')
    job_description = job_description.replace(' DATALAKES ',' DATA LAKES ')
    job_description = job_description.replace(' RANDOM FOREST ',' RANDOMFOREST ')
    job_description = job_description.replace(' SCIKIT LEARN ',' SCIKITLEARN ')
    job_description = job_description.replace(' GOOGLE CLOUD PLATFORM', 'GCP')
    job_description = job_description.replace(' DATA SCIENCE ', ' DATASCIENCE ')
    job_description = job_description.replace(' CONPUTER SCIENCE ',' CONPUTERSCIENCE ')
    job_description = job_description.replace(' DATAMODELLING ', 'DATAMODELLING')
    job_description = job_description.replace(' MODEL ', 'DATAMODELLING')
    job_description = job_description.replace(' MODELLING ', 'DATAMODELLING')
    job_description = job_description.replace(' CLOUD COMPUTING ', ' CLOUDCOMPUTING ')
    job_description = job_description.replace(' CLOUD SERVICES ', ' CLOUDCOMPUTING ')
    job_description = job_description.replace(' CLOUD BASED ', ' CLOUDCOMPUTING ')
    job_description = job_description.replace(' WEB SCRAPING ', 'WEBSCRAPING')
    job_description = job_description.replace(' A I ', ' AI ')
    job_description = job_description.split(' ')

    return job_description

def on_zi_list(job_description, white_list):
    tally_list = []
    for word in white_list:
        if word in job_description:
            tally_list.append(word)
    return tally_list