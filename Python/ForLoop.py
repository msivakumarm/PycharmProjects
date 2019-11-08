#print 0 to 9 numbers

for i in range(10):  #bydefault starting value is 0
    print(i)  # 0 1 2 3 4 5 6 7 8 9

#print 1 to 10
for i in range(1,11):
    print(i)

#print even numbers
for i in range(2,10,2):  #initial value , max value , increment/decrement
    print(i) # 2,4 ,6 ,8

#print odd numbers
for i in range(1,10,2):  #initial value , max value , increment/decrement
    print(i) # 1,3,5,7,9

#print 10 to 1 (descending order)
for i in range(10,1,-1):
    print(i)  # 10,9,8,7,6,5,4,3,2

fruits=['apple','banana','grape']
for val in fruits:
    print(val)
else:
    print("no fruits left")