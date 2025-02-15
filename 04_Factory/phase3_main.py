import phase3_pizzastore as PizzaStore

nyStore = PizzaStore.NYPizzaStore()
chicagoStore = PizzaStore.ChicagoPizzaStore()

pizza = nyStore.orderPizza("チーズ")
print("イーサンの注文は" + pizza.getName() )

pizza = chicagoStore.orderPizza("野菜")
print("ジョエルの注文は" + pizza.getName() )