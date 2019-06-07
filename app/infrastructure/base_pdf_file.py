# -*- coding: UTF-8 -*-

import g

from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

from app.infrastructure.base_file import BaseFile

'''
base pdf file module
'''
class BasePdfFile(BaseFile):

    def __init__(self, file_path, filename):
        super().__init__()
        self.__pdf = canvas.Canvas(file_path + file_name)
        self.__pdf.saveState()
        pass

    def setAuthor(self, author):
        self.__pdf.setAuthor(author)
        pass

    def setTitle(self, title):
        self.__pdf.setTitle(title)
        pass

    def setSubject(self, subject):
        self.__pdf.setSubject(subject)
        pass

    def setPageSize(self, page_size):
        if page_size == 'A4':
            self.__pdf.setPageSize((21.0*cm, 29.7*cm))
        elif page_size == 'B5'
            self.__pdf.setPageSize((18.2*cm, 25.7*cm))
        pass

    def setWhiteRectangle(self, x, y, width, height):
        self.__pdf.setFillColorRGB(0, 0, 0)
        self.__pdf.rect(x, y, width, height, stroke=1, fill=0)
        pass
    
    def drawBlackLine(self, start_x, start_y, stop_x, stop_y, width=1):
        self.__pdf.setLineWidth(width)
        self.__pdf.line(start_x, start_y, stop_x, stop_y)
        pass
    
    def writeText(self, x, y, text, font_type, font_size=10):
        pdfmetrics.registerFont(UnicodeCIDFont(font_type))
        pdfFile.setFont(font_type, font_size)
        pdfFile.drawString(x, y, text)
        pass
    
    def save(self):
        self.__pdf.restoreState()
        self.__pdf.save()
        pass