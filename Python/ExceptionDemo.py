print("program started")

#print(10/0)  #ZeroDivisionError: division by zero
# try:
#     #print(10/0)
#     s=100
#     print(s)
#
#     del s
#     # del s
#     x=None
#     print(len(x))
#
# except ZeroDivisionError:
#     print("Entered into except block - ZeroDivision Error")
# except NameError:
#     print("Entered into except block - Name Error")
# except:
#     print("Exception occured")
# else:
#     print("else block")
#
# finally:
#     print("finally block")
#



# try:
#     print(10/0 )
# except TypeError:
#     print("entered into except block - handled TypeError")
# except ZeroDivisionError:
#     print("entered into except block - handled ZeroDivisionError")
# else :  #else block will be executed if there is no exception
#     print("Entered ento else block")
# finally:
#     print("This is final block")
#
# #case1 - Thrown excception - except
# #case2- Not thrown exception - else
# print("program completed")
#
# #raise exception
# def enterage(age):
#     if age<0:
#         raise ValueError("only positive integers allowed")
#
#     if age%2==0:
#         print("age is even")
#     else:
#         print("age is odd")
#
# # enterage(10)
# # enterage(5)
# # enterage(-1) #ValueError: only positive integers allowed
#
# try:
#     enterage(-1)
# except ValueError:
#     print("only positive integers allowed")
# except:
#     print("something wrong")

#Exception objects
try:
    number=one
    print("The Number is ",number)
except NameError as ex:
    print("Exception is ",ex) #Exception is  name 'one' is not defined
