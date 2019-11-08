#Creating List

list1=list()  #Create empty list
print(list1)
print(type(list1))

list2=list([22,31,61])  #Create list with elements 22,31,61
print(list2)

list3=list(['tom','jerry','spyke'])  #Create list with strings
print(list3)


list4=list("python") #Create list with characters p y,t,h,o,n
print(list4)


list5=[1,4,5,'siva',True]
print(list5)

#Accessing elements in list
l=[1,4,5,'siva',True]
print(l[0]) #1
print(l[3]) #siva



#List Common Operations
list1=[2,3,4,1,32]
print(2 in list1) #True
print(33 not in list1)  #True
print(len(list1))  #find the number of elements in the list -5
print(max(list1))  #find the largest element in the list - 32
print(min(list1))  #find the smallest element in the listt -1
print(sum(list1))  # sum of elements in the list - 42


#List slicing
list=[11,33,44,66,788,1]
print(list[0:5])  # This will return list starting from index 0 to 4 - [11,33,44,66,788]
print(list[:3]) #Similar to string start index is optional , if omitted it will be 0 -[11,33,44]
print(list[2:])  #end index is also optional , if omitted it will be set to last index of the list -[44,66,788,1]

# + and * operations in list
list1=[11,33]
list2=[1,9]
list3=list1+list2   # + Opearator joins 2 list
print(list3)  #[11, 33, 1, 9]

list4=[1,2,3,4]
list5=list4*3  # * Operator replicates the elements in the list
print(list5) #[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


#In or not in operator
list1=[11,22,44,1677,98]
print(22 in list1) #True
print(22 not in list1) #False


#Transversing list using for loop
list=[1,2,3,4,5]

for i in list:
    print(i,end=" ")

print()

#Commonly used list methods with return type
list1=[2,3,4,1,32,4]

print(list1)  #[2, 3, 4, 1, 32, 4]

list1.append(19)
print(list1)  #[2, 3, 4, 1, 32, 4, 19]

print(list1.count(4))  #2

list2=[99,54]
print(list2)
list1.extend(list2)
print(list1)  #[2, 3, 4, 1, 32, 4, 19, 99, 54]


print(list1.index(4)) #returns index of value -2

print(list1.insert(1,25))
print(list1) # [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]


print(list1.pop(2))  #index value - removed and return the value
print(list1) #[2, 25, 4, 1, 32, 4, 19, 99, 54]


list1.pop()  #last index - removed
print(list1) #[2, 25, 4, 1, 32, 4, 19, 99]


list1.remove(32)  #removes value and return none
print(list1) #[2, 25, 4, 1, 4, 19, 99]

list1.reverse()
print(list1) #[99, 19, 4, 1, 4, 25, 2]

list1.sort()
print(list1) #[1, 2, 4, 4, 19, 25, 99]


#List Comprehensive

#
# List comprehensions provide a concise way to create lists.
#It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
# The expressions can be anything, meaning you can put in all kinds of objects in lists.
# The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it.
# The list comprehension always returns a result list.

list1=[]  #Create empty list
print(list1)
for x in range(1,10):
        list1.append(x)

print(list1)


list1=[x for x in range(1,10)]
print(list1)  #  1 2 3 4 5 6 7 8 9

list2=[x+1 for x in range(1,10)]
print(list2)  # 2 3 4 5 6 7 8 9 10

list3=[x for x in range(1,10) if x%2==0]
print(list3)  # 2 4 6 8