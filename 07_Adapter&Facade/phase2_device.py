class Popper:
    def __init__(self,name="ポップコーンメーカー"):
        self.name = name
        
    def on(self):
        print("{}をスイッチオン".format(self.name))
        
    def pop(self):
        print("{}がポップコーンを作っています！".format(self.name))
        
    def off(self):
        print("{}をスイッチオフ".format(self.name))
        
class lights:
    def __init__(self,name="シアターの天井照明"):
        self.name = name
    
    def dim(self, power):
        print("{}を{}%まで暗くします".format(self.name, power))
        
    def on(self):
        print("{}をスイッチオン".format(self.name))
        
    def off(self):
        print("{}をスイッチオフ".format(self.name))
        
class screen:
    def __init__(self,name = "シアターのスクリーン"):
        self.name = name
    
    def down(self):
        print("{}を下ろします".format(self.name))
        
    def up(self):
        print("{}を上げます".format(self.name))
        
class projector:
    def __init__(self,name = "プロジェクター"):
        self.name = name
        
    def on(self):
        print("{}をスイッチオン".format(self.name))
        
    def wideScreenMode(self):
        print("{}はワイドスクリーンモード(縦横比16x9)です".format(self.name))
    
    def off(self)    :
        print("{}をスイッチオフ".format(self.name))
        
class amp:
    def __init__(self,name = "アンプ"):
        self.name = name
    
    def on(self):
        print("{}をスイッチオン".format(self.name))
        
    def setStreamingPlayer(self):
        print("{}をストリーミングプレーヤーに設定".format(self.name))
        
    def setSurroundSound(self):
        print("{}のサラウンドサウンドをスイッチオン".format(self.name))
        
    def setVolume(self, num):
        print("{}の音量を{}に設定".format(self.name, num))
    
    def off(self):
        print("{}をスイッチオフ".format(self.name))
        
class player:
    def __init__(self, name = "ストリーミングプレイヤー",):
        self.name = name
        self.moviename = ""
        
    def on(self):
        print("{}をスイッチオン".format(self.name))
        
    def play(self, moviename):
        self.moviename = moviename
        print("{}は「{}」を再生".format(self.name,moviename ))
        
    def stop(self):
        print("{}は「{}」を停止".format(self.name, self.moviename))
        
    def off(self):
        print("{}をスイッチオフ".format(self.name))