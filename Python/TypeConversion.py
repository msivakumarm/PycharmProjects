#Type Casting
num1=int(input("Enter First Number:")) #10
num2=float(input("Enter Second Number:")) #10.5
print(num1+num2)  #20.5

num1=input("Enter First Number:") #10
num2=input("Enter Second Number:") #10.5
print(int(num1)+float(num2))  #20.5


num1=input("Enter First Number:") #10.5
num2=input("Enter Second Number:") #10.5
print(float(num1)+float(num2))  #21

num1=input("Enter First Number:") #10.5
num2=input("Enter Second Number:") #10
print(float(num1)+float(num2))  #20.5


num1=input("Enter First Number:") #10.5
num2=input("Enter Second Number:") #10.5
print(int(num1)+float(num2))  #ValueError: invalid literal for int() with base 10: '10.5'

#Float can hold int value
#Int cannot hold float value