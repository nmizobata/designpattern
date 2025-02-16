'''
メイン
'''

import phase1_remotecontrol as remotecontrol
import phase1_command as command
import phase1_vender_lib as vender_lib

remote = remotecontrol.SimpleRemoteControl()
light_living = vender_lib.Light("リビング")
remote.setCommand(command.LightOnCommand(light_living))
remote.buttonWasPressed()

remote.setCommand(command.LightOffCommand(light_living))
remote.buttonWasPressed()