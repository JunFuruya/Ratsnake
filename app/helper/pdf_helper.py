# -*- coding: UTF-8 -*-

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm

class PdfHelper:
    # 見積書作成
    @classmethod
    def create_estimate_pdf(cls, file_name, file_path, items, notes):
        pdfFile = PdfHelper.get_pdf(file_name, file_path)
        pdfFile.setFillColorRGB(0, 0, 100)
        pdfFile.rect(2*cm, 2*cm, 6*cm, 6*cm, stroke=1, fill=1)
        pdfFile.setFillColorRGB(0, 0, 0)

        pdfFile.setLineWidth(1)
        pdfFile.line(10*cm, 20*cm, 10*cm, 10*cm)

        pdfFile = PdfHelper.set_title(pdfFile, '見積書')
        #pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
        #pdfFile.setFont('HeiseiKakuGo-W5', 12)
        #pdfFile.drawString(5*cm, 25*cm, 'あいうえおー')

        pdfFile.restoreState()
        pdfFile.save()

    # 請求書作成
    @classmethod
    def create_invoice_pdf(cls, file_name, file_path, items, notes):
        pass

    @classmethod
    def get_pdf(cls, file_name, file_path):
        pdfFile = canvas.Canvas(file_path + file_name + '.pdf')
        pdfFile.saveState()

        pdfFile.setAuthor('Jun Furuya')
        pdfFile.setTitle('')
        pdfFile.setSubject('')

        # A4
        pdfFile.setPageSize((21.0*cm, 29.7*cm))
        # B5
        # pdfFile.setPageSize((18.2*cm, 25.7*cm))
        return pdfFile

    # タイトル追加
    @classmethod
    def set_title(cls, pdf, title):
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))
        pdf.setFont('HeiseiKakuGo-W5', 12)
        pdf.drawString(5*cm, 25*cm, title)
        return pdf
