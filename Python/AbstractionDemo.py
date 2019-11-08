#ABC is a predefined abstract class - we should import from abc package
from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def display(self):
        None  #No implementation

class B(A):
    def display(self):
        print("This is display method")

#obj=A() #TypeError: Can't instantiate abstract class A with abstract methods display
#obj.display() #TypeError: Can't instantiate abstract class A with abstract methods display

obj=B()
obj.display() #This is display method


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):

    def eat(self):
        print("eat NON-VEG")

class Cow(Animal):

    def eat(self):
        print("eat VEG")




t=Tiger()
t.eat() #eat NON-VEG

c=Cow()
c.eat() #eat VEG

#parent class contains 2 abstract methods
#but child class implemented 1 method -
# in this situation we cannot create object for child class. It will be consider as abstract class

#we can constrcutor in abstract class

class parent(ABC): #abstract class
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass

class child(parent):

    def m1(self):
        print("this is m1")

class subchild(child):
    def m2(self):
        print("This is m2")

#c=child() #TypeError: Can't instantiate abstract class child with abstract methods m2
s=subchild()
s.m1() #this is m1
s.m2() #this is m2

#Create constructor in abstract class
class Cal(ABC):
    def __init__(self,value):
        self.value=value  #class variable we can access in sub classes

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class C(Cal):
    def add(self):
       print(self.value+100)

    def sub(self):
        print(self.value-10)

c=C(16)
c.add() #116
c.sub() #6