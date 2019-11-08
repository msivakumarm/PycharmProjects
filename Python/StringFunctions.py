#len , max ,min

print(len("welcome"))  #7
print(max('welcome'))   #w
print(min('welcome'))  #c

#in & notin
s1='welcome'
print('come' in s1)  #True
print('DF' in s1)   #False

print('come' not in s1)  #False
print('DF' not in s1)  #True


#String Comparision

print('siva'=='kumar')  #False
print('siva'!= 'kumar')  #True
print('arrow'>'aron')  #True
print('right'>='left') #True
print('teeth' <'tee')  #False
print('yellow'<='fellow') #False
print('abc'>"") #True

#Iterating string using for loop
s='hello'

for i in s:
    print(i)
    #print(i,end="\n") #This is default behaviour
    #print(i,end="")  #print string without new line
    #print(i,end=" ")  #print string space after every character
    #print(i,end='foo') #now print() will print foo after every character


#Testing Strings

s='welcome to python'
print(s.isalnum()) #False
print(s.isalpha()) #True
print('welcome'.isalnum()) #True
print('2012'.isdigit()) #True
print('first number'.isidentifier()) #False
print('print'.isidentifier()) #True
print(s.islower()) #True
print('WELCOME'.isupper()) #True
print(' '.isspace()) #True

#Searching of substrings


s='welcome to python'
print(s.endswith('thon')) #True
print(s.startswith('good')) #False
print(s.find('come')) #3
print(s.find('become')) #-1
print(s.rfind('o')) #15
print(s.count('o')) #3

#Converting Strings
s='String in PYTHON'
print(s)  #String in PYTHON

s1=s.capitalize()
print(s1)  #String in python

s2=s.title()
print(s2)  #String In Python

s3=s.lower()
print(s3) #string in python

s4=s.upper()
print(s4) #STRING IN PYTHON

s5=s.swapcase()
print(s5) #sTRING IN python

s6=s.replace('in','on')
print(s6) #Strong on PYTHON
