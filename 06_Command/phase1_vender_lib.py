'''
ベンダー提供のライブラリ群
'''

class Light:
    def __init__(self, name):
        self.name = name
        self.onoff = "off"
    
    def __str__(self):
        return self.name + "のライト"
    
    def on(self):
        self.onoff = "on"
        print("{}のライトが点きました".format(self.name))
        
    def off(self):
        self.onoff = "off"
        print("{}のライトが消えました".format(self.name))
    
    def getStatus(self):
        return self.onoff