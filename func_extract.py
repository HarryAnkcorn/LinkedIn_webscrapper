from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def web_scrap(url):
    uclient = urlopen(url)
    uclient.addheaders = ('User-agent', 'Mozilla/5.0')
    page_html = uclient.read()
    uclient.close()
    page_soup = soupifie(page_html)
    return page_soup

def soupifie(page_html):
    page_soup = soup(page_html, "html.parser")
    return page_soup

def load_white_list():
    white_list = []
    f = open("white_list.txt", "r", encoding="utf-8")
    for line in f:
        if line != '':
            if line.isupper(): 
                white_list.append(line.strip())
    f.close()
    return white_list