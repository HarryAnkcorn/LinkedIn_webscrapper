from os import system
from collections import Counter
import re
system('cls')

f = open("example_text.txt", "r", encoding="utf-8")
job_description = f.read()
f.close()

# job_description = re.sub(r'[^\w]', ' ', job_description.upper())

job_description = job_description.replace(' go ',' ')
job_description = job_description.replace('/n',' ')
job_description = job_description.upper()
job_description = re.sub(r'\d', ' ', job_description)
job_description = job_description.replace('.',' ')
job_description = job_description.replace('/n',' ')
job_description = job_description.replace(',',' ')
job_description = job_description.replace('(',' ')
job_description = job_description.replace(')',' ')
job_description = job_description.replace('[',' ')
job_description = job_description.replace(']',' ')
job_description = job_description.replace('{',' ')
job_description = job_description.replace('}',' ')
job_description = job_description.replace('"',' ')
job_description = job_description.replace('“',' ')
job_description = job_description.replace("'RE",'RE')
job_description = job_description.replace("'T",'T')
job_description = job_description.replace("'S",'S')
job_description = job_description.replace("'LL",'LL')
job_description = job_description.replace("'VE",'VE')
job_description = job_description.replace("’RE",'RE')
job_description = job_description.replace("'M",'M')
job_description = job_description.replace("’T",'T')
job_description = job_description.replace("’S",'S')
job_description = job_description.replace("’LL",'LL')
job_description = job_description.replace("’VE",'VE')
job_description = job_description.replace("’M",'M')
job_description = job_description.replace("'",' ')
job_description = job_description.replace('BIG DATA','BIGDATA')
job_description = job_description.replace('!',' ')
job_description = job_description.replace('£',' ')
job_description = job_description.replace('$',' ')
job_description = job_description.replace('%',' ')
job_description = job_description.replace('^',' ')
job_description = job_description.replace('&',' ')
job_description = job_description.replace('*',' ')
job_description = job_description.replace('@',' ')
job_description = job_description.replace('\\',' ')
job_description = job_description.replace('/',' ')
job_description = job_description.replace('|',' ')
job_description = job_description.replace('”',' ')
job_description = job_description.replace('“',' ')
job_description = job_description.replace('’',' ')
job_description = job_description.replace('‘',' ')
job_description = job_description.replace('﻿',' ')
job_description = job_description.replace('-',' ')
job_description = job_description.replace('–',' ')
job_description = job_description.replace(':',' ')
job_description = job_description.replace('…',' ')
job_description = job_description.replace('?',' ')
job_description = job_description.replace('POWER BI','POWERBI')

all_words = ""
all_words += job_description

words_list = all_words.split(' ')

ignore = ['','THE','A','IF','IN','IT','OF','OR','AND','TO','WE','YOU','FOR','OUR','WILL','ARE','BE','IS','AS','ON','THAT','AN',
'I','WORK','HAVE','WORKING','CAN','ROLE','AT','FORM','WITH','YOUR','ALSO','OTHER','THEIR','NEW','ALL','SUPPORT','BASED','LOOKING',
'BY','THIS','NOT','SKILLS','BUSINESS','EXPERIENCE','FROM','DO','TIME','BUT','PEOPLE','MORE','WHO','USING','WITHIN','HELP','ONE',
'US','KNOWLEDGE','WERE','US','WHAT','WELL','OPPORTUNITY','COMPANY','TEAMS', 'YOULL','ENGINEER','OPPORTUNITY','TOOLS','MAKE',
'SYSTEMS', 'BUILDING','PART','NEED','CUSTOMERS','SO','REQUIREMENTS','DAY','BENEFITS','WHERE','BOTH','QUALITY','OFFER','ABOUT',
'ABILITY','INFORMATION','UNDERSTANDING','YEARS','TECHNOLOGIES','SOLUTIONS','TECHNOLOGY','BEST','BUILD','WORLD','THROUGH',
'ENGINEERS','JOIN','WHICH','TECHNICAL','INCLUDING','CODE','UP','PROCESSES','PERSONAL','DEVELOP','PROCESS','AROUND','DIGITAL',
'SUCH','OPPORTUNITIES','SOME','ENSURE','LEVEL','NEEDS','ITS','DEVELOPING','DESIGN','UK','WANT','THEY','RESPONSIBLE','ACROSS',
'CLIENTS','USE','STRONG','APPLICATION','DELIVERY','SYSTEM','GREAT','REMOTE','GET','SUCCESSFUL','EMPLOYEES','RELATED', 'MOST',
'MISSION','SALARY','PROCESSING','PRODUCTS','REQUIRED','LIFE','ABLE','COMFORTABLE','SERVICE','HAS','LEADING','DIVERSITY',
'JOB','ANY','COMMITTED','EVERY','RECRUITMENT','JUST','OUT','PIPELINES','WOULD','KEY','YEAR','ANALYSIS','MANAGEMENT',
'COMMUNITY','PLEASE','CORE','EACH','CULTURE','FOLLOWING','EXCITING','THEM','PROBLEMS','INTO','GROWING','HEALTH','USERS','FURTHER',
'GLOBAL','SHOULD','DEGREE','IDEALLY','OVER','RESPONSIBILITIES','MODELS','TRAINING','SPACE','TAKE','THEN','GOOD','CREATING',
'INCLUSIVE','HOW','WHEN','DAYS','INDUSTRY','FLEXIBLE','REPORTING','PROVIDE','PROJECTS','CREATE','APPLY','ETC','EXPECT','RANGE',
'COLLABORATE','MAY','DISABILITY','HIGH','COMPLEX','THERE','SOMEONE','FAST','STATUS','UNDERSTAND','POSITION','GROW','JUNIOR',
'INTELLIGENCE','FOCUS','CUSTOMER','OPEN','GROWTH','FINANCIAL','RELEVANT','TECH','PLACE','TWO','SUPPORTING','RIGHT','FULL',
'INCLUDE','APPLICATIONS','FUTURE','PRODUCTION','REAL','CURRENTLY','PERFORMANCE','DIVERSE','BRING','FIRST','WAY','IMPORTANT',
'CLEARSCORE','PRACTICES','ESSENTIAL','APPROACH','MANAGE','PROJECT','NOW','PROGRAMMING','DESIRE','PASSION','EARLY','CAREER',
'GROUP','ASK','CANDIDATES','KNOW','COM','GENDER','WEVE','CAPABILITY','DATA','TEAM','ENGINEERING','DEVELOPMENT','ANALYTICS',
'SOFTWARE','SERVICES','PLATFORM','ENVIRONMENT','INFRASTRUCTURE','USER','DEPOP','PRODUCT','NETWORK','AIRBUS','BEING','SERVER',
'SOURCE','ARCHITECTURE','ONLY','CHANGE','EVERYONE','LONG','MUST','SOLVING','EXCELLENT','THAN','DELIVER','COLLEAGUES','PENSION',
'SCHEME','FREE','EQUAL','UNDER','APPLICANTS','AVAILABLE','DONT','END','MAKING','HOME','PROVIDING','DECISIONS','PROGRAMMES',
'ANALYST','DELIVERING','GAIN','LAKE','DATABASES','START','OFFICES','FULLY','COULD','UNITED','MILLION','PROVIDER','SEE',
'INNOVATIVE','ADVANCED','CLOSELY','IMPLEMENTATION','EFFICIENT','CIVIL','MAIN','DESIRABLE','SOCIAL','SEXUAL','ORIENTATION',
'PURPOSES','WRITE','PLATFORMS','INNOVATION','LIKE','WRITING','GYM','SUCCESS','EMPLOYER','INDIVIDUALS','TRADING','DESIGNING',
'SCIENTISTS','STARTUP','SOURCES','BANKING','OPERATION','VIA','FUNCTION','COMMUNICATION','THINGS', 'NEXT','NO','DRIVE','CUTTING',
'EDGE','EXPERIENCED','INTEREST','EQUIVALENT','QUALIFICATIONS','OTHERS','READY','TEST','TOOLING','ACCESS','ANNUAL','PLUS','EMAIL', 
'CV','USED','LARGE','MEET','CONTROL','POSITIVE','IMPACT','VALUES','FIND','CLIENT','CALL','PROUD','LOOK','DEVELOPER','COME',
'MEMBERS','CODING','EVENTS','MENTAL','WHOLE','VARIETY','TOP','VALUE','ROBUST','LEADERSHIP','RUN','WELLBEING','EQUALITY','SITE',
'STANDARD','STUDENTS','SCHOOLS','CONNECT','ALWAYS','EVEN','TIMES','IMPROVE','SECURE','THERES','LANGUAGE','WHY','STATISTICAL',
'CONSTRUCTION','ECONOMETRICS','HOLIDAYS','LOCATION','INTERNAL','TASKS','STANDARDS','PROGRAMS','ONLINE','HARD','WILLINGNESS',
'BECOME','CONNECTING','TREASURY','GATHERING','APP','EXTENSIVE','CLEAR','WORKFORCE','ROLES','CANDIDATE','PACKAGE','WELCOME',
'CONTACT','AGE','BELIEF','ACT','INTEGRITY','EMPLOYMENT','SCALE','ENVIRONMENTS','CONTINUOUS','INTEGRATION','IMPROVEMENT','ENABLE',
'MULTI','BONUS','TERM','ORGANISATION','CONTINUE','SIMPLE','HELPING','LATEST','MATCH','HIGHLY','EFFICIENCY','NUMEROUS','FUN',
'LATEST','MATCH','HIGHLY','EFFICIENCY','NUMEROUS','FUN','BELIEVE','HEALTHCARE','EMPLOYEE','TOWARDS','HOLIDAY','RELIGION','SEX',
'DOING','ADMINISTRATION','PRINCIPLES','COUNTRIES','AREAS','EITHER','TERRAFORM','BALANCE','ALLOW','SURE','CONTROLLER','MANAGING',
'THOSE','CONTRIBUTE','EDUCATION','BEEN','MARKET','UNIVERSITY','BETWEEN','BACK','YOURE','MIGHT','ENABLING','BRIDGEU','HOURS',
'ANALYSTS','BETTER','REPORTS','STAGE','DEMONSTRABLE','ASSISTING','EXPERIAN','EXISTING','APPS','TECHNIQUES','EVOLVE','MEMBER',
'PROGRESSION','EXPERTISE','PROVEN','DISTRIBUTED','ATTITUDE','CHALLENGES','INTERVIEWS','VIRTUAL','TYPE','PROVIDES','RETAIL','LAST'
'RISK','BESPOKE','LAST','RISK','WIDE','ORIENTED','EXPECTED','ANALYTICAL','FORMAL','CERTIFICATIONS','CLEANING','WILLING','EUROPEAN'
'PRIDE','DESCRIPTION','DATE','STEVENAGE','TH','GRADUATE','PROGRAMME','GRADUATES','PERIOD','FAMILIAR','TESTS','ACTIVITIES',
'DEMONSTRATE','COMPUTER','JENKINS','EUROPEAN','PRIDE','COVERING','SUBJECT','NATIONAL','CONFIDENCE','DEPLOYMENT','MEANS','SEEKING',
'MINIMUM','LANGUAGES','PRACTICE','LIVES', 'CREATIVE','POSSIBLE','DEDICATED','ISSUES','EXPERT','ADVANTAGE']
cnt = Counter(words_list)

# f = open("test_list.txt", "a", encoding="utf-8")
# for word in cnt.keys():
#     f.write(f"{word}\n")
# f.close()

for word in list(cnt):
    if word in ignore:
        del cnt[word]

print(cnt.most_common(51))

f = open("test_dict.txt", "a", encoding="utf-8")
for item in cnt.most_common(300):
    f.write(f"{item}\n")
f.close()