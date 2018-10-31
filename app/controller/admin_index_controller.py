#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.index_entity import IndexEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class AdminIndexController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.__title = 'Hideout Login'
        self.__description = 'Login page.'
        self.__notification = 'Please enter your id and password.'
        pass

    def index(self):
        return self.view('./template/admin/index.html', entity=IndexEntity())