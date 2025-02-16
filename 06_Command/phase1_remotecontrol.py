'''
リモコンクラス
'''

class SimpleRemoteControl:
    def __init__(self):
        self.slot = ""
        
    def setCommand(self, command):
        self.slot = command
        
    def buttonWasPressed(self):
        self.slot.execute()