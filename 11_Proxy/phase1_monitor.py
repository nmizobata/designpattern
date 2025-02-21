import phase1_state as gumball

class GumballMonitor:
    def __init__(self, machine:gumball.GumballMachine):
        self.machine = machine
        
    def report(self):
        print("ガムボールマシン： {}".format(self.machine.getLocation()))
        print("現在の在庫      : {}個のガムボール".format(self.machine.getCount()))
        state_dic = {self.machine.noQuarterState:"は25セントが投入されるのを待っています。", 
                     self.machine.soldOutState:"のガムボールは売り切れです。", 
                     self.machine.soldState:"のハンドルが回されました。ガムボールを出す準備をしています。", 
                     self.machine.hasQuarterState:"には25セントが投入されています。ハンドルが回されるのを待っています"}
        print("現在の状態      : {}{}".format(self.machine.getLocation(),state_dic[self.machine.state]))
              