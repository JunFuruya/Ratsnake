#-*- UTF-8 -*-

import sys
from tkinter import Tk, Button, ttk

class BaseView:
    # window is None
    
    def __init__(self):
        window = Tk()

        # TODO rearrange the layout.
        button_frame = ttk.Frame(window)
        button = Button(button_frame, text = 'search')

        button_frame.grid()
        button.grid()

        # TODO move the figures to config file.
        window.geometry("400x300")

        window.mainloop()

