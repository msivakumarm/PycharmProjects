#Create construcor

class Myclass:
    def m1(self):
        print("Good morning")

    def __init__(self):  #Construtor will declare using init method
        print("This is constructor")

#Method contains logic , constructor initializes values
#Method we have to call explicitly,constructor will be automatically while object creation

c=Myclass()  #constructor invoked
c.m1()  #Method calling


#Converting local variables into class variables
class A:
    def values(self,val1,val2):  #val1 and val2 are local variable
        print(val1)
        print(val2)

        # Converting local variables into class variables
        self.val1=val1  #self.val1 and self.val2 are class variables
        self.val2=val2
    def add(self):
        #print(val1+val2) #NameError: name 'val1' is not defined
        print(self.val1+self.val2)

m=A()
m.values(1,2)
m.add()

 #For inializations we can use constructor
#constructor with arguments
class B:
    def __init__(self,val1,val2):  #val1 and val2 are local variable - paramerized constrctor
        print(val1)
        print(val2)

        # Converting local variables into class variables
        self.val1=val1  #self.val1 and self.val2 are class variables
        self.val2=val2
    def add(self):
        #print(val1+val2) #NameError: name 'val1' is not defined
        print(self.val1+self.val2)


m=B(1,2)  #paramerized constrctor
m.add()

#How to call current class method in another method
class C:
    def m1(self):
        print("this is m1")
        #m2(100) - #call m2 from m1 -SyntaxError: invalid syntax
        self.m2(100)


    def m2(self,a):
        print("This is m2 method ",a)
        #m1() - error

obj=C()
obj.m1()  #this is m1  - This is m2 method  100

#constructor with arguments
class D:
    def __init__(self,name):
        print(name)

#obj1=D()  #TypeError: __init__() missing 1 required positional argument: 'name'
obj1=D("Siva")


class E:
    name="Kumar"
    def __init__(self,name):
        print(name)  #constrctor argument -local vaiable
        print(self.name)  #class variable

obj1=E("Siva")


class Emp:

    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal


    def display(self):
        print("Emp id {} Emp Name: {} Emp Sal:{}".format(self.eid,self.ename,self.sal))

e=Emp(101,"Siva",10000)
e.display()

#__str__ - Executes automatically  when you print reference variable

class F:
    def __str__(self):
        return  "This is str"  #returns only string . If we mention other it will throw type error

obj2=C()
print(obj2) # Memory location of object - <__main__.C object at 0x00706090>

obj3=F()
print(obj3)  #This is str

#replace display with __str__ , print (name of object)
class Emp1:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal

    def __str__(self):
        return "Emp id {} Emp Name: {} Emp Sal:{}".format(self.eid,self.ename,self.sal)

e=Emp1(101,"Siva",10000)
print(e)  #Emp id 101 Emp Name: Siva Emp Sal:10000

#__del_ Executes when we destroy the object
class G:
    def m1(self):
        pass
    def __del__(self):
        print("Destroyed")

g1=G()
del g1

