import phase1_pizza

class SimplePizzaFactory:
    def createPizza(self,type:str):
        if type == "チーズ":
            pizza = pizza.CheezePizza()
        elif type == "ペパロニ":
            pizza = pizza.PepperoniPizza()
        elif type == "アサリ":
            pizza = pizza.ClamPizza()
        elif type == "野菜":
            pizza = pizza.VeggiePizza()
        return pizza
    
