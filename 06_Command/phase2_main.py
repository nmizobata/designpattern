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

ceilingfan_high = command.CeilingFanHighCommand(ceilingfan)
ceilingfan_medium = command.CeilingFanMidiumCommand(ceilingfan)
ceilingfan_off = command.CeilingFanOffCommand(ceilingfan)

garageDoor_up = command.GarageDoorUpCommand(garagedoor)
garagedoor_down = command.GarageDoorDownCommand(garagedoor)

stereoWithCD_on = command.StereoOnWithCDCommand(stereo)
stereo_off = command.StereoOffCommand(stereo)

# リモコンボタンへの各制御インスタンスの割付
remote.setCommand(0, light_living_on, light_living_off)
remote.setCommand(1, light_kitchen_on, light_kitchen_off)
remote.setCommand(2, ceilingfan_high, ceilingfan_off)
remote.setCommand(3, ceilingfan_medium, ceilingfan_off)
remote.setCommand(4, stereoWithCD_on, stereo_off)

# マクロボタンの設定
macro_on_command_list = []
macro_on_command_list.append(light_living_on)
macro_on_command_list.append(ceilingfan_medium)
macro_on_command_list.append(stereoWithCD_on)
macro_on = command.MacroCommand(macro_on_command_list)
macro_off_command_list = []
macro_off_command_list.append(light_living_off)
macro_off_command_list.append(ceilingfan_off)
macro_off_command_list.append(stereo_off)
macro_off = command.MacroCommand(macro_off_command_list)
remote.setCommand(5, macro_on, macro_off)

print(remote)

remote.onButtonWasPressed(5)
remote.offButtonWasPressed(5)
print(remote)
# remote.undoButtunWasPressed()
# remote.onButtonWasPressed(3)
# print(remote)
# remote.undoButtunWasPressed()

