import phase3_menu as menu

class Waitress:
    def __init__(self, pancakeHouseMenu:menu.PancakeHouseMenu, dinerMenu:menu.DinerMenu, cafeMenu:menu.CafeMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        self.cafeMenu = cafeMenu
        
    def printMenu(self):
        self.pancakeIterator = self.pancakeHouseMenu.createIterator()
        self.dinerIterator = self.dinerMenu.createIterator()
        self.cafe
        
        print("メニュー\n----\n朝食")
        self._printMenu(self.pancakeIterator)
        print("\n昼食")
        self._printMenu(self.dinerIterator)
        print("\n夕食")
        self._printMenu(self.cafeIterator)
        
    def _printMenu(self, iterator:menu.Iterator):
        while(iterator.hasNext()):
            menuItem = iterator.next()
            print(menuItem.getName(),end=", ")
            print(str(menuItem.getPrice())+" -- ",end = "")
            print(menuItem.getDescription())
        
