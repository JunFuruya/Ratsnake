#-*- UTF-8 -*-

from app.entity import config_entity
from app.infrastructure import config_ini_file

'''
FileWebServerConfigRepository Module
'''
class FileWebServerConfigRepository():
    __web_config = None

    def __init__(self):
        self.__web_config = config_ini_file.WebServerConfigIniFile();
        pass
    
    def get_web_server_config(self):
        server_name, port, debug, reloader = self.__web_config.get_config();

        entity = config_entity.WebServerConfigEntity()
        entity.set_web_host(server_name)
        entity.set_web_port(port)
        entity.set_debug(debug)
        entity.set_reloader(reloader)
        return entity
