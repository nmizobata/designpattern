import phase4_state as state

GumballMachine = state.GumballMachine(5)

print(GumballMachine)
GumballMachine.insertQuarter()
GumballMachine.refill(5)
GumballMachine.turnCrank()

print(GumballMachine)

GumballMachine.insertQuarter()
GumballMachine.refill(5)
GumballMachine.ejectQuarter()
GumballMachine.turnCrank()

print(GumballMachine)

GumballMachine.insertQuarter()
GumballMachine.turnCrank()
GumballMachine.refill(5)
GumballMachine.insertQuarter()
GumballMachine.refill(5)
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