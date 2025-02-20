from abc import ABC, abstractmethod

class MenuComponent(ABC):
    def add(self):
        pass
        
    def remote(self):
        pass
    
    def getChild(i:int):
        pass
    
    def getName(self):
        pass
    
    def getDescription(self):
        pass
    
    def getPrice(self):
        pass
    
    def isVegetarian(self):
        pass
    
    def print(self):
        pass
    
    
class MenuItem(MenuComponent):
    def __init__(self, name:str, description:str, vegetarian:bool, price:float):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price
        
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def isVegetarian(self):
        return self.vegetarian
    
    def print(self):
        print(" "+self.getName(), end="")
        if self.isVegetarian():
            print("(V)", end = "")
        print(", "+str(self.getPrice()))
        print("    -- "+self.getDescription())

class Menu(MenuComponent):
    def __init__(self, name:str, description:str):
        self.menuComponents = []
        self.name = name
        self.description = description
        
    def add(self, menuComponent: MenuComponent):
        self.menuComponents.append(menuComponent)
        
    def remove(self, menuComponent: MenuComponent):
        self.menuComponents.remove(menuComponent)
        
    def getChild(self, i:int):
        return self.MenuComponents[i]
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def print(self):
        print("\n"+self.getName(), end="")
        print(", "+self.getDescription())
        print("-------------------------")
    
        for menuComponent in self.menuComponents:
            menuComponent.print()