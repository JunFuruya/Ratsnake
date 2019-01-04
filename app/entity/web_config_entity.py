# -*- coding: UTF-8 -*-

class WebServerConfigEntity():
    __web_host = ''
    __web_port = ''
    __debug = ''
    __reloader = ''
    __secret_key = ''
    
    def set_web_host(self, web_host):
        self.__web_host = web_host
        return self
    
    def get_web_host(self):
        return self.__web_host

    def set_web_port(self, web_port):
        self.__web_port = web_port
        return self

    def get_web_port(self):
        return self.__web_port

    def set_debug(self, debug):
        self.__debug = debug
        return self

    def get_debug(self):
        return self.__debug

    def set_reloader(self, reloader):
        self.__reloader = reloader
        return self
    
    def get_reloader(self):
        return self.__reloader

    def set_secret_key(self, secret_key):
        self.__secret_key = secret_key
        return self

    def get_secret_key(self):
        return self.__secret_key
    
    def to_array(self):
        pass #TODO: implement