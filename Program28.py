class Base:
    def display1(self):
        print("I am in Base class")
class Derived1(Base):
    def display2(self):
        print("I am in Derived1 class")
class Derived2(Base):
    def display3(self):
        print("I am in Derived2 class")

obj1=Derived1()
obj2=Derived2()
obj1.display1()
obj1.display2()
obj2.display1()
obj2.display3()