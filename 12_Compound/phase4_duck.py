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
        
class Flock(Quackable):
    def __init__(self):
        self.quackers = []
    
    def add(self, quacker:Quackable):
        self.quackers.append(quacker)
        
    def quack(self):
        for quacker in self.quackers:
            quacker.quack()
            
if __name__=="__main__":
    import phase2_goose as goose
    flock=Flock()
    duck1 = MallardDuck()
    duck2 = MallardDuck()
    duck3 = RedheadDuck()
    duck4 = DuckCall()
    duck5 = RubberDuck()
    duck6 = MallardDuck()
    duck7 = GooseAdapter(goose.Goose())
    
    flock.add(duck1)
    flock.add(duck2)
    flock.add(duck3)
    flock.add(duck4)
    flock.add(duck5)
    flock.add(duck6)
    flock.add(duck7)
    
    flock.quack()
    