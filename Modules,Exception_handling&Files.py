                                                 ### Modules ###

'''
Module:-A module is a free defined code used to print or we use whwneever required or wherever required.
  A     Module is a function for a class or an interface.

note:- >> No.of clasess functions becomes a module.
       >> No.of modules becomes a library.
       >> no,of libraries becomes a packages.
       >> No.of packages becomes a software.

Q.)Write a module that print output squaaring and adding no's.

First creat a new file with name of.n.py
then generate a module.

n.py =>> def sumsq(a,b):
                print((a*a+b*b))
                sumsq(3,4)

open new page
import n
n.sumsq(3,4)

output:-25
'''


#                                           **** Exception Handling ****

'''
 Exception:-
             An Exception is an error which abstracts the normal flow of execution of a program.

 Exception handling:-
             Conversion of an error into a readable message is called Exception handling.

 >> Division by zero exception:-
'''
n=int(input("enter numerator"))
d=int(input("enter dinominator"))
try:
    print(n/d)
except:
    print("error")




    
