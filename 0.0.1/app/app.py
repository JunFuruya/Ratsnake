#-*- UTF-8 -*-

import config
import controller
import values

class App:
    controller = None
    view = None
    controllers = []
    
    def __init__(self):
      self.controllers.insert(values.screenIdValue.DEFAULT(), controller.IndexController())
      self.controllers.insert(values.screenIdValue.GOOGLE_SEARCH(), controller.GoogleSearchController())

    def execute(self):
        print('execute')        
        self.changeScreen(values.screenIdValue.DEFAULT())
     
    def changeScreen(self, screenId):
        self.controller = self.controllers[screenId]
        self.view = self.controller.getView()
        self.view.setViewParams(controller.getViewParams())
    