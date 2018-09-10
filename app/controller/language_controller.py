#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.service.web_service import LanguageService
from app.entity.base_web_entity import BaseWebEntity

'''
Language Controller Module
'''
class LanguageController(BaseController):

    def __init__(self):
        self.__service = LanguageService()
        self.__title = '言語マスタ'
        self.__description = '単語帳を作成する言語を登録・編集・削除します。'
        pass

    def index(self, request):
        # TODO もっと良い方法を考える
        limit = request.query.get('limit')
        limit = limit if limit is not None else 10
            
        # TODO もっと良い方法を考える
        offset = request.query.get('offset')
        offset = offset if offset is not None else 0
        
        # TODO もっと良い方法を考える
        entity = BaseWebEntity()
        entity.set_records(self.__service.getList(limit, offset))
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity
    
    def detail(self, request):
        entity = LanguagePageEntity()
        entity = self.__service.get()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        pass
    
    def create(self, request):
        entity = LanguagePageEntity()
        entity = self.__service.get()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return entity

    def confirm(self, request):
        entity = LanguagePageEntity()
        entity = self.__service.get()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        pass
    
    def update(self, request):
        entity = LanguagePageEntity()
        entity = self.__service.get()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        pass
    
    def delete(self, request):
        entity = LanguagePageEntity()
        entity = self.__service.get()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        pass

    def complete(self, request):
        entity = LanguagePageEntity()
        entity = self.__service.get()
        entity.set_notification('This is the index page.')
        pass
    