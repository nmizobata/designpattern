import phase2_menu as menu

class Waitress:
    def __init__(self, pancakeHouseMenu:menu.PancakeHouseMenu, dinerManu:menu.DinerMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerManu
        
    def printMenu(self):
        self.pancakeIterator = self.pancakeHouseMenu.createIterator()
        self.dinerIterator = self.dinerMenu.createIterator()
        
        print("メニュー\n----\n朝食")
        self._printMenu(self.pancakeIterator)
        print("\n昼食")
        self._printMenu(self.dinerIterator)
        
    def _printMenu(self, iterator:menu.Iterator):
        while(iterator.hasNext()):
            menuItem = iterator.next()
            print(menuItem.getName(),end=", ")
            print(str(menuItem.getPrice())+" -- ",end = "")
            print(menuItem.getDescription())
        
