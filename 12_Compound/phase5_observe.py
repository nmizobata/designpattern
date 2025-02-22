from abc import ABC, abstractmethod

# サブジェクト＝通知する側(今回はカモ達)
class QuackObservable(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass
    
    @abstractmethod
    def notifyObservers(self):
        pass
    
# オブザーバー＝通知を受け取る側(今回はカモ研究者)
class Observer(ABC):
    @abstractmethod
    def update(self, duck):
        pass

class Quacklogist(Observer):
    def update(self, duck:QuackObservable):
        print("カモの鳴き声学者: {}が鳴きました".format(duck.__class__.__name__))

class BirdWatcher(Observer):
    def update(self, duck:QuackObservable):
        print("バードウォッチャ: {}を見つけました!!".format(duck.__class__.__name__))

if __name__=="__main__":
    import phase5_duck as duck
    import phase5_counter_decorater as counter
    import phase5_abstractfactory as factory
    

    duckfactory = factory.CountingDuckFactory()
    mallardduck = duckfactory.createMallardDuck()
    rubberduck  = duckfactory.createRubberDuck()
    redheadduck1 = duckfactory.createRedheadDuck()
    redheadduck2 = duckfactory.createRedheadDuck()

    flock_redhead = duck.Flock()
    flock_redhead.add(redheadduck1)
    flock_redhead.add(redheadduck2)
    flock = duck.Flock()
    flock.add(mallardduck)
    flock.add(rubberduck)
    flock.add(flock_redhead)
    
    quacklogist = Quacklogist()
    birdwatcher = BirdWatcher()
    flock.registerObserver(quacklogist)
    flock_redhead.registerObserver(birdwatcher)
    # mallardduck.registerObserver(quacklogist)
    # rubberduck.registerObserver(quacklogist)
    # mallardduck.quack()
    # rubberduck.quack()
    flock.quack()
    print("カモが{}回鳴きました".format(counter.QuackCounter.getQuacks()))