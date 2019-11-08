#Creating Set
my_set = {"Chalk", "Duster", "Board"}
print(my_set)  #{'Duster', 'Board', 'Chalk'}

#Looping Items in Set
for x in my_set:
    print(x)

print("Chalk" in my_set) #True

#Adding element to Set
my_set.add("Pen")
print(my_set)  #{'Duster', 'Board', 'Pen', 'Chalk'}

#Adding element to Set
my_set.update(["Pencil", "Eraser"])
print(my_set) #{'Pencil', 'Chalk', 'Pen', 'Duster', 'Eraser', 'Board'}

#Length of Set
print(len(my_set)) #6

#Remove element from set
my_set.remove("Pencil")
print(my_set)  #{'Duster', 'Eraser', 'Pen', 'Board', 'Chalk'}


my_set.discard("Pen")
print(my_set) #{'Duster', 'Eraser', 'Board', 'Chalk'}

# my_set.remove("Pencil")
my_set.discard("Pen")
print(my_set.pop()) #Chalk

my_set.clear()
print(my_set)

del my_set
my_set_2 = {"Apples", 1,2, (3,4,5)}
print(my_set_2)
my_list = [1,2,3]
print(my_list)
my_set_3 = set(my_list)
print(my_set_3)
# UNION | INTERSECTION | DIFF | SYMMETRIC DIFF
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3, 4, 5}
print(A.union(B))
print(A | B)
print(A.intersection(B))
print(A & B)
print(A.difference(B))
print(A - B)
print(A.symmetric_difference(B))
print(A ^ B)