from abc import ABC, abstractmethod

class Quackable(ABC):
    def quack(self):
        pass
    
class MallardDuck(Quackable):
    def quack(self):
        print("ガーガー")
        
class RedheadDuck(Quackable):
    def quack(self):
        print("ガーガー")
        
class DuckCall(Quackable):
    def quack(self):
        print("ガアガア")
        
class RubberDuck(Quackable):
    def quack(self):
        print("キューキュー")
        
class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose
        
    def quack(self):
        self.goose.honk()