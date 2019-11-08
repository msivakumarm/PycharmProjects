#Example1
def sum(*args):
    s=0
    for i in args:
        s=s+i #s+=i
    print("Sum is :",s)

sum(3,6)
sum(5,6,9)

#Example2
def mu_three(a,b,c):
    print(a,b,c)

args=[1,2,3] #List
mu_three(*args) #1 2 3 - no of arguments same as no of paramters

#Example3
def my_three(a,b,c):
    print(a,b,c)

#pass parameter as key value pairs
x={'a':'one','b':'two','c':'three'} #dictionay data - parameter names should match with key
my_three(**x) #one two three

#Example4
def my_func(**kargs):
    for i,j in kargs.items(): #key and value pairs
        print(i,j)
 
my_func(a='one',b='two',c='three')