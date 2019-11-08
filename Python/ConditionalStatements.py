a=100

if a>20:
    print("This is true condition")
else:
    print("This is false condition")

if True:
    print ("This is true")
else:
    print("This is false")


if 1:  #True-1 , False-0
    print("True")
else:
    print("False")

#Even or Odd
a=3
if a%2==0:
    print("even number")
else:
    print("odd number")


#MultiStatements under if and else blocks
if 0:
    print("statement1")
    print("statement2")
    print("statement3")
else:
    print("statement4")
    print("statement5")

print ("This is not part of if else blocks")

#Single Staments in single line
print("Welcome") if True else print("python")
print("Welcome") if 10>20 else print("python")


#Multiple Staments in single line
{print("Welcome") ,print("Siva")} if True else {print("python") , print("Training")}

#elif command in python
a=12

if a==10:
    print("Ten")
elif a==20:
    print("Twenty")
elif a==30:
    print("Thirty")
else:  #Optional
    print("not listed")