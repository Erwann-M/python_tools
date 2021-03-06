#coding:utf-8
import shutil

class Decoration:
    
    default_width = shutil.get_terminal_size().columns / 1.5
    
    def __init__(self):
        pass
        
    def big_title_print(cls, title):
        border = "+" + "".center(int(Decoration.default_width), "=") + "+"
        contain = "|" + "".center(int(Decoration.default_width), " ") + "|"
        title = " " + title.upper() + " "
        title = "|" + title.center(int(Decoration.default_width), " ") + "|"
        print("")
        print(border)
        print(contain)
        print(title)
        print(contain)
        print(border)
        print("")
        
    def title_print(cls, title):
        border = "+" + "".center(int(Decoration.default_width), "=") + "+"
        title = " " + title.upper() + " "
        title = "|" + title.center(int(Decoration.default_width), " ") + "|"
        print("")
        print(border)
        print(title)
        print(border)
        print("")
        
    def subtitle_print(cls, title):
        title = " " + title + " "
        title = title.center(int(Decoration.default_width), "=")
        print("")
        print(title)
        print("")
        
    def separator(cls):
        print("")
        print("".center(int(Decoration.default_width), "-"))
        print("")
        
    def change_width(cls, width):
        Decoration.default_width = width
        
    big_title_print = classmethod(big_title_print)
    title_print = classmethod(title_print)
    separator = classmethod(separator)
    subtitle_print = classmethod(subtitle_print)
    change_width = classmethod(change_width)


if __name__ == "__main__":
    Decoration.big_title_print("Mon jolie gros titre pour le test")
    Decoration.title_print("Mon petit titre pour le test")
    Decoration.separator()
    Decoration.subtitle_print("Mon petit sous titre pour test")
    