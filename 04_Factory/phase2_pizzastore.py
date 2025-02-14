from abc import ABC, abstractmethod
import phase2_pizza as pizza_recipe

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
        if type == "チーズ":
            pizza = pizza_recipe.NYStyleCheezePizza()
        elif type == "ペパロニ":
            pizza = pizza_recipe.NYStylePepperoniPizza()
        elif type == "アサリ":
            pizza = pizza_recipe.NYStyleClamPizza()
        elif type == "野菜":
            pizza = pizza_recipe.NYStyleVeggiePizza()
        else:
            pizza = None
        return pizza
                
class ChicagoPizzaStore(PizzaStore):
    def createPizza(self, type:str) -> pizza_recipe.Pizza:
        if type == "チーズ":
            pizza = pizza_recipe.ChicagoStyleCheezePizza()
        elif type == "ペパロニ":
            pizza = pizza_recipe.ChicagoStylePepperoniPizza()
        elif type == "アサリ":
            pizza = pizza_recipe.ChicagoStyleClamPizza()
        elif type == "野菜":
            pizza = pizza_recipe.ChicagoStyleVeggiePizza()
        else:
            pizza = None
        return pizza
            
    
class CaliforniaPizzaStore(PizzaStore):
    def createPizza(self, type:str) -> pizza_recipe.Pizza:
        if type == "チーズ":
            pizza = pizza_recipe.CaliforniaStyleCheezePizza()
        elif type == "ペパロニ":
            pizza = pizza_recipe.CaliforniaStylePepperoniPizza()
        elif type == "アサリ":
            pizza = pizza_recipe.CaliforniaStyleClamPizza()
        elif type == "野菜":
            pizza = pizza_recipe.CaliforniaStyleVeggiePizza()
        return pizza
    