'''
enum型を使うと容易にSingletonを作ることができる。
'''

from enum import Enum,auto

class Singleton(Enum):
    
    Instance = auto()
    
    def setNumber(self, number):
        self.number = number
        
    def getNumber(self):
        return self.number
        
class test:
    def __init__(self):
        self.singleton = Singleton.Instance
        
    def getNumber(self):
        return self.singleton.getNumber()
        
    def setNumber(self,number):
        self.singleton.setNumber(number)
    
    
if __name__=="__main__":
    a1 = Singleton.Instance  # インスタンス生成は＝クラス名()ではなく、クラス名.Instanceとなる。
    b1 = Singleton.Instance
    test_ = test()  # class testのコンストラクタの中で、Singleton.Instanceを宣言。
    
    a1.setNumber(50)
    print("a1のクラスでインスタンス変数numberに値50を入れると、その他のインスタンスでも変更される。(numberはクラス変数ではない)")
    print("a1 number:   {}, class id:{}".format(a1.getNumber(), id(a1)))
    print("b1 number:   {}, class id:{}".format(b1.getNumber(), id(b1)))
    print("test_ number:{}, class id:{}".format(test_.getNumber(), id(test_.singleton)))
    
    test_.setNumber(500)
    print("クラスtest_の内部変数Singletonのインスタンス変数numberに値500を入れると、その他のインスタンスでも変更される。")
    print("test_ number:{}, class id:{}".format(test_.getNumber(),id(test_.singleton)))
    print("a1 number:   {}, class id:{}".format(a1.getNumber(), id(a1)))
    print("b1 number:   {}, class id:{}".format(b1.getNumber(), id(b1)))
    
