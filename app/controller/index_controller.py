#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.base_web_entity import BaseWebEntity

from app.helper.helper import HashHelper

'''
Word Controller Module
'''
class IndexController(BaseController):
    def __init__(self):
        self.__title = ''
        self.__description = ''
        pass

    def index(self, request):
        # TODO もっと良い方法を考える
        entity = BaseEntity()
        entity.set_title(self.__title)
        entity.set_description(self.__description)
        entity.set_notification('This is the index page.')
        return self.view('./template/index.html')
        #return self.view('./template/index.html', entity=entity)

