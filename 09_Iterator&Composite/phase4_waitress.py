class Waitress:
    def __init__(self, allMenus):
        self.allMenus = allMenus
        
    def printMenu(self):
        self.allMenus.print()