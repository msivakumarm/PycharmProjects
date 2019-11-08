#Approach1
import Python.a
import Python.b

obj1=Python.a.animal()
obj1.display()

obj2=Python.b.Bird()
obj2.display()

#Approach2
from Python.a import *
from Python.b import *

a=animal()
a.display()

b=Bird()
b.display()

#Fetch no of classes and functions in module , we cannot fetch method names
import Python.m

print(dir(Python.m)) #['A', 'B', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'm3']

#Fetch no of classes in module