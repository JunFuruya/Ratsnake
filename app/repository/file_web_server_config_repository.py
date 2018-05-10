#-*- UTF-8 -*-

import app.entity.config_entity
import app.infrastructure.config_ini_file

'''
FileWebServerConfigRepository Module
'''
class FileWebServerConfigRepository():
    __file = None

    def __init__(self):
        self.__file = app.infrastructure.config_ini_file.WebServerConfigIniFile();
        print(self.__file)
        pass
    
    def get_web_server_config(self):
        entity = app.entity.config_entity.WebServerConfigEntity()
        entity.set_web_host('localhost')
        entity.set_web_port(8080)
        entity.set_debug(True)
        entity.set_reloader(True)
        #entity.set_web_host(self.__file['HOST']['ServerName'])
        #entity.set_web_port(self.__file['HOST']['Port'])
        #entity.set_debug(self.__file['HOST']['Debug'])
        #entity.set_reloader(self.__file['HOST']['Reloader'])
        return entity
