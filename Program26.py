class Class1:
    def display1(self):
        print("I am in class1")
class Class2(Class1):
    def display2(self):
        print("I am in class2")
class Class3(Class2):
    def display3(self):
        print("I am in class3")

c=Class3()
c.display1()
c.display2()
c.display3()
