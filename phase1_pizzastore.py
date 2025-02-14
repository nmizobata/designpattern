import phase1_factory

class PizzaStore:
    def __init__(self, factory:phase1_factory.SimplePizzaFactory):
        self.factory = factory
        
    def orderPizza(self,type:str):
        pizza = self.factory.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    
    