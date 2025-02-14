'''
コーヒーのサイズにより料金が変わる仕様を導入
Tall(S)、Grande(M)、Venti(L)。Enumクラスを利用
BeverageクラスにsetSize, getSizeを追加。
コーヒーの価格はもとより、オプションの価格もサイズによって変わる。
また、descriptionにサイズ情報を出す。

気づき
Enumクラスは便利。Enumの定義名を取得したい場合は、.nameで参照する。
サイズ情報のように包む前後で統一されるプロパティは、インスタンスプロパティではなく、クラスプロパティを利用する。インスタンスプロパティを使うと、インスタンス作成ごとに変わってしまうので注意。
'''

from abc import ABC, abstractmethod
from enum import Enum, auto

class Size(Enum):
    TALL = auto()
    GRANDE = auto()
    VENTI = auto()

class Beverage(ABC):
    size = Size.TALL  # クラスプロパティとしてサイズ情報を定義
    
    @abstractmethod
    def cost(self):
        pass
    
    def setSize(self, size:Size):
        Beverage.size = size   # クラスプロパティを参照する場合は、クラス名.プロパティを使う
        
    def getSize(self):
        return Beverage.size
    
class HouseBlend(Beverage):
    def __init__(self):
        self.description = "ハウスブレンドコーヒー"
        
    def cost(self):
        CostTable = {Size.TALL:0.89, Size.GRANDE:0.99, Size.VENTI:1.09}
        return CostTable[self.getSize()]

    
class DarkRoast(Beverage):
    def __init__(self):
        self.description = "ダークローストコーヒー"
    
    def cost(self):
        CostTable = {Size.TALL:0.99, Size.GRANDE:1.09, Size.VENTI:1.19}
        return CostTable[self.getSize()]
    
class Espresso(Beverage):
    def __init__(self):
        self.description = "エスプレッソコーヒー"
        
    def cost(self):
        CostTable = {Size.TALL:1.99, Size.GRANDE:2.09, Size.VENTI:2.19}
        return CostTable[self.getSize()]
    
class Decaf(Beverage):
    def __init__(self):
        self.description = "デカフェコーヒー"
    
    def cost(self):
        CostTable = {Size.TALL:1.05, Size.GRANDE:1.15, Size.VENTI:1.25}
        return CostTable[self.getSize()]
    
class CondimentDecorator(Beverage):
    def __init__(self, wrapped_class:Beverage):
        self.wrapped_class = wrapped_class
        self.description = self.getDescription()
    
    @abstractmethod
    def getDescription(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass
    
class Milk(CondimentDecorator):
    
    def getDescription(self):
        return self.wrapped_class.description + " ミルク入り"
        
    def cost(self):
        CostTable = {Size.TALL:0.10, Size.GRANDE:0.20, Size.VENTI:0.30}
        return CostTable[self.getSize()] + self.wrapped_class.cost()
    
class Mocha(CondimentDecorator):
    
    def getDescription(self):
        return self.wrapped_class.description + " モカ入り"
    
    def cost(self):
        CostTable = {Size.TALL:0.20, Size.GRANDE:0.30, Size.VENTI:0.40}
        return CostTable[self.getSize()] + self.wrapped_class.cost()
    
class Soy(CondimentDecorator):
    
    def getDescription(self):
        return self.wrapped_class.description + " 豆乳入り"
    
    def cost(self):
        CostTable = {Size.TALL:0.15, Size.GRANDE:0.25, Size.VENTI:0.35}
        return CostTable[self.getSize()] + self.wrapped_class.cost()
    
class Whip(CondimentDecorator):
        
    def getDescription(self):
        return self.wrapped_class.description + " ホイップ入り"
    
    def cost(self):
        CostTable = {Size.TALL:0.10, Size.GRANDE:0.20, Size.VENTI:0.30}
        return CostTable[self.getSize()] + self.wrapped_class.cost()
    
if __name__== "__main__":
    order = HouseBlend()
    order = Soy(order)
    order.setSize(Size.VENTI)  # クラスプロパティを利用しているので、いつサイズ指定コマンドをおいても、すべてのクラスに適用される。
    order = Mocha(order)
    order = Mocha(order)
    print("オーダーは{}, Sizeは{}です".format(order.description,order.getSize().name))
    print("料金は{}ドルです".format(order.cost()))