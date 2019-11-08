#Super - To invoke parent class method

class A:
    def m1(self):
        print("This is m1 from class A")


class B(A):
    def m2(self):
        print("This is m2 from class B")
        super().m1()  #calling parent class method using super()
b=B()
b.m2()

#Super - Invoke parent class variables

class A:
    a,b=10,20

class B(A):
    i,j=100,200

    def m(self,x,y):
        print("This is m2 from class B")
        print(x+y) #local variables  -3
        print(self.i+self.j)  # child class variables -300
        print(self.a+self.b) #parent class variables -30


b=B()
b.m(1,2)

#same name for local varibles,child class variables,parent class variables
a,b=15,20  #global variables

class A:
    a,b=10,20

class B(A):
    a,b=100,200

    def m(self,a,b):
        print("This is m2 from class B")
        print(a+b) #local variables  -3
        print(self.a+self.b)  # child class variables -300
        print(super().a+super().b) #Acccess parent class variables using super keyword  -30
        print(globals()['a']+globals()['b'])  #Global variables -35


i=B()
i.m(1,2)

print("constrcutor super")
#Super -To invoke parent class constructor
class A:
    def __init__(self):
        print("Constructor from A")

class B(A):
    pass

b=B()  #Constructor from A


class A:
    def __init__(self):
        print("Constructor from A")

class B(A):
    def __init__(self):
        print("Constructor from B")
        super().__init__() #Invoke parent class constructor using super
        #A.__init__(self)  #Access constuctor using class Name


b=B()  #Constructor from B , Constructor from A ,Constructor from A