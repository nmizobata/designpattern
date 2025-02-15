'''
Pizzaのクラス
'''

from abc import ABC, abstractmethod
import phase3_ingredient as ingredient

class Pizza(ABC):
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
        
    @abstractmethod
    def prepare(self):
        pass
        # print("{}を下準備".format(self.name))
        # print("生地をこねる")
        # print("ソースを追加")
        # print("トッピングを追加")
        # for topping in self.toppings:
        #     print(" " + topping)
    
    def bake(self):
        print("180度で25分間焼く")
    
    def cut(self):
        print("ピザを扇形にカットする")
    
    def box(self):
        print("PizzaStoreの箱にピザを入れる")
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class CheezePizza(Pizza):
    def __init__(self, ingredientFactory:ingredient.PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
        # self.name = "ニューヨークスタイルのソース&チーズピザ"
        # self.dough = "薄いクラスト生地"
        # self.sauce = "マリナラソース"
        # self.toppings = ["すりおろしたレッジャーノチーズ"]
        
    def prepare(self):
        print(self.name + "を下準備")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheeze = self.ingredientFactory.createCheese()

class ClamPizza(Pizza):
    def __init__(self, ingredientFactory: ingredient.PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
        
    def prepare(self):
        print(self.name + "を下準備")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheeze = self.ingredientFactory.createCheese()
        self.clam = self.ingredientFactory.createClam()


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory: ingredient.PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(self.name + "を下準備")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheeze = self.ingredientFactory.createCheese()
        self.pepperoni = self.ingredientFactory.createPepperoni()

class VeggiePizza(Pizza):
    def __init__(self, ingredientFactory: ingredient.PizzaIngredientFactory):
        self.ingredientFactory = ingredientFactory
    
    def prepare(self):
        print(self.name + "を下準備")
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheeze = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()


if __name__=="__main__":
    pizza = VeggiePizza(ingredient.ChicagoPizzaIngredientFactory())
    pizza.setName("テスト")
    pizza.prepare()
    