from abc import ABC, abstractmethod


class PizzaIngredientFactory(ABC):
    @abstractmethod
    def createDough(self):
        pass
    
    @abstractmethod
    def createSauce(self):
        pass
    
    @abstractmethod
    def createCheese(self):
        pass
    
    @abstractmethod
    def createVeggies(self):
        pass
    
    @abstractmethod
    def createPepperoni(self):
        pass
    
    @abstractmethod
    def createClam(self):
        pass
        
        
class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()
    
    def createSauce(self):
        return MarinaraSauce()
    
    def createCheese(self):
        return ReggianoCheese()
    
    def createVeggies(self):
        Veggies = [Garlic(), Onion(), Mushroom(), Redpepper()]
        return Veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FreshClams()
    
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough()
    
    def createSauce(self):
        return PlumTomatoSauce()
    
    def createCheese(self):
        return MozzarellaCheese()
    
    def createVeggies(self):
        Veggies = [Spinach(), Eggplant(), BlackOlives(), Redpepper()]
        return Veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FrozenClams()
    
class CaliforniaPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return VeryThinCrustDough()
    
    def createSauce(self):
        return BruschettaSauce()
    
    def createCheese(self):
        return GoatCheese()
    
    def createVeggies(self):
        Veggies = [Garlic(), Onion(), Mushroom(), Redpepper()]
        return Veggies
    
    def createPepperoni(self):
        return SlicedPepperoni()
    
    def createClam(self):
        return FreshClams()
    
class ThinCrustDough:
    def __init__(self):
        print("薄いクラスト生地をこねる")
    
class MarinaraSauce:
    def __init__(self):
        print("マリナラソースを追加")
        
class ReggianoCheese:
    def __init__(self):
        print("レッジャーノチーズを追加")

class SlicedPepperoni:
    def __init__(self):
        print("スライスペパロニを追加")
   
class Garlic:
    def __init__(self):
        print("ガーリックを追加")
    
class Onion:
    def __init__(self):
        print("玉ねぎを追加")
    
class Mushroom:
    def __init__(self):
        print("マッシュルームを追加")

class Redpepper:
    def __init__(self):
        print("レッドペッパーを追加")

class FreshClams:
    def __init__(self):
        print("新鮮なあさりを追加")

class PlumTomatoSauce:
    def __init__(self):
        print("トマトソースを追加")

class MozzarellaCheese:
    def __init__(self):
        print("モツァレラチーズを追加")

class Spinach:
    def __init__(self):
        print("ほうれん草を追加")

class Eggplant:
    def __init__(self):
        print("なすを追加")

class BlackOlives:
    def __init__(self):
        print("オリーブを追加")

class FrozenClams:
    def __init__(self):
        print("冷凍あさりを追加")

class VeryThinCrustDough:
    def __init__(self):
        print("極薄クラスト生地をこねる")

class BruschettaSauce:
    def __init__(self):
        print("ブルスケッタソースを追加")

class GoatCheese:
    def __init__(self):
        print("ゴートチーズを追加")