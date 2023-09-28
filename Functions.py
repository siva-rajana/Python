#                                                     *********** FUNCTIONS **********

#Functions:-A Function is a Block of code to print calling whenever required and wherever requiered.based on arguements functions are classified into 4 groups.


#1. without arguements with return type
#2. without arguements with return type
#3. with arguemnets without return type
#4. with arguements with retuen type


# Function Creation:-1. A function is used 'def' keyword following by function name & paranthesis().
#                     2. every function has 3 parts.
#                        a.Function declaration
#                        b.function body or implementation
#                        c.function calling.

# >>Syntax of function:-
#
 #                           function name
#                              ^
#                        def siva():  >> function declaration
#                            print()  >> function body
#                        siva() --- function calling


# Advantages of Functions:-1.Function decreses file size.
#                           2.it decreases the memory.
#                           3.it increases the readability of the program.
#                           4.creation of a general functions.


# let us see some example on Functions

#def siva():
#    print(" my name is siva")        #>>> output:- my name is siva
#    print("welcome to python")
#siva()


# Classification of functions:-

#1.)without arguements with return type


#Q.) Write a program to print all arthimetic operation by usi g functions?

#def add():
#    x=20
#    y=5
#    print(x+y)
#add()


#Q.) Write a program to print the numbers using functions?

#def num():
#    n=int(input("enter any number"))
#    for i in range(1,n):
#          print(i)
#num()


#2. without arguements with return type:-

#def add():
#    x=10
#    y=20
#    z=x+y
#    return z
#res=add()
#print(res)


#3. with arguemnets without return type:-

#def add(x,y):
#    print(x+y)
#add(10,20)

#def add(x,y,z):
#    print(x+y-z)
#add(10,20,10)


#4. with arguements with retuen type:-


#def add(x,y):
#    z=x+y
#    return z
#res=add(10,20)
#print(res)


#Q.)Create dynamically program using model 3 functions(with arguements without return type)?

#def art(x,y):
#    
#    print(x+y)
#    print(x-y)
#    print(x*y)
#    print(x/y)
#    print(x%y)
#x1=int(input("eneter x value:"))
#y1=int(input("enter y value:"))
#art(x1,y1)



# **Based on arguements functions are again classified into 4 types:-1.Required arguements.
#                                                                     2.Keyword Arguements.
#                                                                     3.Default arguements.
#                                                                     4.Variable length arguements.


#1.)Required arguements:-
#                The no.of arguements in the function defination should be equal to no.of arguements in the function call.order of arguements cannot be change.

#def siva(x,y):
#    print("x=",x)            #>>output:-x=10,y=20,30   here follows the order of arguements does not change,what we give the first that only print.
#    print("y=",y)
#    print(x+y)
#siva(10,20)


#2.Keyword Arguements:-
#                The no.of arguements in function defination should be be equal no.of arguements in  the function call.the order arguements can be change by using keywords

#def siva(a,b):
#    print("a=",a)                  #>> a=20,b=10 does n ot follow order of arguements,what we given that only print.
#    print("b=",b)
#siva(b=10,a=20)

#3.Default arguements:-
#                   > one arguements is given as default.
#                   >  the no.of arguements in the function call,the no.of arguements in the function defination did not be equal.
#                   >  if any arguement is not givenm in function call then it prints the default arguement,if all the arguements are given then prints as it is.


#def display(name,course="btech"):
#    print("the name is :",name)                              #>>output:-  the name is : rama
#   print("the course is:",course)                                       # the course is: B.E
#display("rama","B.E")                                                     #the name is : siva
#print()                                                                   #the course is: btech
#display("siva")


#4. Variable length arguements:-
#                           The function is having any no.of arguements bydeclaring the arguements with preffix '*'.
#                         > The length of arguements is variable.the length is divided at the time of function call.
#                         > in function call how many variables are supplied that many variables are taken as arguements in the function definition.


#def names(*names):
#    for i in names:                        #output:- siva,rajana,siva
#        print(i)
#names("siva","rajana","siva")





#                                                      ******* "Lambda Function" **********

# Lambda function:- Lambda functions are also known as special functions are aninyamos fun ctions and  it is also known as one line function
#                 1.This functions is not used 'de'keyword
#                 2.it returns expression not a value so that it is return type function,it returns expression direct into the variable.
#                 3. This functions is mainly used to check the reality of mathmatical equations.

#res=(lambda x,y,z:x+y+z)                      #output:-the total is 18
#print("the total is",res(5,6,7))



                                                             






          
