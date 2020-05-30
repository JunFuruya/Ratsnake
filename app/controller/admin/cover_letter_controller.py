# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
from app.helper.pdf_helper import PdfHelper
#from app.validator.language_validator import LanguageValidator
#from app.service.language_service import LanguageService
#from app.entity.language_entity import LanguageEntity

'''
Cover Letter Controller Module
'''
class CoverLetterController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('送り状管理画面', '送り状データを登録・編集・削除・PDF出力します。', '')
        self.__user_id = self.get_login_user()
        #self.__service = CoverLetterService()
        #self.__validator = CoverLetterValidator()
        pass

    # PDFファイル作成
    def get_pdf(self, cover_letter_id):
        items = {
          #{"item": "●●機能追加", "num": 1, "amount": 100000}
        }
        notes = {}
        PdfHelper.create_estimate_pdf('estimate', '/var/www/html/hideout/public/pdf/', items, notes)
        pass
