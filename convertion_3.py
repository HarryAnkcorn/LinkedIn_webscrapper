from os import system
from collections import Counter
import re
system('cls')

f = open("example_text.txt", "r", encoding="utf-8")
job_description = f.read()
f.close()

white_list = []
f = open("white_list.txt", "r", encoding="utf-8")
for line in f:
    if line != '':
        if line.isupper(): 
            white_list.append(line.strip())
f.close()

job_description = job_description.replace('\n',' ')
job_description = job_description.replace(' go ',' ')
job_description = re.sub(r'\d', ' ', job_description)
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
job_description = job_description.replace(' MACHINE LEARNING ',' MACHINELEARNING ')
job_description = job_description.replace(' DATA WAREHOUSE ',' DATAWAREHOUSING ')
job_description = job_description.replace(' DATA WAREHOUSING ',' DATAWAREHOUSING ')
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

all_words = ""
all_words += job_description

words_list = all_words.split(' ')

cnt = Counter(words_list)

# f = open("convertion_text.txt", "a", encoding="utf-8")
# f.write(f"{all_words}")
# f.close()

# f = open("test_list.txt", "a", encoding="utf-8")
# for word in cnt.keys():
#     f.write(f"{word}\n")
# f.close()

for word in list(cnt):
    if word not in white_list:
        del cnt[word]

print(cnt.most_common(51))

# f = open("test_dict_2.txt", "a", encoding="utf-8")
# for item in cnt.most_common(300):
#     f.write(f"{item}\n")
# f.close()