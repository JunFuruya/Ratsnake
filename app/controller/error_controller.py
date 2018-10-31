#-*- UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.base_web_entity import BaseWebEntity
from app.entity.error_entity import ErrorEntity

from app.helper.helper import HashHelper

'''
Error Controller Module
'''
class ErrorController(BaseController):
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

    def error(status):
        error_entity = ErrorEntity()
        error_entity.set_http_status(status)
        error_entity.set_user_error_message('')
        error_entity.set_title(status + ' Error')
        error_entity.set_description('We can\'t find the page. Please check the URL.')
    
        tempalte_path = './template/front/error.html'
        return jinja2_template(tempalte_path, entity=error_entity)

