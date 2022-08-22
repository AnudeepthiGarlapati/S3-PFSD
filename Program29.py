class Base:
    def display1(self):
        print("I am in Base class")
class Derived1(Base):
    def display2(self):
        print("I am in Derived1 class")
class Derived2(Base):
    def display3(self):
        print("I am in Derived2 class")
class FinalDerived(Derived1,Derived2):
    def display4(self):
        print("I am in FinalDerived class")

obj=FinalDerived()
obj.display1()
obj.display2()
obj.display3()
obj.display4()
