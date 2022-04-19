#coding:utf-8

class tools:
    def __init__(self):
        pass
        
    def titleprint(cls, title):
        decorator = "".center(50, "=")
        title = title.center(50, "-")
        print("")
        print(decorator)
        print(title)
        print(decorator)
        print("")
        
    def separator(cls):
        print("")
        print("".center(50, "-"))
        print("")
        
    titleprint = classmethod(titleprint)
    separator = classmethod(separator)


if __name__ == "__main__":
    tools.titleprint("titre")
    tools.separator()
    