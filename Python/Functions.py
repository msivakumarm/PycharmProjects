def abc():
    print("Hi abc") #body

abc()


def myfunc():
    #statements
    pass # omits the body of the functions

myfunc()

#sum of 2 numbers
def add(a,b):
    print(a+b)

add(1,2)
add(5,6)


#sum of all numbers
def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i

    print(result)
    return result

s=sum(1,4)
print(s)


#Return None  - IF you dont explicitly mention return then it returns None
def func():
    print("Hello")

def add(sum,end):
    print("Welcome")
    return #None

x=func()
print(x)
s=add(1,2)
print(s)

#Local variable and Global variable

global_var=10  #Global variable

def f():
    local_var=100 #Local variable
    print(global_var)
    print(local_var)

f()
print(global_var)
#print(local_var) #NameError: name 'local_var' is not defined

#Same name for global and variable name
xy=100

def f2():
    xy=200
    print(xy)
    print("global" ,globals()['xy'])

f2()  #200
print(xy)  #100

#change local variable to global
z=1
def local_global():
    global z
    z=10
    print(z)
    global s
    s=200


local_global()
print("local global",z)
print("local global",s)
t=1
def increment():
    #t=10  #if both t treat as same then change t to global t
    global t
    t=10
    print(t)  #10

increment()
print(t) #10

#Passing values with default values(positional)


def func(i,j=100):
    print(i,j)

func(1,2)  #1 2
func(1) #1 100

#Keyword Arguments
def named_args(name,greeting):
    print(greeting+" "+name)

named_args("Siva","HI")  #Positional Arguments - HI Siva
named_args(name="Siva",greeting="HI")  #Keyword Arguments - HI Siva
named_args(greeting="HI",name="Siva")  #Keyword Arguments- order is not imporant -HI Siva

#Mixing of Keyword and positional arguments
def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30)  #Positional Arguments - 10 20 30
my_func(10,b=20,c=30) #Mixing of Keyword and positional arguments - 10 20 30
my_func(10,c=30,b=20) #Mixing of Keyword and positional arguments -10 20 30
#my_func(10,b=20,30)  #SyntaxError: positional argument follows keyword argument -
# Incorrect - positional arguments must appear before any keyword argument

#Return multiple values
def bigger (a,b):
    if a>b:
        return a,b
    else:
        return b,a



s=bigger(100,200)
print(s)
print(type(s))

s=bigger(200,100)
print(s)

big=s[0]
small=s[1]

print(big)
print(small)