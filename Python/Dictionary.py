#Creating dictionary
friends={'tom':'111-222-333',
         'jerry':'666-33-111'
         }


print(friends) #{'111-222-333', 'jerry', '666-33-111', 'tom'}
print(type(friends)) #<class 'dict'>

#Retrieving elements from dictionary
print(friends['tom'])  #111-222-333


#Adding elements to dictionary
friends['bob']='888-999-666'
print(friends) #{'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-666'}


#Modifying elements to dictionary
friends['bob']='888-999-777'
print(friends) #{'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-777'}

#Delete elements to dictionary
del friends['bob']
print(friends) #{'tom': '111-222-333', 'jerry': '666-33-111'}

#Looping Items in Dictionary
values={'a':'100',
         'b':'200',
         'c':'300',
         'd':'400'}

for x in values:
    print(x," : ",values[x])

#Length of dictionary
print(len(values)) #4

#Equality Test in Dictionary
d1={'mike':41 , 'bob':3}
d2={'bob':3 , 'mike':41}

print(d1==d2) #True
print(d1!=d2) #False

#Dictionary Methods
friends={'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-666'}
print(friends) #{'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-666'}

#Pop Item - Returns randomly select an item from dictionary and also remove from the dictionary
print(friends.popitem()) #('bob', '888-999-666')
print(friends) #{'tom': '111-222-333', 'jerry': '666-33-111'}

#Clear - Clears everything from dictionary
friends.clear()
print(friends) #{}

friends={'tom': '111-222-333', 'jerry': '666-33-111', 'bob': '888-999-666'}

#Return keys in dictionary as tuples
print(friends.keys()) #dict_keys(['tom', 'jerry', 'bob'])

#Return values in dictionary as tuples
print(friends.values()) #dict_values(['111-222-333', '666-33-111', '888-999-666'])

#get(key) - Return the value of the key,if key not found it returns None,instead of throwing KeyError Exception
print(friends.get('jerry')) #666-33-111

#Pop - remove the item from the dictionary , if Key is not found KeyError will be thrown
print(friends.pop('tom')) #111-222-333
print(friends) #{'jerry': '666-33-111', 'bob': '888-999-666'}

