from enum import Enum,auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    
    
class Test:
    def __init__(self):
        self.size = Color.RED
    
    def setColor(self, color:Color):
        self.size = color
        
class Test2(Test):
    def aaaa(self):
        print("aaaa")
        
        
obj = Test2()
print(obj.size.name)
obj.setColor(Color.GREEN)
print(obj.size.name)



