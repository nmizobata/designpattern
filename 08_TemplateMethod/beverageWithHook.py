from abc import ABC, abstractmethod

class CaffeineBeverageWithHook(ABC):
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if (self.customerWantsCondiments()):
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
        
    def customerWantsCondiments(self):
        return True

class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("紅茶を浸す")
        
    def addCondiments(self):
        print("レモンを追加する")
        
    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if (answer.lower().startswith('y')):
            return True
        else:
            return False
        
        
    def getUserInput(self):
        answer = ""
        answer = input("紅茶にレモンを入れますか? (y/n)")
        return answer

class CoffeeWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print("フィルタを使ってコーヒーをドリップする")
        
    def addCondiments(self):
        print("砂糖とミルクを加える")
        
    def customerWantsCondiments(self):
        answer = self.getUserInput()
        if (answer.lower().startswith('y')):
            return True
        else:
            return False
        
        
    def getUserInput(self):
        answer = ""
        answer = input("コーヒーに砂糖とミルクを入れますか? (y/n)")
        return answer
    
if __name__=="__main__":
    tea = TeaWithHook()
    print("紅茶を淹れる")
    tea.prepareRecipe()
    
    
    coffee = CoffeeWithHook()
    print("コーヒーを淹れる")
    coffee.prepareRecipe()