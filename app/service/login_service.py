# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.user_repository import UsersRepository

class LoginService(BaseService):
    def __init__(self):
        self.__reposiroty = UsersRepository()
        pass

    def is_authenticated(self, username, password):
        return self.__reposiroty.exists(username, password)