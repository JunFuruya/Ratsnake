#-*- UTF-8 -*-

'''
Service Module
'''

from bs4 import BeautifulSoup
import urllib3

# TODO モジュール組み込み後に消す
if __name__ == "__main__":
    service = Service()
    service.getSearchList()

class BaseService:
    '''
    BaseService Class
    '''

    google_search_url = 'https://www.google.co.jp/search'
    query = '%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%AA%E3%83%B3%E3%82%B0'
    
    def __init__(self):
        '''
        constructor
        '''
        pass
    
    def getSearchList(self):
        '''
        get a search list
        '''
        html = urllib3.urlopen(google_search_url + '?q=' + query)
        soup = BeautifulSoup(html)
        url_list = soup.find("a")
        
        for url in url_list:
            prit(url)


class IdcfCloudStartService:
    '''
    control IDCF cloud
    '''

    idcf_cloud_repository = null
    
    '''
    constructor
    '''
    def __init__(self):
        self.idcf_cloud_repository = IdcfCloudRepository()
        pass
    
    def start():
        '''
        start server
        '''
        self.idcf_cloud_repository.start()
        pass

    def stop():
        '''
        stop server
        '''
        self.idcf_cloud_repository.stop()
        pass