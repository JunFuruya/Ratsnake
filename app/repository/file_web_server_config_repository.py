#-*- UTF-8 -*-

from app.entity.web_config_entity import WebServerConfigEntity
from app.infrastructure.config_ini_file import WebServerConfigIniFile

'''
FileWebServerConfigRepository Module
'''
class FileWebServerConfigRepository():
    __web_config = None

    def __init__(self):
        self.__web_config = WebServerConfigIniFile();
        pass
    
    def get_web_server_config(self):
        server_name, port, debug, reloader = self.__web_config.get_config();

        entity = WebServerConfigEntity()
        entity.set_web_host(server_name)
        entity.set_web_port(port)
        entity.set_debug(debug)
        entity.set_reloader(reloader)
        return entity
