#Create set in python
a={1,4,2.4,'aaa','abc',9,2}
b=set([1,4,3,'abc'])
print(a)
print(b)

#Create empty set
c=set()
print(c)

#dir returns number of methods
print(dir(a))

#length of set
My_set={1,'s',7.8}
print(len(My_set))  #3

#Access elements
a={1,4,2.4,'aaa','abc',9,2,1,2}
print(a) #prints only unique elements {1, 2, 4, 9, 2.4, 'aaa', 'abc'}

for x in a:
    print(x,end=" ") #1 2 4 9 2.4 aaa abc
print()

#Adding elements
e=set()
print(e) #set()

e.add(1)
print(e) #{1}

e.update([4,7,'ab'])
print(e) #{1, 4, 'ab', 7}

#Remove,discard,pop
a={1,4,2.4,'aaa','abc',9,2}
print(a) #{1, 2, 4, 9, 'abc', 'aaa', 2.4}

a.remove(4)
print(a) #{1, 2, 9, 'abc', 'aaa', 2.4}

#a.remove(4) #a.remove(4) -{1, 3, 4, 'abc'} KeyError: 4
a.discard(4)
print(a) #{1, 2, 'abc', 9, 2.4, 'aaa'}

print("pop")
print(a.pop()) # random value 1
print(a) #{2, 9, 'abc', 2.4, 'aaa'}

#Union of sets
a={1,2,4.6,7.8,'r','s'}
b={2,5,'d','abc'}

print(a|b)  #{1, 2, 'd', 5, 's', 7.8, 4.6, 'abc', 'r'}
print(a.union(b)) #{1, 2, 's', 'd', 5, 'abc', 7.8, 4.6, 'r'}

#Intersection of sets
a={1,2,4.6,7.8,'r','s'}
b={2,5,'d','abc'}
print(a&b) # {2}
print(a.intersection(b)) # {2}

#Difference of sets
print(a-b) #{1, 7.8, 'r', 4.6, 's'}
print(a.difference(b)) #{1, 7.8, 'r', 4.6, 's'}

e=frozenset(a)
print(e) #frozenset({1, 2, 4.6, 'r', 's', 7.8})
#e.add(3) #AttributeError: 'frozenset' object has no attribute 'add'
