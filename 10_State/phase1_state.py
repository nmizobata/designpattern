class GumballMachine:
    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3
    
    def __init__(self, count:int):
        self.state = GumballMachine.SOLD_OUT
        self.count = 0
        self.count = count
        if count > 0:
            self.state = GumballMachine.NO_QUARTER
            
    def insertQuarter(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("もう25セントを投入することはできません")
        elif self.state == GumballMachine.NO_QUARTER:
            self.state = GumballMachine.HAS_QUARTER
            print("25セントを投入しました")
        elif self.state == GumballMachine.SOLD_OUT:
            print("25セントを投入することはできません。売り切れです")
        elif self.state == GumballMachine.SOLD:
            print("お待ちください。ガムボールを出す準備をしています")
            
    def ejectQuarter(self):
        if self.state == GumballMachine.HAS_QUARTER:
            print("25セントを返却しました")
            self.state = GumballMachine.NO_QUARTER
        elif self.state == GumballMachine.NO_QUARTER:
            print("25セントを投入していません")
        elif self.state == GumballMachine.SOLD:
            print("申し訳ありません。すでにハンドルを回しています")
        elif self.state == GumballMachine.SOLD_OUT:
            print("返金できません。まだ25セントを投入していません")
            
    def turnCrank(self):
        if self.state == GumballMachine.SOLD:
            print("2回回してもガムボールをもう一つ手に入れることはできません")
        elif self.state == GumballMachine.NO_QUARTER:
            print("ハンドルを回しましたが、25セントを投入していません")
        elif self.state == GumballMachine.SOLD_OUT:
            print("ハンドルを回しましたが、ガムボールがありません")
        elif self.state == GumballMachine.HAS_QUARTER:
            print("ハンドルを回しました")
            self.state = GumballMachine.SOLD
            self.dispense()
    
    def dispense(self):
        if self.state == GumballMachine.SOLD:
            print("ガムボールがスロットから出てきます")
            self.count = self.count - 1
            if self.count == 0:
                print("おっと、ガムボールが無くなりました")
                self.state = GumballMachine.SOLD_OUT
            else:
                self.state = GumballMachine.NO_QUARTER
        elif self.state == GumballMachine.NO_QUARTER:
            print("まずお金を払う必要があります")
        elif self.state == GumballMachine.SOLD_OUT:
            print("販売するガムボールはありません")
        elif self.state == GumballMachine.HAS_QUARTER:
            print("ハンドルを回す必要があります")
            
    def __str__(self):
        state_dic = {GumballMachine.NO_QUARTER:"は25セントが投入されるのを待っています。",
                     GumballMachine.SOLD_OUT:"のガムボールは売り切れです。",
                     GumballMachine.SOLD:"のハンドルが回されました。ガムボールを出す準備をしています。",
                     GumballMachine.HAS_QUARTER:"には25セントが投入されています。ハンドルが回されるのを待っています"}
        string = "\nMighty Gumball, Inc.\n"
        string += "Java対応据付型ガムボール モデル#2004\n"
        string += "在庫:{}個のガムボール\n".format(self.count)
        string += "マシン{}\n".format(state_dic[self.state])
        return string
            