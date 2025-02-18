from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    def prepareRecite(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()
        
    @abstractmethod
    def brew(self):
        pass
    
    @abstractmethod
    def addCondiments():
        pass
    
    def boilWater(self):
        print("お湯を沸かす")
    
    def pourInCup(self):
        print("カップに注ぐ")
        
class Tea(CaffeineBeverage):
    def brew(self):
        print("紅茶を浸す")
        
    def addCondiments(self):
        print("レモンを追加する")
        
class Coffee(CaffeineBeverage):
    def brew(self):
        print("フィルタを使ってコーヒーをドリップする")
        
    def addCondiments(self):
        print("砂糖とミルクを追加する")
        
if __name__=="__main__":
    coffee = Coffee()
    coffee.prepareRecite()
    
    tea = Tea()
    tea.prepareRecite()
        