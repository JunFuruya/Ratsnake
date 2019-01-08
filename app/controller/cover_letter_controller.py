# -*- coding: UTF-8 -*-

from app.controller.base_controller import BaseController
#from app.validator.language_validator import LanguageValidator
#from app.service.language_service import LanguageService
#from app.entity.language_entity import LanguageEntity
# TODO インフラ層に移動
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm

from app.helper.helper import HashHelper

'''
Cover Letter Controller Module
'''
class CoverLetterController(BaseController):
    def __init__(self, request):
        super().__init__(request)
        self.set_page_info('送り状管理画面', '送り状データを登録・編集・削除・PDF出力します。', '')
        self.__user_id = self.get_login_user()
        self.__service = LanguageService()
        self.__validator = LanguageValidator()
        pass

    def get_pdf(self, cover_letter_id):

        pdfFile = canvas.Canvas('./python.pdf')
        pdfFile.saveState()

        pdfFile.setAuthor('python-izm.com')
        pdfFile.setTitle('PDF生成')
        pdfFile.setSubject('サンプル')
 
        # A4
        pdfFile.setPageSize((21.0*cm, 29.7*cm))
        # B5
        # pdfFile.setPageSize((18.2*cm, 25.7*cm))

        pdfFile.setFillColorRGB(0, 0, 100)
        pdfFile.rect(2*cm, 2*cm, 6*cm, 6*cm, stroke=1, fill=1)
        pdfFile.setFillColorRGB(0, 0, 0)

        pdfFile.setLineWidth(1)
        pdfFile.line(10*cm, 20*cm, 10*cm, 10*cm)

        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
        pdfFile.setFont('HeiseiKakuGo-W5', 12)
        pdfFile.drawString(5*cm, 25*cm, 'あいうえおー')

        pdfFile.restoreState()
        pdfFile.save()
        pass