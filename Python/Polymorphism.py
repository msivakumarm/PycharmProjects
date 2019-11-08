#overriding variable

class Parent:
    name="siva"
    name1="m"

class Child(Parent):
    name="Kumar"

c=Child()
print(c.name)  #Kumar
print(c.name1) #m

#override methods
class Bank:
    def rateofinterest(self):
        return 0

class ICICI(Bank):
    def rateofinterest(self):
        return 10.5

i=ICICI()
print(i.rateofinterest())  #10.5

obj=Bank()
print(obj.rateofinterest()) #0

#overload methods
class calc:
    def add(self,x,y,z=0):
        print(x+y+z)



c=calc()
#c.add(1) #TypeError: add() missing 1 required positional argument: 'y'
c.add(1,2)
c.add(1,2,3)