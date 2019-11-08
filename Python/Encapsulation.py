#private variables can be access only within the method

class Myclass:
    __a=10 #private variable
    b=20  #public

    def disp(self):
        print(self.__a)

obj=Myclass()
obj.disp()  #10
print(Myclass.b) #20
#print(Myclass.__a) #we cannot access becuase it is private variable.AttributeError: type object 'Myclass' has no attribute '__a'


#private methods can be access within the class
class Myclass:
    def __disp1(self):  #this is private method
        print("This is display1 method")

    def disp2(self):
        print("This is display2 method")
        self.__disp1()  #access other method

obj=Myclass()
obj.disp2()
#obj.__disp1() #we cannot access because it is private method.AttributeError: 'Myclass' object has no attribute '__disp1'

#we can access private variables outside if class indirectly using methods
class Myclass:
    __empid=101

    def setempid(self,eid):
        self.__empid=eid
    def getempid(self):
        print(self.__empid)

obj=Myclass()
obj.getempid() #101
obj.setempid(102)
obj.getempid() #102