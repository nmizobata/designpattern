from abc import ABC, abstractmethod
import phase1_turkey as turkey_lib

class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass
    
class MallardDuck(Duck):
    def quack(self):
        print("ガーガー")
        
    def fly(self):
        print("跳んでいます")
        
class TurkeyApapter(Duck):
    def __init__(self, turkey_:turkey_lib.Turkey):
        self.turkey = turkey_
        
    def quack(self):
        self.turkey.gobble()
        
    def fly(self):
        for i in range(5):
            self.turkey.fly()
        
        
if __name__=="__main__":
    turkey = TurkeyApapter(turkey_lib.WildTrukey())
    turkey.quack()
    turkey.fly()