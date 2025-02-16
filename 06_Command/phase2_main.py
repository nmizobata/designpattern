'''
メイン
'''

import phase2_remotecontrol as remotecontrol
import phase2_command as command
import phase2_vender_lib as vender

# 装置インスタンスの生成
remote = remotecontrol.RemoteControl()
light_living = vender.Light("リビング")
light_kitchen = vender.Light("キッチン")
ceilingfan = vender.CeilingFan("リビング")
garagedoor = vender.GarageDoor()
stereo = vender.Stereo("リビング")

# 各装置の制御インスタンスの生成
light_living_on = command.LightOnCommand(light_living)
light_living_off = command.LightOffCommand(light_living)

light_kitchen_on = command.LightOnCommand(light_kitchen)
light_kitchen_off = command.LightOffCommand(light_kitchen)

ceilingfan_on = command.CeilingFanOnCommand(ceilingfan)
ceilingfan_off = command.CeilingFanOffCommand(ceilingfan)

garageDoor_up = command.GarageDoorUpCommand(garagedoor)
garagedoor_down = command.GarageDoorDownCommand(garagedoor)

stereoWithCD_on = command.StereoOnWithCDCommand(stereo)
stereo_off = command.StereoOffCommand(stereo)

# リモコンボタンへの各制御インスタンスの割付
remote.setCommand(0, light_living_on, light_living_off)
remote.setCommand(1, light_kitchen_on, light_kitchen_off)
remote.setCommand(2, ceilingfan_on, ceilingfan_off)
remote.setCommand(3, stereoWithCD_on, stereo_off)

print(remote)

remote.onButtonWasPressed(0)
remote.offButtonWasPressed(0)
remote.onButtonWasPressed(1)
remote.offButtonWasPressed(1)
remote.onButtonWasPressed(2)
remote.offButtonWasPressed(2)
remote.onButtonWasPressed(3)
remote.offButtonWasPressed(3)
