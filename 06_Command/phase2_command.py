'''
コマンドオブジェクトクラス
'''

from abc import ABC, abstractmethod
import phase2_vender_lib as vender

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
    
class NoCommand(Command):
    def execute(self):
        pass
    
    def undo(self):
        pass
        
class LightOnCommand(Command):
    def __init__(self,light):
        self.light = light
        
    def execute(self):
        self.light.on()
        
    def undo(self):
        self.light.on()
        
class LightOffCommand(Command):
    def __init__(self,light:vender.Light):
        self.light = light
        
    def execute(self):
        self.light.off()
        
    def undo(self):
        self.light.on()
        
class StereoOnWithCDCommand(Command):
    def __init__(self,stereo:vender.Stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.on()
        self.stereo.setCd()
        self.stereo.setVolume(11)
    
    def undo(self):
        self.stereo.off()

class StereoOffCommand(Command):
    def __init__(self,stereo:vender.Stereo):
        self.stereo = stereo
    
    def execute(self):
        self.stereo.off()

    def undo(self):
        self.stereo.on()
        
class CeilingFanHighCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        self.prev_status = ""
        
    def execute(self):
        self.prev_status = self.ceilingfan.getStatus()
        self.ceilingfan.high()
            
    def undo(self):
        CeilingFan_dic = {
            'High':self.ceilingfan.high,
            'Medium':self.ceilingfan.medium,
            'Low':self.ceilingfan.low,
            'Off':self.ceilingfan.off}
        CeilingFan_dic[self.prev_status]()

class CeilingFanMidiumCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        self.prev_status = ""
        
    def execute(self):
        self.prev_status = self.ceilingfan.getStatus()
        self.ceilingfan.medium()
            
    def undo(self):
        CeilingFan_dic = {
            'High':self.ceilingfan.high,
            'Medium':self.ceilingfan.medium,
            'Low':self.ceilingfan.low,
            'Off':self.ceilingfan.off}
        CeilingFan_dic[self.prev_status]()


class CeilingFanLowiumCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        self.prev_status = ""
        
    def execute(self):
        self.prev_status = self.ceilingfan.getStatus()
        self.ceilingfan.low()
            
    def undo(self):
        CeilingFan_dic = {
            'High':self.ceilingfan.high,
            'Medium':self.ceilingfan.medium,
            'Low':self.ceilingfan.low,
            'Off':self.ceilingfan.off}
        CeilingFan_dic[self.prev_status]()

class CeilingFanOffCommand(Command):
    def __init__(self, ceilingfan:vender.CeilingFan):
        self.ceilingfan = ceilingfan
        
    def execute(self):
        self.prev_status = self.ceilingfan.getStatus()
        self.ceilingfan.off()
        
    def undo(self):
        CeilingFan_dic = {
            'High':self.ceilingfan.high,
            'Medium':self.ceilingfan.medium,
            'Low':self.ceilingfan.low,
            'Off':self.ceilingfan.off}
        CeilingFan_dic[self.prev_status]()
class GarageDoorUpCommand(Command):
    def __init__(self, garagedoor:vender.GarageDoor):
        self.garagedoor = garagedoor
        
    def execute(self):
        self.garagedoor.up()
        
    def undo(self):
        self.garagedoor.down()

class GarageDoorDownCommand(Command):
    def __init__(self, garagedoor:vender.GarageDoor):
        self.garagedoor = garagedoor
        
    def execute(self):
        self.garagedoor.down()
    
    def undo(self):
        self.garagedoor.up()

class MacroCommand(Command):
    def __init__(self, command_list:list[Command]):
        self.commands = command_list
        
    def execute(self):
        for command_item in self.commands:
            command_item.execute()

    def undo(self):
        pass

if __name__=="__main__":
    light_genkan = vender.Light("玄関")
    # print(light_genkan)
    lighton = LightOnCommand(light_genkan)
    # lightoff = LightOffCommand(light_genkan)
    # lighton.execute()
    # lightoff.execute()
    
    stereo = vender.Stereo("リビング")
    stereoon = StereoOnWithCDCommand(stereo)
    # stereoon.execute()
    # stereoon.undo()
    # stereooff = StereoOffCommand(stereo)
    # stereooff.execute()
    # stereooff.undo()
    
    commands_list = []
    commands_list.append(lighton)
    commands_list.append(stereoon)
    macro = MacroCommand(commands_list)
    macro.execute()
    