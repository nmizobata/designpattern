from abc import ABC, abstractmethod
import phase3_pizza as pizza_recipe
import phase3_ingredient as ingredientFactory

class PizzaStore(ABC):
        
    def orderPizza(self,type:str) -> pizza_recipe.Pizza:
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    @abstractmethod
    def createPizza(self, type):
        pass
    
class NYPizzaStore(PizzaStore):
    def createPizza(self, type:str) -> pizza_recipe.Pizza:
        self.ingredientFactory = ingredientFactory.NYPizzaIngredientFactory()
        
        if type == "チーズ":
            pizza = pizza_recipe.CheezePizza(self.ingredientFactory)
            pizza.setName("ニューヨークスタイルチーズピザ")
        elif type == "ペパロニ":
            pizza = pizza_recipe.PepperoniPizza(self.ingredientFactory)
            pizza.setName("ニューヨークスタイルペパロニピザ")
        elif type == "アサリ":
            pizza = pizza_recipe.ClamPizza(self.ingredientFactory)
            pizza.setName("ニューヨークスタイルあさりピザ")
        elif type == "野菜":
            pizza = pizza_recipe.VeggiePizza(self.ingredientFactory)
            pizza.setName("ニューヨークスタイル野菜ピザ")
        else:
            pizza = None
        
        return pizza
                
class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, type:str) -> pizza_recipe.Pizza:
        self.ingredientFactory = ingredientFactory.ChicagoPizzaIngredientFactory()
        if type == "チーズ":
            pizza = pizza_recipe.CheezePizza(self.ingredientFactory)
            pizza.setName("シカゴスタイルチーズピザ")
        elif type == "ペパロニ":
            pizza = pizza_recipe.PepperoniPizza(self.ingredientFactory)
            pizza.setName("シカゴスタイルペパロニピザ")
        elif type == "アサリ":
            pizza = pizza_recipe.ClamPizza(self.ingredientFactory)
            pizza.setName("シカゴスタイルあさりピザ")
        elif type == "野菜":
            pizza = pizza_recipe.VeggiePizza(self.ingredientFactory)
            pizza.setName("シカゴスタイル野菜ピザ")
        else:
            pizza = None
        return pizza
            
    
class CaliforniaPizzaStore(PizzaStore):
    def createPizza(self, type:str) -> pizza_recipe.Pizza:
        self.ingredientFactory = ingredientFactory.CaliforniaPizzaIngredientFactory()
        if type == "チーズ":
            pizza = pizza_recipe.CheezePizza(self.ingredientFactory)
            pizza.setName("カリフォルニアスタイルチーズピザ")
        elif type == "ペパロニ":
            pizza = pizza_recipe.PepperoniPizza(self.ingredientFactory)
            pizza.setName("カリフォルニアスタイルペパロニピザ")
        elif type == "アサリ":
            pizza = pizza_recipe.ClamPizza(self.ingredientFactory)
            pizza.setName("カリフォルニアスタイルあさりピザ")
        elif type == "野菜":
            pizza = pizza_recipe.VeggiePizza(self.ingredientFactory)
            pizza.setName("カリフォルニアスタイル野菜ピザ")
        else:
            pizza = None
        return pizza
    