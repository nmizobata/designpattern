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
        
    def setFlyBehavior(self, flybehavior:fly.FlyBehavior):
        self.flyBehavior = flybehavior
        
    def setQuackBehavior(self, quackbehavior:quack.QuackBehavior):
        self.quackBehavior = quackbehavior
        
    def swim():
        print("すべてのカモは浮きます。おもちゃのカモでも")
        

class MallardDuck(Duck):
    def __init__(self):
        super().__init__(flybehavior = fly.FlyWithWings(), quackbehavior = quack.Quack())
    
    def display(self):
        print("私は本物のマガモです")
        
class ModelDuck(Duck):
    def __init__(self):
        self.flyBehavior = fly.FlyNoWay()
        self.quackBehavior = quack.Quack()
        
    def display(self):
        print("私は模型のカモです")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.display()
    mallard.performFly()
    mallard.performQuack()
    print("-"*10)
    modelduck = ModelDuck()
    modelduck.display()
    modelduck.performFly()
    modelduck.setFlyBehavior(fly.FlyRocketPoweres())
    modelduck.performFly()

    modelduck.performQuack()
    

    