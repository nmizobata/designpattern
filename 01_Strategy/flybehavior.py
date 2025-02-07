from abc import ABC, abstractmethod

class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyWithWings(FlyBehavior):
    def fly(self):
        print("飛んでいます")
        
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("飛べません")
        
class FlyRocketPoweres(FlyBehavior):
    def fly(self):
        print("ロケットで飛んでいます！")