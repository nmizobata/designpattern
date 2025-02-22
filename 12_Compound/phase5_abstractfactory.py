from abc import ABC, abstractmethod
import phase5_duck as duck
import phase2_goose as goose
import phase5_counter_decorater as counter

class AbstractDuckFactory(ABC):
    @abstractmethod
    def createMallardDuck(self):
        pass
    @abstractmethod
    def createRedheadDuck(self):
        pass
    @abstractmethod
    def createDuckCall(self):
        pass
    @abstractmethod
    def createRubberDuck(self):
        pass
    @abstractmethod
    def createGooseAdapter(self):
        pass
    
class DuckFactory(AbstractDuckFactory):
    def createMallardDuck(self):
        return duck.MallardDuck()
    
    def createRedheadDuck(self):
        return duck.RedheadDuck()
    
    def createDuckCall(self):
        return duck.DuckCall()
    
    def createRubberDuck(self):
        return duck.RubberDuck()
    
    def createGooseAdapter(self):
        return duck.GooseAdapter(goose.Goose())
    
class CountingDuckFactory(AbstractDuckFactory):
    def createMallardDuck(self):
        return counter.QuackCounter(duck.MallardDuck())
    
    def createRedheadDuck(self):
        return counter.QuackCounter(duck.RedheadDuck())
    
    def createDuckCall(self):
        return counter.QuackCounter(duck.DuckCall())
    
    def createRubberDuck(self):
        return counter.QuackCounter(duck.RubberDuck())
    
    def createGooseAdapter(self):
        return counter.QuackCounter(duck.GooseAdapter(goose.Goose()))
    