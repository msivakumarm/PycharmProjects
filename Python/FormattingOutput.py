name='siva'
age=28
sal=10000.25

#Approach1
print(name,age,sal)

#Approach2
print("name is :",name)
print("age is :",age)
print("sal is :",sal)


#print("name is : siva   age is : 28  sal is : 10000.25")
#print("name is : ",name," age is :",age," sal is :",sal)

# #Approach3 -using % operator - Here type of data is important
#print("Name is : %s , age is %d , sal is %f "%(name,age,sal))


#Approach4- using {}- Here order of value is important
#print("Name is : {} , age is {} , sal is {} ".format(name,age,sal))
#print("Name is : {} , age is {} , sal is {} ".format(age,age,age))


# #Approach5- using {index} - Here index and  value is important
print("Name is : {2} , age is {0} , sal is {1} ".format(age,sal,name))  #index start from 0
#print("Name is : {2} , age is {2} , sal is {2} ".format(age,sal,name))
