class Demo1:
    def display(self,a,b):
        return a+b
class Demo2(Demo1):
    def display(self,a,b):
        return a*b

d1=Demo1()
d2=Demo2()
print(d1.display(1,2))
print(d2.display(2,3))