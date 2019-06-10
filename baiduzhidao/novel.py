# coding=UTF-8

import requests
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'https://www.kanunu8.com/book3/8373/index.html'
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    return requests.get(url, headers=headers).content
def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    novle_author_soup = soup.find('td', attrs={'valign': 'middle'}).getText()
    
    return novle_author_soup
if __name__ == '__main__':
    url = DOWNLOAD_URL
    html = download_page(url)
    a = parse_html(html)
    print(a)