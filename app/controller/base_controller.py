#-*- UTF-8 -*-

from bottle import jinja2_template

'''
Base Controller Module
'''
class BaseController():
    __service = None
    
    __title = ''
    __description = ''
    __notification = ''
    
    def __init__(self):
        pass

    def view(self, tempalte_path, entity):
        return jinja2_template(tempalte_path, entity)