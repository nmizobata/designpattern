import phase3_menu as menu

class Waitress:
    def __init__(self, pancakeHouseMenu:menu.PancakeHouseMenu, dinerMenu:menu.DinerMenu, cafeMenu:menu.CafeMenu):
        self.pancakeHouseMenu = pancakeHouseMenu
        self.dinerMenu = dinerMenu
        self.cafeMenu = cafeMenu
        
    def printMenu(self):
        self.pancakeIterator = self.pancakeHouseMenu.createIterator()
        self.dinerIterator = self.dinerMenu.createIterator()
        self.cafeIterator = self.cafeMenu.createIterator()

        print("メニュー\n----\n朝食")
        self._printMenu(self.pancakeIterator)
        print("\n昼食")
        self._printMenu(self.dinerIterator)
        print("\n夕食")
        self._printMenu(self.cafeIterator)
        
    def _printMenu(self, iterator:menu.Iterator):
        for menuItem in iterator:
            print(menuItem.getName(),end=", ")
            print(str(menuItem.getPrice())+" -- ",end = "")
            print(menuItem.getDescription())
        
if __name__=='__main__':
    waitress = Waitress(menu.PancakeHouseMenu(), menu.DinerMenu(), menu.CafeMenu())
    waitress.printMenu()