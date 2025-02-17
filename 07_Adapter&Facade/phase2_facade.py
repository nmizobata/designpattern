
class HomeTheaterFacade:
    def __init__(self, amp, player, projector, screen, lights, popper):
        self.amp = amp
        self.player = player
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper
        
    def watchMovie(self, movie):
        print("映画を見る準備をします")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amp.on()
        self.amp.setStreamingPlayer()
        self.amp.setSurroundSound()
        self.amp.setVolume(5)
        self.player.on()
        self.player.play(movie)
        
    def endMovie(self):
        print("ムービーシアターを停止します")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amp.off()
        self.player.stop()
        self.player.off()
        
