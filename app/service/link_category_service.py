# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.link_category_repository import LinkCategoryRepository
from app.repository.db_user_repository import DbUsersRepository

class LinkCategoryService(BaseService):
    def __init__(self):
        self.__reposiroty = LinkCategoryRepository()
        pass

    def getList(self, limit, oiffset):
        return self.__reposiroty.findList(limit, oiffset)

    def get(self, user_id, link_category_id):
        return self.__reposiroty.find(user_id, link_category_id)

    def create(self, user_id, link_category_name):
        return self.__reposiroty.insert(user_id, link_category_name)

    def update(self, link_category_id, user_id, link_category_name):
        return self.__reposiroty.update(link_category_id, user_id, link_category_name)

    def delete(self, link_category_id, user_id):
        return self.__reposiroty.delete(link_category_id, user_id)
