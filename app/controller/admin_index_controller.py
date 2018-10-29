#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.index_entity import IndexEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class AdminIndexController(BaseController):
    def __init__(self):
        self.__title = ''
        self.__description = ''
        pass

    def index(self, request):
        # TODO: username取得
        entity = IndexEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/admin/index.html', entity=entity)

