file=open("D:\SeleniumPython\dummyfiles\myfile.txt","w") #open file for writing
file.write('This is First Line \n')
file.write('This is Second Line \n')

file.close()

#Reading all data at once
file=open("D:\SeleniumPython\dummyfiles\myfile.txt","r")
print(file.read()) #This is First Line  This is Second Line
file.close()

#Read given number of characters
file=open("D:\SeleniumPython\dummyfiles\myfile.txt","r")
print(file.read(2)) #Th
file.close()

#Reading all lines as an array
file=open("D:\SeleniumPython\dummyfiles\myfile.txt","r")
print(file.readlines()) #['This is First Line \n', 'This is Second Line \n']
file.close()

#Read only one line
file=open("D:\SeleniumPython\dummyfiles\myfile.txt","r")
print(file.readline())  #This is First Line
file.close()

#Append data
file=open("D:\SeleniumPython\dummyfiles\myfile.txt","a")
file.write('This is Third Line \n')
file.close()

#Looping through the data using for loop
file=open("D:\SeleniumPython\dummyfiles\myfile.txt","r")
for line in file:
    print(line)
file.close()