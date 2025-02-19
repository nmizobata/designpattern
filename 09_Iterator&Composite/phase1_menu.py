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
    
class PancakeHouseMenu:
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
    
    def getMenuItems(self):
        return self.menuItems
    
class DinerMenu:
    MAX_ITEMS = 6
    def __init__(self):
        self.menuItems = [MenuItem("","",False,0.0)]*(DinerMenu.MAX_ITEMS+1)
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
        self.addItem("Hoddog",
                     "ザワークラウト、レリッシュ、玉ねぎ、チーズを挟んだホットドッグ",
                     False,
                     3.05)
        
    def addItem(self,name:str,description:str, vegetarian:bool, price:float):
        self.menuItem = MenuItem(name, description, vegetarian, price)
        if self.numberOfItems > DinerMenu.MAX_ITEMS:
            print("すみません、メニューはいっぱいです！ メニューに項目を追加できません")
        else:
            self.menuItems[self.numberOfItems] = self.menuItem
            self.numberOfItems += 1
            
    def getMenuItems(self):
        return self.menuItems[:self.numberOfItems]

if __name__=="__main__":
    # Pythonでは、配列もArrayもリストの概念でカバーできるため、同じ表現で値を取り出すことができる。
    pancake = PancakeHouseMenu()
    for menu in pancake.getMenuItems():
        print("name:{} description:{} vegetarian:{} price:{}".format(menu.name, menu.description, menu.vegetarian, menu.price))
    
    dinner = DinerMenu()
    print("registard menu {} / max limit {}: ".format(dinner.numberOfItems, dinner.MAX_ITEMS+1))
    for menu in dinner.getMenuItems():
        print("name:{} description:{} vegetarian:{} price:{}".format(menu.name,menu.description,menu.vegetarian,menu.price))
    