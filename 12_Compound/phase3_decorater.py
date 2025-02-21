import phase2_duck as duck
class QuackCounter(duck.Quackable):
    numberOfQuacks = 0    # クラス変数
    
    def __init__(self, duck:duck.Quackable):
        self.duck = duck
    
    def quack(self):
        self.duck.quack()
        QuackCounter.numberOfQuacks += 1
    
    
    @classmethod     # クラスメソッド
    def getQuacks(self):
        return QuackCounter.numberOfQuacks
        
    