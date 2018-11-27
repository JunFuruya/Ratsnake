# -*- coding: UTF-8 -*-

from app.service.base_service import BaseService
from app.repository.link_repository import LinkRepository
from app.repository.link_category_repository import LinkCategoryRepository
from app.repository.user_repository import UsersRepository
from app.entity.link_entity import LinkEntity
from app.entity.link_category_entity import LinkCategoryEntity

class LinkService(BaseService):
    __repository = None
    __link_category_repository = None
    
    def __init__(self):
        self.__repository = LinkRepository()
        self.__link_category_repository = LinkCategoryRepository()
        pass

    def getList(self, user_id, limit, offset):
        return self.__repository.findList(user_id, limit, offset)
    
    def get(self, user_id, link_id):
        return self.__repository.find(user_id, link_id)

    def create(self, user_id, link_category_id, link_site_name, link_url, link_display_order):
        return self.__repository.insert(user_id, link_category_id, link_site_name, link_url, link_display_order)

    def update(self, user_id, link_id, link_category_id, link_site_name, link_url, link_display_order):
        return self.__repository.update(user_id, link_id, link_category_id, link_site_name, link_url, link_display_order)

    def delete(self, user_id, link_id):
        return self.__repository.delete(user_id, link_id)

    def get_link_categories(self, user_id, limit, offset):
        return self.__link_category_repository.findList(user_id, limit, offset)