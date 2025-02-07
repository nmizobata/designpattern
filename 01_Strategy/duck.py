from abc import ABC, abstractmethod
import flybehavior as fly
import quackbehavior as quack


class Duck(ABC):
    def __init__(self, flybehavior:fly.FlyBehavior, quackbehavior:quack.QuackBehavior):
        self.flyBehavior = flybehavior
        self.quackBehavior = quackbehavior
    
    @abstractmethod
    def display(self):
        pass
    
    def performFly(self):
        self.flyBehavior.fly()
        
    def performQuack(self):
        self.quackBehavior.quack()
        
    def swim():
        print("すべてのカモは浮きます。おもちゃのカモでも")
        

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(flybehavior = fly.FlyWithWings(), quackbehavior = quack.Quack())
    
    def display(self):
        print("私は本物のマガモです")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.performFly()
    mallard.performQuack()

    