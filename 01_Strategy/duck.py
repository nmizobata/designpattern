from abc import ABC, abstractmethod
import flybehavior as fly
import quackbehavior as quack


class Duck(ABC):
    # def __init__(self, flybehavior:fly.FlyBehavior, quackbehavior:quack.QuackBehavior):
    #     self.flyBehavior = flybehavior
    #     self.quackBehavior = quackbehavior
    @abstractmethod
    def __init__(self):
        self.flyBehavior = fly.FlyBehavior()
        self.quackBehavior = quack.QuackBehavior()
    
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
        
    def swim(self):
        print("すべてのカモは浮きます。おもちゃのカモでも")
        

class MallardDuck(Duck):
    # def __init__(self):
    #     super().__init__(flybehavior = fly.FlyWithWings(), quackbehavior = quack.Quack())
    def __init__(self):
        self.flyBehavior = fly.FlyWithWings()
        self.quackBehavior = quack.Quack()
    
    def display(self):
        print("私は本物のマガモです")

class RedheadDuck(Duck):
    pass

class RubberDuck(Duck):
    def __init__(self):
        self.flyBehavior = fly.FlyNoWay()
        self.quackBehavior = quack.MuteQuack()
        
    def display(self):
        print("私はおもちゃのゴムでできたカモです")

class DecoyDuck(Duck):
    def __init__(self):
        self.flyBehavior = fly.FlyNoWay()   
        self.quackBehavior = quack.MuteQuack()
        
    def display(self):
        print("私は木で作られたカモです")
        
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
    print("-"*10)
    rubbuerduck = RubberDuck()
    rubbuerduck.display()
    rubbuerduck.performFly()
    rubbuerduck.performQuack()
    

    