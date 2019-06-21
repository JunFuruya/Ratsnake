# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.entity.base_web_entity import BaseWebEntity
from app.entity.error_entity import ErrorEntity

'''
Error Controller Module
'''
class ErrorController(BaseController):
    def __init__(self, request):
        super().__init__(request, False)
        self.set_page_info('Error', 'エラーが発生しました。', '')
        pass

    def index(self, request):
        return self.view('./template/index.html', BaseEntity())

    def error(self, status):
        error_entity = ErrorEntity()
        error_entity.set_http_status(status)
        error_entity.set_user_error_message('')
    
        return self.view('./template/front/error.html', entity=error_entity)

