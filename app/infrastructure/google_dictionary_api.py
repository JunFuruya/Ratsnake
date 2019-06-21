# -*- coding: UTF-8 -*-

import certifi, io, pycurl

import g

from app.infrastructure.base_api import BaseApi

'''
Google Dictionary Api module
'''
class GoogleDictionaryApi(BaseApi):
    END_POINT = 'https://www.google.com/#q=define+'
    
    def __init__(self):
        super().__init__()
        pass

    def get(self, foreign_word, timeout=10):
        curl = pycurl.Curl()
        buffer = io.BytesIO()
        
        # TODO Baseクラスへ追い出す
        curl.setopt(pycurl.HTTPHEADER, ['Content-Length: 1000'])
        curl.setopt(pycurl.URL, self.END_POINT + foreign_word)
        curl.setopt(pycurl.CAINFO, certifi.where())
        curl.setopt(pycurl.CUSTOMREQUEST, 'POST')
        curl.setopt(pycurl.TIMEOUT, timeout)
        curl.setopt(pycurl.WRITEDATA, buffer)
        
        response_code = 0
        
        try:
            curl.perform()
            body = buffer.getvalue()
            g.log.info('########################')
            response_code = curl.getinfo(pycurl.RESPONSE_CODE)
            g.log.info(response_code)
            g.log.info(body.decode('utf-8'))

        except Exception as e:
            g.log.error(e)

        finally:
            curl.close()
            
        if response_code == 200:
            g.log.info(body.decode('utf-8'))
            return

        else:
            g.log.error(response_code)
            return []
