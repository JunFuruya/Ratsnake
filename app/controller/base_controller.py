#-*- UTF-8 -*-

from bottle import jinja2_template, redirect

from app.helper.helper import HashHelper

'''
Base Controller Module
'''
class BaseController():
    __title = ''
    __description = ''
    __notification = ''

    def __init__(self, request, should_check=True):
        self.__request = request
        self.__session = request.environ.get('beaker.session')
        self.check_login_status(should_check)
        pass

    def view(self, tempalte_path, entity):
        entity.set_title(self.__title) 
        entity.set_description(self.__description) 
        entity.set_notification(self.__notification) 

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
    
    def get_session(self, key):
        if HashHelper.hexdigest(key) not in self.__session:
            return ''
        else:
            return self.__session.get(HashHelper.hexdigest(key), False)
    
    def set_session(self, key, value):
        self.__session[HashHelper.hexdigest(key)] = value
        self.__session.save()
        pass
    
    def check_login_status(self, should_check=True):
        if (should_check):
            # TODO 動的に取得する
            username = 'admin'
            session_value = self.get_session('login')
            hashed_value = HashHelper.hexdigest(username)
    
            if(session_value != hashed_value):
                return self.redirect('/admin/login')
            pass
        else:
            pass