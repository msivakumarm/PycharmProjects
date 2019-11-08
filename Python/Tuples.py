#Creating Tuples
t1=() #Creating an empty tuple with no data
t2=(11,22,33)
t3=tuple([1,2,3,4,4]) #tuple from array
t4=tuple('abc')  #tuple from String

print(t1) #()
print(t2) #(11, 22, 33)
print(t3) #(1, 2, 3, 4, 4)
print(t4) #('a', 'b', 'c')

#Tuple Funtions
t1=(1,12,55,12,81)
print(min(t1)) #1
print(max(t1))  #81
print(sum(t1))  #161
print(len(t1)) #5

#Iterating through tuples
t=(11,22,33,44,55)
for i in t:
    print(i,end=" ") #11 22 33 44 55
print()

#Slicing tuples
t=(11,22,33,44,55)
print(t[0:2]) #(11, 22)
print(t[2:4]) #(33, 44)
print(t[:3]) #(11, 22, 33)
print(t[2:]) #(33, 44, 55)

#in and not in operator
t=(11,22,33,44,55)
print(22 in t) #True
print(22 not in t) #False

