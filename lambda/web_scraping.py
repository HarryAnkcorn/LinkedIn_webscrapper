from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import urllib

def web_scrape(url):
    uclient = urlopen(url)
    uclient.addheaders = ('User-Agent', "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36")
    page_html = uclient.read()
    uclient.close()
    page_soup = soupifie(page_html)
    return page_soup

def soupifie(page_html):
    page_soup = soup(page_html, "html.parser")
    return page_soup

