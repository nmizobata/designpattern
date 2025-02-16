'''
ベンダー提供のライブラリ群
'''

class Light:
    def __init__(self, name):
        self.name = name
        self.onoff = "off"
    
    def __str__(self):
        return self.name + "のライト"
    
    def on(self):
        self.onoff = "on"
        print("{}のライトが点きました".format(self.name))
        
    def off(self):
        self.onoff = "off"
        print("{}のライトが消えました".format(self.name))
    
    def getStatus(self):
        return self.onoff

class CeilingFan:
    def __init__(self, name):
        self.name = name
        self.speed = "Off"
    
    def high(self):
        self.speed = "High"
        print("{}のCeiling FanはHighになりました".format(self.name))
    
    def medium(self):
        self.speed = "Medium"
        print("{}のCeiling FanはMediumになりました".format(self.name))

    def low(self):
        self.speed = "Low"
        print("{}のCeiling FanはLowになりました".format(self.name))

    def off(self):
        self.speed = "Off"
        print("{}のCeiling Fanは止まっています".format(self.name))
        
    def getStatus(self):
        return self.speed
    

class GarageDoor:
    def __init__(self):
        self.updown = "down"
        
    def up(self):
        self.updown = "up"
        print("ガレージのドアが開きました")
        
    def down(self):
        self.updonw = "down"
        print("ガレージのドアが閉まりました")

class Stereo:
    def __init__(self, name):
        self.name = name
        self.main_onoff = "off"
        self.cd_onoff = "off"
        self.dvd_onoff = "off"
        self.radio_onoff = "off"
        self.volume = 0
    
    def __str__(self):
        return self.name + "のステレオ(CD{}, DVD{}, Radio{})".format(self.cd_onoff, self.dvd_onoff, self.radio_onoff)
    
    def setCd(self):
        self.cd_onoff = "on"
        self.dvd_onoff = "off"
        self.radio_onoff = "off"
        print("{}のステレオにCDがセットされました".format(self.name))
        
    def setDvd(self):
        self.cd_onoff = "off"
        self.dvd_onoff = "on"
        self.radio_onoff = "off"
        print("{}のステレオにDVDがセットされました".format(self.name))

    def setRadio(self):
        self.cd_onoff = "off"
        self.dvd_onoff = "off"
        self.radio_onoff = "on"
        print("{}のステレオにRadioがセットされました".format(self.name))

    def on(self):
        self.main_onoff = "on"
        print("{}のステレオの電源がONになりました".format(self.name))
        
    def off(self):
        self.main_onoff = "off"
        print("{}のステレオの電源を消しました".format(self.name))
        
    def setVolume(self, vol:int):
        if vol < 0:
            vol = 0
        if vol > 7:
            vol = 7
        self.volume = vol
        print("{}のステレオのボリュームを{}にセットしました".format(self.name, self.volume))

if __name__=="__main__":
    stereo = Stereo("リビング")
    stereo.on()
    stereo.setCd()
    stereo.setVolume(11)
    stereo.off()
    