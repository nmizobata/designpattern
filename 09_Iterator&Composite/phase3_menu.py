from abc import ABC, abstractmethod

class DinerMenuIterator:
    def __init__(self, items):
        self.position = 0
        self.items = items
    
    def __itr__(self):
        return self
    
    def __next__(self):
        if self.hasNext():
            menuItem = self.items[self.position]
            self.position += 1
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if (self.position >= len(self.items) or self.items[self.position] is None):
            return False
        else:
            return True
        

class PancakeMenuIterator:
    def __init__(self, menulist):
        self.num = 0
        self.menulist = menulist
    
    def __itr__(self):
        return self
    
    def __next__(self):
        if self.hasNext(self):
            menuItem = self.menulist[self.num]
            self.num += 1
            return menuItem
        else:
            raise StopIteration
    
    def hasNext(self) -> bool:
        if (self.num >= len(self.menulist)):
            return False
        else:
            return True

class CafeMenuIterator:
    def __init__(self, menulist):
        self.menulist = menulist
        self.num = 0
    
    def __itr__(self):
        return self
    
    def __next__(self):
        item = self.menulist[self.num]
        self.num += 1
        return item
        

class MenuItem:
    def __init__(self, name:str, description:str, vegetarian: bool, price:float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
        
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def isVegetarian(self):
        return self.vegetarian

class Menu(ABC):
    @abstractmethod
    def createIterator(self):
        pass
 
class PancakeHouseMenu(Menu):
    def __init__(self):
        self.menuItems = []
        self.addItem("K&Bのパンケーキ朝食",
                     "スクランブルエッグとトースト付きパンケーキ",
                     True,
                     2.99)
        self.addItem("いつものパンケーキ朝食",
                     "卵焼きとソーセージ付きパンケーキ",
                     False,
                     2.99)
        self.addItem("ブルーベリーパンケーキ",
                     "新鮮なブルーベリーを使ったパンケーキ",
                     True,
                     3.49)
        self.addItem("ワッフル",
                     "ブルーベリーかイチゴの好きな方をのせたワッフル",
                     True,
                     3.59)
    
    def addItem(self, name:str, description:str, vegetarian: bool, price: float):
        menuItem = MenuItem(name, description, vegetarian, price)
        self.menuItems.append(menuItem)
    
    # def getMenuItems(self):
    #     return self.menuItems
    
    def createIterator(self):
        return PancakeMenuIterator(self.menuItems)
        

    
class DinerMenu(Menu):
    MAX_ITEMS = 6
    def __init__(self):
        self.menuItems = [None]*(DinerMenu.MAX_ITEMS+1)
        self.numberOfItems = 0
        self.addItem("ベジタリアンBLT",
                     "レタス、トマト、フェイクベーコンを挟んだ全粒小麦パンサンドイッチ",
                     True,
                     2.99)
        self.addItem("BLT",
                     "レタス、トマト、ベーコンを挟んだ全粒小麦パンサンドイッチ",
                     False,
                     2.99)
        self.addItem("本日のスープ",
                     "ポテトサラダを添えた本日のスープ",
                     False,
                     3.29)
        self.addItem("ホットドッグ",
                     "ザワークラウト、レリッシュ、玉ねぎ、チーズを挟んだホットドッグ",
                     False,
                     3.05)
        self.addItem("蒸し野菜と玄米",
                     "玄米の上に蒸し野菜",
                     True,
                     3.99)
        self.addItem("パスタ",
                     "マリナラソーススパゲティとサワードウパン",
                     True,
                     3.89)
        
    def addItem(self,name:str,description:str, vegetarian:bool, price:float):
        self.menuItem = MenuItem(name, description, vegetarian, price)
        if self.numberOfItems > DinerMenu.MAX_ITEMS:
            print("すみません、メニューはいっぱいです！ メニューに項目を追加できません")
        else:
            self.menuItems[self.numberOfItems] = self.menuItem
            self.numberOfItems += 1
            
    # def getMenuItems(self):
    #     return self.menuItems[:self.numberOfItems]
    
    def createIterator(self):
        return DinerMenuIterator(self.menuItems)

class CafeMenu(Menu):
    def __init__(self):
        self.menuItems = {}
        self.addItem("野菜バーガーとフライドポテト",
                "全粒小麦にレタスとトマトを挟んだ野菜バーガーとフライドポテト",
                True,
                3.99)
        self.addItem("本日のスープ",
                "サラダが付いた本日のスープ",
                False,
                3.69)
        self.addItem("ブリトー",
                "インゲン豆、サルサ、グアカモーレ入りの大きなブリトー",
                True,
                4.29)
        
    def addItem(self, name:str, description:str, vegetarian:bool, price: float):
        self.menuItems[name] = [name, description, vegetarian, price]
        
    # def getMenuItems(self):
    #     return self.menuItems
    def __str__(self):
        
        return self.menuItems
    
    def createIterator(self):
        return CafeMenuIterator(list(self.menuItems.values()))

if __name__=="__main__":
    # dinerMenuIterator = DinerMenu().createIterator()
    # for menu in dinerMenuIterator:
    #     print("name:{} description:{} vegetarian:{} price:{}".format(menu.name,menu.description,menu.vegetarian,menu.price))
        
    # pancakeMenuIterator = PancakeHouseMenu().createIterator()
    # for menu in pancakeMenuIterator:
    #     print("name:{} description:{} vegetarian:{} price:{}".format(menu.name,menu.description,menu.vegetarian,menu.price))


    # cafeMenuIterator = CafeMenu().createIterator()
    # for menu in cafeMenuIterator:
    #     print("name:{} description:{} vegetarian:{} price:{}".format(menu.name,menu.description,menu.vegetarian,menu.price))
    print(list(CafeMenu().menuItems.values()))
    cafeMenuIterator = CafeMenuIterator(list(CafeMenu().menuItems.values()))
    next(cafeMenuIterator)
    print(cafeMenuIterator)
    # for menu in cafeMenuIterator:
        # print("name:{} descri/ption:{} vegetarian:{} price:{}".format(menu.name,menu.description,menu.vegetarian,menu.price))