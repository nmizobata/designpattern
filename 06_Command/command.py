'''
コマンドオブジェクトクラス
'''

from abc import ABC, abstractmethod
import vender_lib as vender

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light
        
    def execute(self):
        self.light.on()
        
class LightOffCommand(Command):
    def __init__(self,light):
        self.light = light
        
    def execute(self):
        self.light.off()
        


if __name__=="__main__":
    light_genkan = vender.Light("玄関")
    print(light_genkan)
    lighton = LightOnCommand(light_genkan)
    lightoff = LightOffCommand(light_genkan)
    lighton.execute()
    lightoff.execute()
    