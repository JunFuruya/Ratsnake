# -*- coding: UTF-8 -*-

import certifi
import pycurl

class BaseApi():
    __curl = None
    def __init__(self):
        self.__curl = pycurl.Curl()
        
        pass
    
    def set_header(self, header):
        self.__curl.setopt(pycurl.HTTPHEADER, header)
        pass
    
    def get(self, url, timeout=10):
        self.__curl.setopt(pycurl.URL, url)
        self.__curl.setopt(pycurl.CAINFO, certifi.where())
        self.__curl.setopt(pycurl.CUSTOMREQUEST, 'GET')
        self.__curl.setopt(pycurl.TIMEOUT, timeout)
        self.__curl.perform()
        pass
    
    def post(self, url, timeout=10):
        self.__curl.setopt(pycurl.URL, url)
        self.__curl.setopt(pycurl.CAINFO, certifi.where())
        self.__curl.setopt(pycurl.CUSTOMREQUEST, 'POST')
        self.__curl.setopt(pycurl.TIMEOUT, timeout)
        self.__curl.perform()
        pass