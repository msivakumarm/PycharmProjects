#Approach 1
import Python.animal
import Python.Bird

Python.animal.fly()
Python.animal.color()

Python.Bird.fly()
Python.Bird.color()


#Approach 2


#if both modules having same function
#consider m1 module has disp function and m2 module has disp function , which function will be called
#which modules imported last that module will be called

from  Python.animal import  *

fly() #Animal cant fly
color() #Animal is black

from Python.Bird import  *

fly() #Bird can fly
color() #Bird is Green
