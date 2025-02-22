import phase3_counter_decorater as counter
import phase3_duck as duck
import phase3_abstractfactory as factory

def main():
    duckFactory = factory.CountingDuckFactory()
    
    mallardDuck = duckFactory.createMallardDuck()
    redheadDuck = duckFactory.createRedheadDuck()
    duckCall    = duckFactory.createDuckCall()
    rubberDuck  = duckFactory.createRubberDuck()
    gooseAdapter= duckFactory.createGooseAdapter()
    

    print("\nカモシミュレータ  抽象ファクトリ付")
    simulate(mallardDuck)
    simulate(redheadDuck)
    simulate(duckCall)
    simulate(rubberDuck)
    simulate(gooseAdapter)
    print("カモが鳴いた回数：{}回".format(counter.QuackCounter.getQuacks()))
    
    
def simulate(duck:duck.Quackable):
    duck.quack()
    
if __name__=="__main__":
    main()