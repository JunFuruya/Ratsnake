#-*- UTF-8 -*-

from app.entity.web_config_entity import WebServerConfigEntity
from app.infrastructure.web_server_yaml_file import WebServerConfigYamlFile

'''
WebServerConfigRepository Module
'''
class WebServerConfigRepository():
    __web_config = None

    def __init__(self):
        self.__web_config = WebServerConfigYamlFile();
        pass
    
    def get_web_server_config(self):
        server_name, port, debug, reloader, secret_key = self.__web_config.get_config();

        entity = WebServerConfigEntity()
        entity.set_web_host(server_name)
        entity.set_web_port(port)
        entity.set_debug(debug)
        entity.set_reloader(reloader)
        entity.set_secret_key(secret_key)
        return entity
