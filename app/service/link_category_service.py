# -*- coding: utf-8 -*-

from app.service.base_service import BaseService
from app.repository.link_category_repository import LinkCategoryRepository
from app.repository.user_repository import UsersRepository

class LinkCategoryService(BaseService):
    def __init__(self):
        self.__reposiroty = LinkCategoryRepository()
        pass

    def getList(self, user_id, limit, offset):
        return self.__reposiroty.findList(user_id, limit, offset)

    def get(self, user_id, link_category_id):
        return self.__reposiroty.find(user_id, link_category_id)

    def create(self, user_id, link_category_name, link_category_display_order):
        return self.__reposiroty.insert(user_id, link_category_name, link_category_display_order)

    def update(self, link_category_id, user_id, link_category_name, link_category_display_order):
        return self.__reposiroty.update(link_category_id, user_id, link_category_name, link_category_display_order)

    def delete(self, link_category_id, user_id):
        return self.__reposiroty.delete(link_category_id, user_id)
