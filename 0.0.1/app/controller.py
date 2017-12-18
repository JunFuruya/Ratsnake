#-*- UTF-8 -*-

import view

class BaseController():
    title = 'base'
    view_params = []

    def __init__(self):
        return None
    
    def getTitle(self):
        return self.title
    
    def getView(self):
        # TODO 各ControllerごとのViewを返す
        return view.BaseView()
    
    def getViewParams(self):
        return view_params
    
class IndexController(BaseController):
    def __init__(self):
        return None

    def getView(self):
        # TODO 各ControllerごとのViewを返す
        return view.BaseView()

class GoogleSearchController(BaseController):
    def __init__(self):
        return None
    
    def getView(self):
        # TODO 各ControllerごとのViewを返す
        return view.BaseView()
