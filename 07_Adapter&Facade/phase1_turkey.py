from abc import ABC, abstractmethod

class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass
    
    @abstractmethod
    def fly(self):
        pass
        
class WildTrukey(Turkey):
    def gobble(self):
        print("ゴロゴロ")
        
    def fly(self):
        print("短い距離を飛んでいます")
        