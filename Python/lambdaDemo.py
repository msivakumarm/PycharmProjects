def x(a):
    return a+10

print(x(5)) #15 

x=lambda a:a+10

print(x(5)) #passing single variable -15

x=lambda a,b:a*b
print(x(5,6)) #passing multiple variables -30

x=lambda a,b,c:a+b+c
print(x(5,6,2)) #13