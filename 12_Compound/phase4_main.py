import phase3_decorater as counter
import phase4_duck as duck
import phase3_abstractfactory as factory

def main():
    duckFactory = factory.CountingDuckFactory()
    
    mallardDuck = duckFactory.createMallardDuck()
    redheadDuck = duckFactory.createRedheadDuck()
    duckCall    = duckFactory.createDuckCall()
    rubberDuck  = duckFactory.createRubberDuck()
    gooseAdapter= duckFactory.createGooseAdapter()
    
    print("\nカモシミュレータ  コンポジット(群れ)付")
    flockOfDucks= duck.Flock()
    flockOfDucks.add(redheadDuck)
    flockOfDucks.add(duckCall)
    flockOfDucks.add(rubberDuck)
    flockOfDucks.add(gooseAdapter)
    
    flockOfMallards = duck.Flock()
    
    mallard1 = duckFactory.createMallardDuck()
    mallard2 = duckFactory.createMallardDuck()
    mallard3 = duckFactory.createMallardDuck()
    mallard4 = duckFactory.createMallardDuck()
    
    flockOfMallards.add(mallard1)
    flockOfMallards.add(mallard2)
    flockOfMallards.add(mallard3)
    flockOfMallards.add(mallard4)
    
    flockOfDucks.add(flockOfMallards)
    
    print("\nカモシミュレータ 群れ全体のシミュレーション")
    simulate(flockOfDucks)
    
    print("\nカモシミュレータ マガモの群れのシミュレーション")
    simulate(flockOfMallards)
    
    print("カモが鳴いた回数：{}回".format(counter.QuackCounter.getQuacks()))
    
    
def simulate(duck:duck.Quackable):
    duck.quack()
    
if __name__=="__main__":
    main()