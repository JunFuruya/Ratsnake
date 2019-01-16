# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
#from app.validator.language_validator import LanguageValidator
#from app.service.language_service import LanguageService
#from app.entity.language_entity import LanguageEntity
from app.entity.base_web_entity import BaseWebEntity

from app.helper.helper import HashHelper

'''
Balance Sheet Controller Module
'''
class BalanceSheetController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('貸借対照表', '貸借対照表を作成・閲覧します。', '')
        self.__user_id = self.get_login_user()
        #self.__service = LanguageService()
        #self.__validator = LanguageValidator()
        pass

    def index(self):
        return self.view('./template/admin/balance-sheets/list.html', BaseWebEntity())
