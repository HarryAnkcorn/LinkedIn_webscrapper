from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def web_scrap(url):
    uclient = urlopen(url)
    page_html = uclient.read()
    uclient.close()
    return page_html

def soupifie(page_html):
    pass

def load_white_list():
    white_list = []
    f = open("white_list.txt", "r", encoding="utf-8")
    for line in f:
        if line != '':
            if line.isupper(): 
                white_list.append(line.strip())
    f.close()
    
    return white_list