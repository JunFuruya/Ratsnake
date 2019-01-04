# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.user_repository import UsersRepository

class LoginService(BaseService):
    def __init__(self):
        self.__reposiroty = UsersRepository()
        pass

    def findByLoginInfo(self, username, password):
        return self.__reposiroty.findByLoginInfo(username, password)