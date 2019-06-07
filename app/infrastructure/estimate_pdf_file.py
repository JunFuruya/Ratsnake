# -*- coding: UTF-8 -*-

import g

from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

from app.infrastructure.base_file import BaseFile

'''
estimate file module
'''
class EstimatePdfFile(BaseFile):

    def __init__(self, file_path, file_name):
        # TODO ユーザ情報からとる
        author = 'Jun Furuya'
        title = '見積書'
        subject = ''
        
        super().__init__(file_path, file_name)
        super().setAuthor(self, author):
        super().setTitle(self, title):
        super().setSubject(self, subject):
        pass

    def create(self, estimate_entity):
        #TODO Entityから情報を取得し、見積書を作成する。

        super().save()
        pass
