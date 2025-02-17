import phase1_duck as duck_lib
import phase_1turkeyturkey as turkey_lib

duck = duck_lib.MallardDuck()
turkey = turkey_lib.WildTrukey()
turkeyAdapter = duck_lib.TurkeyApapter(turkey)

print("Turkeyの出力")
turkey.gobble()
turkey.fly()

print("\nDuckの出力")
duck.quack()
duck.fly()

print("\nTurkeyAdapterの出力")
turkeyAdapter.quack()
turkeyAdapter.fly()