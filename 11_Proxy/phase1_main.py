import phase1_state as machine
import phase1_monitor as monitor

arg0 = "Austin"
arg1 = "112"

count = int(arg1)
gumballMachine = machine.GumballMachine(arg0, count)
monitor = monitor.GumballMonitor(gumballMachine)

monitor.report()


