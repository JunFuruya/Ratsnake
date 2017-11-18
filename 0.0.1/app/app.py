#-*- UTF-8 -*-

import config
import controller
import values
import view

class App:
    controllers = []
    
    def __init__(self):
      self.controllers.insert(values.screenIdValue.DEFAULT(), controller.IndexController())
      self.controllers.insert(values.screenIdValue.GOOGLE_SEARCH(), controller.GoogleSearchController())

    @staticmethod
    def execute():
        print('execute')
        
        objView = view.BaseView()
     
    def changeScreen(self, screenId):
        controller = self.controllers[screenId]
        view = self.views[screenId]
        view.setViewParams(controller.getViewParams())
    
