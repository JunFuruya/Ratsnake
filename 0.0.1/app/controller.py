#-*- UTF-8 -*-

class BaseController():
    title = 'base'

    def __init__(self):
        return None
    
    def getTitle(self):
        return self.title
    
class IndexController(BaseController):
    def __init__(self):
        return None
    
class GoogleSearchController(BaseController):
    def __init__(self):
        return None