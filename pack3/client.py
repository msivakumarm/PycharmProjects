#Access functons from other package
#Approach1
import sys
sys.path.append("C:\\Users\\SIVA\\PycharmProjects\\pack1")

#Approach1
import module1
import module2

module1.display()
module2.show()

#Approach2
from module1 import *
from module2 import *

display()
show()

#Approach3
from pack1.module1 import  *
from pack1.module2 import *
display() #This is display function from module1
show() #This is show function from module2


#accessing sub package
#Approach1
import sys
sys.path.append("C:\\Users\\SIVA\\PycharmProjects\\pack1")
from module1 import *

sys.path.append("C:\\Users\\SIVA\\PycharmProjects\\pack1\\pack2")
from module3 import *
show() #This is show function from module3




#Approach2
from pack1.module1 import *
from pack1.pack2.module3 import *
display() #This is display function from module1
show() #This is show function from module3