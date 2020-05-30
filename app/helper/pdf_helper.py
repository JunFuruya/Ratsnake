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

        #pdfFile.setFillColorRGB(0, 0, 100)
        #pdfFile.rect(2*cm, 2*cm, 6*cm, 6*cm, stroke=1, fill=1)
        #pdfFile.setFillColorRGB(0, 0, 0)

        #pdfFile.setLineWidth(1)
        #pdfFile.line(10*cm, 20*cm, 10*cm, 10*cm)

        pdfFile = PdfHelper.set_title(pdfFile, 'お見積書')
        pdfFile = PdfHelper.set_number(pdfFile, 'SC-E-20200408-01')
        pdfFile = PdfHelper.set_date(pdfFile, '2020/04/01')

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

        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiKakuGo-W5'))

        return pdfFile

    # タイトル追加
    @classmethod
    def set_title(cls, pdf, title):
        pdf.setFont('HeiseiKakuGo-W5', 16)
        pdf.drawString(8*cm, 25*cm, title)
        return pdf

    # 番号
    @classmethod
    def set_number(cls, pdf, number):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        pdf.drawString(13*cm, 27*cm, '見積番号: ' + number)
        return pdf

    # 発行日
    @classmethod
    def set_date(cls, pdf, date):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        pdf.drawString(13*cm, 26*cm, '発行日: ' + date)
        return pdf

    # 取引先
    @classmethod
    def set_client_name(cls, pdf, clientName):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        pdf.drawString(13*cm, 26*cm, clientName + '御中')
        return pdf

    # 住所
    @classmethod
    def set_address(cls, pdf, addressLines):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        for line in addressLines:
            # TODO 位置の修正
            pdf.drawString(13*cm, 26*cm, line)
        return pdf

    # 固定文言
    @classmethod
    def set_estimate_fixed_text(cls, pdf):
        # TODO 位置の修正
        pdf.setFont('HeiseiKakuGo-W5', 8)
        pdf.drawString(13*cm, 26*cm, '下記の通り、お見積り申し上げます。')
        return pdf

    # 総額欄
    @classmethod
    def set_amount(cls, pdf, amount):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        # TODO 位置の修正
        pdf.drawString(13*cm, 26*cm, 'お見積金額')
        pdf.drawString(13*cm, 26*cm, '\\' + amount + '(税別)')
        return pdf

    # 内訳欄
    @classmethod
    def set_items(cls, pdf, items):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        # TODO 位置の修正
        pdf.drawString(13*cm, 26*cm, '内訳')
        pdf.drawString(13*cm, 26*cm, '適用')
        pdf.drawString(13*cm, 26*cm, '数量')
        pdf.drawString(13*cm, 26*cm, '単位')
        pdf.drawString(13*cm, 26*cm, '金額（円）')
        for item in items:
            pdf.drawString(13*cm, 26*cm, item)
        pdf.drawString(13*cm, 26*cm, '合計')
        # TODO 合計金額の計算
        pdf.drawString(13*cm, 26*cm, '')
        return pdf

    # 前提条件欄
    @classmethod
    def set_notes(cls, pdf, notes):
        pdf.setFont('HeiseiKakuGo-W5', 8)
        # TODO 位置の修正
        pdf.drawString(13*cm, 26*cm, '前提条件')
        for note in notes:
            pdf.drawString(13*cm, 26*cm, '・' + )
        pdf.drawString(13*cm, 26*cm, '以上')

        return pdf

