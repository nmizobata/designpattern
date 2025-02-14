from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self):
        self.description = ""
        
    @abstractmethod
    def cost(self):
        pass
    
class HouseBlend(Beverage):
    def __init__(self):
        self.description = "ハウスブレンドコーヒー"
        
    def cost(self):
        return 0.89
    
class DarkRoast(Beverage):
    def __init__(self):
        self.description = "ダークローストコーヒー"
    
    def cost(self):
        return 0.99
    
class Espresso(Beverage):
    def __init__(self):
        self.description = "エスプレッソコーヒー"
        
    def cost(self):
        return 1.99
    
class Decaf(Beverage):
    def __init__(self):
        self.description = "デカフェコーヒー"
    
    def cost(self):
        return 1.05
    
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
        return 0.10 + self.wrapped_class.cost()
    
class Mocha(CondimentDecorator):
    
    def getDescription(self):
        return self.wrapped_class.description + " モカ入り"
    
    def cost(self):
        return 0.20 + self.wrapped_class.cost()
    
class Soy(CondimentDecorator):
    
    def getDescription(self):
        return self.wrapped_class.description + " 豆乳入り"
    
    def cost(self):
        return 0.15 + self.wrapped_class.cost()
    
class Whip(CondimentDecorator):
        
    def getDescription(self):
        return self.wrapped_class.description + " ホイップ入り"
    
    def cost(self):
        return 0.10 + self.wrapped_class.cost()
    
if __name__== "__main__":
    order = HouseBlend()
    order = Whip(order)
    order = Mocha(order)
    order = Mocha(order)
    order = Soy(order)
    print("オーダーは{}です".format(order.description))
    print("料金は{}ドルです".format(order.cost()))