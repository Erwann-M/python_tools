import tkinter as tk

class TkinterTools:
    def __init__(self):
        pass
    
    def center_window(cls, main_app, window_x, window_y):
        screen_x = int(main_app.winfo_screenwidth())
        screen_y = int(main_app.winfo_screenheight())
        
        window_x = int(window_x)
        window_y = int(window_y)

        posX = int((screen_x / 2) - (window_x / 2))
        posY = int((screen_y / 2) - (window_y / 2))

        geo = "{}x{}+{}+{}".format(window_x, window_y, posX, posY)
        
        return geo
    
    center_window = classmethod(center_window)
        