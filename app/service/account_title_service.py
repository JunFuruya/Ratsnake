# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.account_title_repository import AccountTitleRepository

class AccountTitleService(BaseService):
    def __init__(self):
        self.__reposiroty = AccountTitleRepository()
        pass

    def getList(self, user_id, limit, offset):
        return self.__reposiroty.findList(user_id, limit, offset)

    def get(self, user_id, account_title_id):
        return self.__reposiroty.find(user_id, account_title_id)

    def create(self, user_id, account_title_name, account_title_classification_type):
        return self.__reposiroty.insert(user_id, account_title_name, account_title_classification_type)

    def update(self, account_title_id, user_id, account_title_name, account_title_classification_type):
        return self.__reposiroty.update(account_title_id, user_id, account_title_name, account_title_classification_type)

    def delete(self, account_title_id, user_id):
        return self.__reposiroty.delete(account_title_id, user_id)
