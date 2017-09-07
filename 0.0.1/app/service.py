#-*- UTF-8 -*-

from bs4 import BeautifulSoup
import urllib3

# TODO モジュール組み込み後に消す
if __name__ == "__main__":
    service = Service()
    service.getSearchList()

class BaseService:
    google_search_url = 'https://www.google.co.jp/search'
    query = '%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0'
    
    def __init__(self):
        pass
    
    def getSearchList(self):
        html = urllib3.urlopen(google_search_url + '?q=' + query)
        soup = BeautifulSoup(html)
        url_list = soup.find("a")
        
        for url in url_list:
            prit(url)
