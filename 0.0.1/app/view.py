#-*- UTF-8 -*-

import sys
from tkinter import Tk, ttk

class BaseView:
    window = None
    panel_frame = None
    view_params = []
    
    title = "BaseView"
    
    def __init__(self):
        self.window = Tk()

        # TODO rearrange the layout.
        self.panel_frame = ttk.Label(self.window, text=self.title)
        self.panel_frame.grid(column = 1, columnspan = 1, padx = 0, pady = 0, ipadx = 0, ipady = 0, row = 1, rowspan = 1, sticky = "")

        button_frame = ttk.Frame(self.window)
        button_frame.grid(column = 1, columnspan = 1, padx = 0, pady = 0, ipadx = 0, ipady = 0, row = 2, rowspan = 1, sticky = "")

        button = ttk.Button(button_frame, text = 'search')
        # BUtton-1 は左クリック
        button.bind("<Button-1>", self.setScreenTitle)
        button.grid(column = 1, columnspan = 1, padx = 0, pady = 0, ipadx = 0, ipady = 0, row = 1, rowspan = 1, sticky = "")

        # TODO move the figures to config file.
        self.window.geometry("400x300")
        self.window.mainloop()

    def setScreenTitle(self, event):
        title = "result"
        self.title = title
        self.panel_frame.config(text = self.title)

    def setViewParams(self, params):
        self.view_params = params