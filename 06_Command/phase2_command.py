'''
コマンドオブジェクトクラス
'''

from abc import ABC, abstractmethod
import phase2_vender_lib as vender

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class NoCommand(Command):
    def execute(self):
        pass
        
class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light
        
    def execute(self):
        self.light.on()
        
class LightOffCommand(Command):
    def __init__(self,light:vender.Light):
        self.light = light
        
    def execute(self):
        self.light.off()
        
class StereoOnWithCDCommand(Command):
    def __init__(self,stereo:vender.Stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.setCd()
        self.stereo.setVolume(11)

class StereoOffCommand(Command):
    def __init__(self,stereo:vender.Stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.Off()

class CeilingFanOnCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        
    def execute(self):
        self.ceilingfan.on()


class CeilingFanOffCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        
    def execute(self):
        self.ceilingfan.off()

class GarageDoorUpCommand(Command):
    def __init__(self, garagedoor:vender.GarageDoor):
        self.garagedoor = garagedoor
        
    def execute(self):
        self.garagedoor.up()

class GarageDoorDownCommand(Command):
    def __init__(self, garagedoor:vender.GarageDoor):
        self.garagedoor = garagedoor
        
    def execute(self):
        self.garagedoor.down()

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        
    def execute(self):
        self.ceilingfan.off()

if __name__=="__main__":
    light_genkan = vender.Light("玄関")
    print(light_genkan)
    lighton = LightOnCommand(light_genkan)
    lightoff = LightOffCommand(light_genkan)
    lighton.execute()
    lightoff.execute()
    