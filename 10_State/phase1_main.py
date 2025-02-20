import state

GumballMachine = state.GumballMachine(5)

print(GumballMachine)
GumballMachine.insertQuarter()
GumballMachine.turnCrank()

print(GumballMachine)

GumballMachine.insertQuarter()
GumballMachine.ejectQuarter()
GumballMachine.turnCrank()

print(GumballMachine)

GumballMachine.insertQuarter()
GumballMachine.turnCrank()
GumballMachine.insertQuarter()
GumballMachine.turnCrank()
GumballMachine.ejectQuarter()

print(GumballMachine)

GumballMachine.insertQuarter()
GumballMachine.insertQuarter()
GumballMachine.turnCrank()
GumballMachine.insertQuarter()
GumballMachine.turnCrank()
GumballMachine.insertQuarter()
GumballMachine.turnCrank()

print(GumballMachine)