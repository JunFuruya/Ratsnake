# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
#from app.validator.language_validator import LanguageValidator
#from app.service.language_service import LanguageService
#from app.entity.language_entity import LanguageEntity
from app.entity.base_web_entity import BaseWebEntity

'''
SC Mail Controller Module
'''
class ScMailController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('SCメール送信画面', 'SC社に対してメールを送信します。', '')
        self.__user_id = self.get_login_user()
        #self.__service = LanguageService()
        #self.__validator = LanguageValidator()
        pass

    def index(self):
        return self.view('./template/admin/sc_mail/list.html', BaseWebEntity())
