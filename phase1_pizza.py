'''
Pizzaのクラス
'''

from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass
    
    def bake(self):
        pass
    
    def cut(self):
        pass
    
    def box(self):
        pass

class CheezePizza(Pizza):
    def prepare(self):
        pass
    
class PepperoniPizza(Pizza):
    def prepare(self):
        pass
    
class ClamPizza(Pizza):
    def prepare(self):
        pass
    
class VeggiePizza(Pizza):
    def prepare(self):
        pass