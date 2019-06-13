# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.client_address_repository import ClientAddressRepository

class ClientAddressService(BaseService):
    def __init__(self):
        self.__reposiroty = ClientAddressRepository()
        pass

    def getList(self, user_id, client_id, client_address_id, limit, oiffset):
        return self.__reposiroty.findList(user_id, client_id, client_address_id, limit, oiffset)

    def get(self, user_id, client_id, client_address_id):
        return self.__reposiroty.find(user_id, client_id, client_address_id)

    def create(self, user_id, client_id, client_address_id, client_name):
        return self.__reposiroty.insert(user_id, client_id, client_address_id, client_name)

    def update(self, user_id, client_id, client_address_id, client_name):
        return self.__reposiroty.update(user_id, client_id, client_address_id, client_name)

    def delete(self, user_id, client_id, client_address_id):
        return self.__reposiroty.delete(user_id, client_id, client_address_id)
