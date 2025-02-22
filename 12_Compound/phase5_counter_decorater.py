import phase5_duck as duck

class QuackCounter(duck.Quackable):
    numberOfQuacks = 0    # クラス変数
    
    def __init__(self, duck:duck.Quackable):
        self.duck = duck
    
    def quack(self):
        self.duck.quack()
        QuackCounter.numberOfQuacks += 1
    
    def registerObserver(self, observer):
        self.duck.registerObserver(observer)
        
    def notifyObservers(self):
        self.duck.notifyObservers()
    
    @classmethod     # クラスメソッド
    def getQuacks(self):
        return QuackCounter.numberOfQuacks
        

if __name__=="__main__":
    import phase5_duck as duck
    mallardduck = QuackCounter(duck.MallardDuck())
    mallardduck.quack()
    print("{}回鳴きました".format(mallardduck.getQuacks()))
    