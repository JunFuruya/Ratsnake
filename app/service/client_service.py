# -*- coding: UTF-8 -*-

import g

from app.service.base_service import BaseService
from app.repository.client_repository import ClientRepository

class ClientService(BaseService):
    def __init__(self):
        self.__reposiroty = ClientRepository()
        pass

    def getList(self, user_id, limit, oiffset):
        g.log.info('getList')
        return self.__reposiroty.findList(user_id, limit, oiffset)
'''
    def get(self, user_id, client_id):
        return self.__reposiroty.find(user_id, client_id)

    def create(self, user_id, client_name):
        return self.__reposiroty.insert(user_id, client_name)

    def update(self, client_id, user_id, client_name):
        return self.__reposiroty.update(client_id, user_id, client_name)

    def delete(self, client_id, user_id):
        return self.__reposiroty.delete(client_id, user_id)
'''