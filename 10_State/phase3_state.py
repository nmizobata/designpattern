from abc import ABC, abstractmethod
import random

class State(ABC):
    @abstractmethod
    def insertQuarter(self):
        pass

    @abstractmethod
    def ejectQuarter(self):
        pass

    @abstractmethod
    def turnCrank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass

class SoldState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("お待ちください。ガムボールを出す準備をしています")

    def ejectQuarter(self):
        print("申し訳ありません。すでにハンドルを回しています")

    def turnCrank(self):
        print("2回回してもガムボールをもう一つ手に入れることはできません")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() > 0:
            self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
        else:
            print("おっと、ガムボールが無くなりました")
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class SoldOutState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self):
        print("25セントを投入することはできません。売り切れです")

    def ejectQuarter(self):
        print("返金できません。まだ25セントを投入していません")

    def turnCrank(self):
        print("ハンドルを回しましたが、ガムボールがありません")

    def dispense(self):
        print("販売するガムボールはありません")

class NoQuarterState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self):
        print("25セントを投入しました")
        self.gumballMachine.setState(self.gumballMachine.getHasQuarterState())

    def ejectQuarter(self):
        print("25セントを投入していません")

    def turnCrank(self):
        print("ハンドルを回しましたが、25セントを投入していません")

    def dispense(self):
        print("まずお金を払う必要があります")

class HasQuarterState(State):
    
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
    
    def insertQuarter(self):
        print("もう25セントを投入することはできません")

    def ejectQuarter(self):
        print("25セントを返却しました")
        self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())

    def turnCrank(self):
        print("ハンドルを回しました")
        winner = random.randint(0,1)
        if winner == 0 and self.gumballMachine.getCount() > 1:
            print("当たりです！ 25セントで2つのガムボールがもらえます")
            self.gumballMachine.setState(self.gumballMachine.getWinnerState())
        else:
            print("残念、はずれです！ 1つのガムボールがもらえます")
            self.gumballMachine.setState(self.gumballMachine.getSoldState())

    def dispense(self):
        print("ガムボールが出せません")

class WinnerState(State):
    def __init__(self, gumballMachine):
        self.gumballMachine = gumballMachine
        
    def insertQuarter(self):
        print("お待ちください。もう一つガムボールを出す準備をしています")

    def ejectQuarter(self):
        print("申し訳ありません。すでにハンドルを回しています")

    def turnCrank(self):
        print("2回回してもガムボールをもう一つ手に入れることはできません")

    def dispense(self):
        self.gumballMachine.releaseBall()
        if self.gumballMachine.getCount() == 0:
            self.gumballMachine.setState(self.gumballMachine.getSoldOutState())
        else:
            self.gumballMachine.releaseBall()
            if self.gumballMachine.getCount() > 0 :
                self.gumballMachine.setState(self.gumballMachine.getNoQuarterState())
            else:
                print("おっと、ガムボールが無くなりました")
                self.gumballMachine.setState(self.gumballMachine.getSoldOutState())

class GumballMachine:
    def __init__(self, numberGumballs:int):
        self.soldOutState = SoldOutState(self)
        self.noQuarterState = NoQuarterState(self)
        self.hasQuarterState = HasQuarterState(self)
        self.soldState = SoldState(self)
        self.winnerState = WinnerState(self)
        
        self.count = numberGumballs
        if numberGumballs > 0:
            self.state = self.noQuarterState
        else:
            self.state = self.soldOutState
            
    def insertQuarter(self):
        self.state.insertQuarter()
            
    def ejectQuarter(self):
        self.state.ejectQuarter()
            
    def turnCrank(self):
        self.state.turnCrank()
        self.state.dispense()
    
    def setState(self,state):
        self.state = state
        
    def releaseBall(self):
        print("ガムボールがスロットから出てきます")
        if self.count != 0:
            self.count = self.count - 1 
    
    def getNoQuarterState(self):
        return self.noQuarterState
    
    def getSoldState(self):
        return self.soldState
    
    def getSoldOutState(self):
        return self.soldOutState
    
    def getHasQuarterState(self):
        return self.hasQuarterState
    
    def getWinnerState(self):
        return self.winnerState
    
    def getCount(self):
        return self.count
    
    def __str__(self):
        state_dic = {self.noQuarterState:"は25セントが投入されるのを待っています。",
                     self.soldOutState:"のガムボールは売り切れです。",
                     self.soldState:"のハンドルが回されました。ガムボールを出す準備をしています。",
                     self.hasQuarterState:"には25セントが投入されています。ハンドルが回されるのを待っています"}
        string = "\nMighty Gumball, Inc.\n"
        string += "Java対応据付型ガムボール モデル#2004\n"
        string += "在庫:{}個のガムボール\n".format(self.count)
        string += "マシン{}\n".format(state_dic[self.state])
        return string
            