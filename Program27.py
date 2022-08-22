class Base1:
    def display1(self):
        print("I am in Base1")
class Base2:
    def display2(self):
        print("I am in Base2")
class Derived(Base1,Base2):
    def display3(self):
        print("I am in Derived")

obj=Derived()
obj.display1()
obj.display2()
obj.display3()