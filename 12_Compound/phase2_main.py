import phase2_duck as duck
import phase2_goose as goose
import phase2_decorater as counter

def main():
    mallardDuck = counter.QuackCounter(duck.MallardDuck())
    redheadDuck = counter.QuackCounter(duck.RedheadDuck())
    duckCall    = counter.QuackCounter(duck.DuckCall())
    rubberDuck  = counter.QuackCounter(duck.RubberDuck())
    gooseAdapter= counter.QuackCounter(duck.GooseAdapter(goose.Goose()))
    
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