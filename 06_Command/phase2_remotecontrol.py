'''
リモコンクラス
'''
import phase2_command as command
import phase2_vender_lib as vender

class RemoteControl:
    def __init__(self):
        self.onCommands = [command.NoCommand()]*7
        self.offCommands = [command.NoCommand()]*7
        
    def setCommand(self, slot:int, onCommand:command.Command, offCommand:command.Command):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
        
    def onButtonWasPressed(self, slot:int):
        self.onCommands[slot].execute()
        
    def offButtonWasPressed(self, slot:int):
        self.offCommands[slot].execute()
        
    def __str__(self):
        string = "---------- リモコン -----------\n"
        for slot in range(7):
            string += "slot[{}]: {} {}\n".format(slot, self.onCommands[slot].__class__.__name__, self.offCommands[slot].__class__.__name__)
        return string
        
if __name__=="__main__":
    remotecontrol = RemoteControl()
    remotecontrol.onCommands[0] = command.LightOnCommand()
    print(remotecontrol)