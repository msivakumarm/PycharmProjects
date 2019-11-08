str1='welcome'
str2='welcome'

print(id(str1))  #4524172912
print(id(str2))  #4524172912

str2="Siva"
print(id(str1))  #4524172912
print(id(str2))  #4359120624


str2=str2+" kumar"

print(id(str2))  #4350387760