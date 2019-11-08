# Inheritance
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m2(self):
        print("this is m2 method from class B")

Aobj=A()
Aobj.m1()  #this is m1 method from class A

Bobj=B()
Bobj.m1() #this is m1 method from class A
Bobj.m2() #this is m2 method from class B

#Single Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

b=B()
b.m1()  #30 - A
b.m2()  #300  - B

#MultiLevel Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(B):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)


c=C()
c.m1()  #A
c.m2() #B
c.m3() #C

#Hirarchical Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(A):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)

b=B()
b.m1()  #A
b.m2()  #B

c=C()
c.m1()  #A
c.m3()  #B

#Multiple Inheritance
class A:
    def m1(self):
        print("This is m1 from class A")

class B:
    def m2(self):
        print("This is m2 from class B")

class C(A,B):
    def m3(self):
        print("This is m3 from class C")

c=C()
c.m1() #A
c.m2() #B
c.m3() #C