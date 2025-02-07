from abc import ABC, abstractmethod

class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
    
class Quack(QuackBehavior):
    def quack(self):
        print("ガーガー")
        
class MuteQuack(QuackBehavior):
    def quack(self):
        print("<<沈黙>>")
        
class Squeak(QuackBehavior):
    def quack(self):
        print("キューキュー")