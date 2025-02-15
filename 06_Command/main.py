'''
メイン
'''

import remotecontrol
import command
import vender_lib

remote = remotecontrol.SimpleRemoteControl()
light_living = vender_lib.Light("リビング")
remote.setCommand(command.LightOnCommand(light_living))
remote.buttonWasPressed()

remote.setCommand(command.LightOffCommand(light_living))
remote.buttonWasPressed()