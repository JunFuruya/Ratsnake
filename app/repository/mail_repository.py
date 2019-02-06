# -*- coding: UTF-8 -*-

from app.infrastructure.gmail_api import GmailApi

class MailRepository():
    def __init__(self):
        self.__repository = GmailApi()
        pass
    
    def get_list(self, label):
        mail_list = self.__repository.get_mails_by_label(label)
        
        for mail in mail_list:
            print(mail)
        
        # TODO Entity実装して返す
        return None
    