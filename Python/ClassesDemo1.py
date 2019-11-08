class MyClass:
    def myfunc(self):
        print("kumar") #pass

    def display(self,name):
        print("Name is :",name)



#Function -outside class , doesn't belongs to any class
# Method - Within class , belongs to class where it was created

#Create object
mc=MyClass()
mc.myfunc()
mc.display("Siva")

#Instance method and static method

class FirstClass:
    def m1(self): #Instance method
        print("Instance method")

    @staticmethod
    def m2():  #Static method - doesn't require self keyword,
                    # If we mention it will throw error TypeError: m2() missing 1 required positional argument: 'self'
                    #It will treat 'self' as paramter
        print("Static method")

    @staticmethod
    def m3(age):
        print("Age is :",age)
f=FirstClass()
f.m1()
FirstClass.m2()
FirstClass.m3(10)


#Declare variables inside class
class Secondclass:
    a,b=100,200  #class variables

    def add(self):
        print(self.a+self.b)  #access class variables using self keyword

    def mul(self):
        print(self.a*self.b)

s=Secondclass()
s.add()
s.mul()

#Local variables , Global variable and class variables

#Local variables - variables created within the method
#class variables - variables created inside the class
#Gloabal variables - variables created outside of the class

i,j=15,25  #Global variables

class ThirdClass:
    a,b=10,20 #class variables

    def add(self,x,y): # x,y - local variables
        print(x+y) #Accessing local variables  -3
        print(self.a+self.b) #Accessing class variables -30
        print(i+j) #Accesssing Global variables -40

t=ThirdClass()
t.add(1,2)


#Same variable for Local variables , Global variable and class variables
a,b=15,25  #Global variables

class FouthClass:
    a,b=10,20 #class variables

    def add(self,a,b): # x,y - local variables
        print(a+b) #Accessing local variables  -3
        print(self.a+self.b) #Accessing class variables -30
        print(globals()['a']+globals()['b']) #Accesssing Global variables -40

f=FouthClass()
f.add(1,2)

#Creating multiple objects for one class
class Fifthclass:
    def display(self):
        print("Good morning")

obj1=Fifthclass()
obj1.display()

obj2=Fifthclass()
obj2.display()



#Named object and Nameless object
#Named object - object created and assigned to a reference variables Eg: obj=Myclass()  , obj.display()
#Nameless object - object created but not assigned to a reference variables Eg: Myclass() , Myclass().display()

obj1=Fifthclass()  #Named object
obj1.display()

Fifthclass().display()  #Nameless object


#How to check memory locations of object

f1=Fifthclass()
f2=Fifthclass()
f3=f1

print(id(f1)) #4482729936
print(id(f2))  #4482730320
print(id(f3)) #4482729936

#if you want to verify 2 objects pointing to same location or not
print(f1 is f2) #False
print(f1 is f3)  #True

print(f1 is not f2) #True
print(f1 is not f3)  #False
