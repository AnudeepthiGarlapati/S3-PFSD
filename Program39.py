import math
class Demo:
    def p_rectangle(self,l,b):
        print("Perimeter of Rectangle is:",2*(l+b))
    def a_rectangle(self,l,b):
        print("Area of Rectangle is :",l*b)
    def p_circle(self,r):
        print("Perimeter of Circle: ",2*math.pi*r)
    def a_circle(self,r):
        print("Area of circle: ",math.pi*r*r)
    def p_triangle(self,x,y,z):
        print("Perimeter of triangle is ",x+y+z)
    def a_triangle(self,x,y,z):
        s=(x+y+z)/2
        print("Area of triangle is ",math.sqrt(s*(s-x)*(s-y)*(s-z)))

obj=Demo()
obj.p_rectangle(1,2)
obj.a_rectangle(1,2)
obj.p_circle(2)
obj.a_circle(2)
obj.p_triangle(3,6,4)
obj.a_triangle(3,6,4)