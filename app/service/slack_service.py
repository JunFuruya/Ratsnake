# -*- coding: UTF-8 -*-

from app.repository.idcf_cloud_repository import IdcfCloudRepository
from app.repository.slack_repository import SlackRepository
from app.service.base_service import BaseService

'''
Service Module
'''
class SlackService(BaseService):
    __slack_repository = None
    __idcf_cloud_repository = None

    def __init__(self):
        self.__slack_reposiroty = SlackRepository()
        self.__idcf_cloud_repository = IdcfCloudRepository()
        
    def run(self):
        self.__slack_reposiroty.run()

    def start_idcf_cloud_server():
        self.__idcf_cloud_repository.start()

    def stop_idcf_cloud_server():
        self.__idcf_cloud_repository.stop()

#    api_idcf_cloud_repository.get_virtual_machine_list()
#    api_idcf_cloud_repository.stop()
    