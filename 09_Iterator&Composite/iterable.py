# Fibonacci Iterater
# 1,1から順にフィボナッチ数列を出力。for文などで使用できる。
# hasnext機能を持つ特殊メソッドがないので、__next__関数の中に条件＋raise StopIteratioを追加して上限を定める必要がある。


class Fibonacci:
    def __init__(self, max:int=1000):
        self.a, self.b = 1, 1
        self.max = max
        
    def __iter__(self):
        return self
    
    def __next__(self):
        current = self.a
        self.a, self.b = self.b, self.a + self.b
        if current > self.max:
            raise StopIteration
        return current
    
class List_Iterator:
    def __init__(self,list_num):
        self.list_ = list_num
        self.num = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.num += 1 
        if self.num+1 > len(self.list_):
            raise StopIteration
        return self.list_[self.num]

class Test:
    def __init__(self):
        self.dict_ = {1:"a",2:"b",3:"c",4:"d",5:"e"}
        print(self.dict_.values())
    def createIterator(self):
        return List_Iterator(list(self.dict_.values()))

# ------------------------
fib = Fibonacci(300)
next(fib) # 1
next(fib) # 1
next(fib) # 2
next(fib) # 3

# 5, 8,13,21,34,55
for i in fib:
    print(i)
    if i > 50:
        break

# [89, 144, 233]
print(list(fib))
# ------------------------

for i in Fibonacci(500):
    print(i)
    
## ----------------------
fib = Fibonacci(500)
while True:
    num = next(fib)
    print(num)
    if num > 10:
        break
    
    
test_list = Test().createIterator()
for i in test_list:
    print(i)