#coding:utf-8

class Tools:
    
    default_width = 50
    
    def __init__(self):
        pass
        
    def title_print(cls, title):
        decorator = "".center(int(Tools.default_width), "=")
        title = " " + title + " "
        title = title.center(int(Tools.default_width), "-")
        print("")
        print(decorator)
        print(title)
        print(decorator)
        print("")
        
    def subtitle_print(cls, title):
        title = " " + title + " "
        title = title.center(int(Tools.default_width), "=")
        print("")
        print(title)
        print("")
        
    def separator(cls):
        print("")
        print("".center(int(Tools.default_width), "-"))
        print("")
        
    def change_width(cls, width):
        Tools.default_width = width
        
    titleprint = classmethod(title_print)
    separator = classmethod(separator)
    subtitleprint = classmethod(subtitle_print)
    change_width = classmethod(change_width)


if __name__ == "__main__":
    Tools.change_width(60)
    Tools.titleprint("Mon jolie titre")
    Tools.separator()
    Tools.subtitleprint("Mon petit sous titre")
    