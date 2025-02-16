'''
リモコンクラス
'''
import phase2_command as command
import phase2_vender_lib as vender

class RemoteControl:
    def __init__(self):
        self.onCommands = [command.NoCommand()]*7
        self.offCommands = [command.NoCommand()]*7
        self.undoCommand = command.NoCommand()
        
    def setCommand(self, slot:int, onCommand:command.Command, offCommand:command.Command):
        self.onCommands[slot] = onCommand
        self.offCommands[slot] = offCommand
        
    def onButtonWasPressed(self, slot:int):
        self.onCommands[slot].execute()
        self.undoCommand = self.onCommands[slot]
        
    def offButtonWasPressed(self, slot:int):
        self.offCommands[slot].execute()
        self.undoCommand = self.offCommands[slot]
    
    def undoButtunWasPressed(self):
        self.undoCommand.undo()
    
    def __str__(self):
        string = "---------- リモコン -----------\n"
        for slot in range(7):
            string += "slot[{}]: {} {}\n".format(slot, self.onCommands[slot].__class__.__name__, self.offCommands[slot].__class__.__name__)
        string += "undo   : {}".format(self.undoCommand.__class__.__name__)
        return string
        
if __name__=="__main__":
    import phase2_vender_lib as vender
    
    remotecontrol = RemoteControl()
    remotecontrol.setCommand(0,command.LightOnCommand(vender.Light("リビング")),command.LightOffCommand("リビング"))
    remotecontrol.onButtonWasPressed(0)
    print(remotecontrol)