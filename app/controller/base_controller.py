# -*- coding: UTF-8 -*-

from bottle import jinja2_template, redirect, response

import g

from app.helper.hash_helper import HashHelper

'''
Base Controller Module
'''
class BaseController():
    __title = ''
    __description = ''
    __notification = ''
    __login_user_id = ''
    LOGIN_SESSION_USER_ID = 'login_user_id'
    SECRET = 'hideout_secret'

    def __init__(self, request, should_check=True):
        self.__request = request
        self.__session = request.environ.get('beaker.session')

        self.__login_user_id = self.get_session(self.LOGIN_SESSION_USER_ID)
        self.check_login_status(should_check)
        pass
    
    def set_page_info(self, title, description, notification):
        self.__title = title
        self.__description = description
        self.__notification = notification

    def view(self, tempalte_path, entity):
        entity.set_title(self.__title) 
        entity.set_description(self.__description)
        entity.set_notification(self.__notification)
        entity.set_login_status(self.__login_user_id)

        return jinja2_template(tempalte_path, entity=entity)
    
    def redirect(self, path):
        return redirect(path)
    
    def get_param(self, key, default=''):
        if key not in self.__request.forms:
            if key not in self.__request.query:
                return default
            elif self.__request.query.getunicode(key).strip() == '':
                return default
            else:
                return self.__request.query.getunicode(key).strip() 
        elif self.__request.forms.getunicode(key).strip() == '':
            return default
        else:
            return self.__request.forms.getunicode(key).strip()
    
    def set_session(self, key, value):
        self.__session[HashHelper.hexdigest(key)] = value
        self.__session.save()
        pass

    def get_session(self, key):
        if HashHelper.hexdigest(key) not in self.__session:
            return ''
        else:
            return self.__session.get(HashHelper.hexdigest(key), False)
    
    def set_cookie(self, key, value, max_age, secret):
        response.set_cookie(key, value, max_age=max_age, secret=secret)
        pass

    def get_cookie(self, key, secret):
            return self.__request.get_cookie(key, secret=secret)
    
    def check_login_status(self, should_check=True):
        if (should_check):
            if(self.__login_user_id == ''):
                if(self.get_cookie(HashHelper.hexdigest(self.LOGIN_SESSION_USER_ID), secret=self.SECRET)):
                    self.__login_user_id = self.get_cookie(HashHelper.hexdigest(self.LOGIN_SESSION_USER_ID), secret=self.SECRET);
                else:
                    return self.redirect('/admin/login')
        pass
    
    def get_login_user(self):
        return self.__login_user_id

    def get_offset(self, record_num_per_page, page_num):
        if(int(page_num) == 1):
            return 0
        else:
            return (int(page_num) - 1) * int(record_num_per_page)
 