'''
Pizzaのクラス
'''

from abc import ABC, abstractmethod

class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
        
    def prepare(self):
        print("{}を下準備".format(self.name))
        print("生地をこねる")
        print("ソースを追加")
        print("トッピングを追加")
        for topping in self.toppings:
            print(" " + topping)
    
    def bake(self):
        print("180度で25分間焼く")
    
    def cut(self):
        print("ピザを扇形にカットする")
    
    def box(self):
        print("PizzaStoreの箱にピザを入れる")
        
    def getName(self):
        return self.name

class NYStyleCheezePizza(Pizza):
    def __init__(self):
        self.name = "ニューヨークスタイルのソース&チーズピザ"
        self.dough = "薄いクラスト生地"
        self.sauce = "マリナラソース"
        self.toppings = ["すりおろしたレッジャーノチーズ"]

class NYStylePepperoniPizza(Pizza):
    def __init__(self):
        pass

class NYStyleClamPizza(Pizza):
    def __init__(self):
        pass
   
class NYStyleVeggiePizza(Pizza):
    def __init__(self):
        pass
     
class ChicagoStyleCheezePizza(Pizza):
    def __init__(self):
        self.name = "シカゴスタイルのディープディッシュチーズピザ"
        self.dough = "極厚クラスト生地"
        self.sauce = "プラムトマトソース"
        self.toppings = ["シュレッドモツァレラチーズ"]
        
    def cut(self):
        print("ピザを四角形にカットする")

class ChicagoStylePepperoniPizza(Pizza):
    def __init__(self):
        pass

class ChicagoStyleClamPizza(Pizza):
    def __init__(self):
        pass
   
class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self):
        pass
        
class CaliforniaStyleCheezePizza(Pizza):
    def __init__(self):
        pass

class CaliforniaStylePepperoniPizza(Pizza):
    def __init__(self):
        pass

class CaliforniaStyleClamPizza(Pizza):
    def __init__(self):
        pass
   
class CaliforniaStyleVeggiePizza(Pizza):
    def __init__(self):
        pass