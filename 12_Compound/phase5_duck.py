from abc import ABC, abstractmethod
import phase5_observe as observe

class Quackable(observe.QuackObservable):
    def quack(self):
        pass
    
    
class Observable(observe.QuackObservable):
    def __init__(self, duck:observe.QuackObservable):
        self.observers = []
        self.duck = duck
    
    def registerObserver(self, observer):
        self.observers.append(observer)
        
    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.duck)
            
class MallardDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)
    
    def quack(self):
        print("ガーガー")
        self.notifyObservers()
        
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
        
    def notifyObservers(self):
        self.observable.notifyObservers()
        
class RedheadDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)
    
    def quack(self):
        print("ガーガー")
        self.notifyObservers()
        
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
        
    def notifyObservers(self):
        self.observable.notifyObservers()
        
class DuckCall(Quackable):
    def __init__(self):
        self.observable = Observable(self)
        
    def quack(self):
        print("ガアガア")
        self.notifyObservers()
        
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
        
    def notifyObservers(self):
        self.observable.notifyObservers()
        
class RubberDuck(Quackable):
    def __init__(self):
        self.observable = Observable(self)
        
    def quack(self):
        print("キューキュー")
        self.notifyObservers()
            
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
        
    def notifyObservers(self):
        self.observable.notifyObservers()
    
class GooseAdapter(Quackable):
    def __init__(self, goose):
        self.goose = goose
        self.observable = Observable(self)
        
    def quack(self):
        self.goose.honk()
        self.notifyObservers()
          
    def registerObserver(self, observer):
        self.observable.registerObserver(observer)
        
    def notifyObservers(self):
        self.observable.notifyObservers()   
        
class Flock(Quackable):
    def __init__(self):
        self.quackers = []
        # self.observable = Observable(self)
    
    def add(self, quacker:Quackable):
        self.quackers.append(quacker)
        
    def quack(self):
        for quacker in self.quackers:
            quacker.quack()
    
    def registerObserver(self, observer):
        for quacker in self.quackers:
            quacker.registerObserver(observer)
            
    def notifyObservers(self):
        pass
            
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

    