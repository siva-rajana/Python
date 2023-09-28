#                                                                     LOOPS
#  4.Loops:-
#           A loop is an iterativestatements used to print block of required no.of times is called "loops".loops are classified into two types,they are...
#                  1.While loop
#                  2.For loop

#  1.While Loop:-
#                 Syntax>>  V.D
#                           i=1 or 0 or anyother num
#                           while(condition):
#                                   st-1
#                                   vairiable increase/decrease.(+,-)


# Let us do some problems on While loop....

#Q.)write a program on while loop to print the 0 to n numbers?

#num=int(input("enter any number:"))
#i=0
#while(i<=num):           >> eneter any num:10
#    print(i)             >> 0 1 2 3 4 5 6 7 8 9 10
#    i+=1

#Q.)Write a program on while loop to print Even Numbers b/w 1 to n numbers?

#n=int(input("eneter any number"))
#i=1
#while(i<=n):
#    if(i%2==0):            >> Enter any number:20
#        print(i)           >> 2 4 6 8 10 12 14 16 18 20
#   i+=1


# Q.)Write a program on while loop to print Odd numbers?

#n=int(input("eneter any number"))
#i=1                       i=1
#while(i<=n):              while(i<=n):          Enter any number:20
#    if(i%2==1):      or        print(i)                 >> 1 3 5 7 9 11 13 15 17 19
#        print(i)               i=i+2
#    i+=1


#n=int(input("n="))
#for i in range(6):
#    i=i*i
#    print(i)

#                                    *******FOR LOOP******
# SYNTAX
#       >>>     for i in range(p1,p2,p3):
#                             print(i)



# Q>.) Write a program to print wholenumbers?

#n=int(input("enter any number:"))
#for i in range(0,n+1,1):
#    print(i)                          >>> output:-0 to n numbers

#write a program to print even numbers and odd numbers full dynamically?

#ch=input("eneter choice:")
#if(ch=="even" or ch=="EVEN"):
#    n=int(input("eneter any number:"))
#    for  i in range(0,n+1,2):
#        print(i)
#elif(ch=="odd" or ch=="ODD"):
#    n=int(input("eneter any number:"))
#    for i in range(1,n+1,2):
#        print(i)
#else:
#    print("invalid choice")


#q.) Write a program to print any table in arthimatic by using for loop in fully dynamicallu?

#n=int(input("enetr any table number:"))
#start=int(input("enter start number:"))
#end=int(input("enter end number:"))           >>> output:- 2*1=2
#for i in range(start,end+1,1):                             2*2=4
#   print(n,"*",i, "=",n*i)                                2*n=n......



# Q.)write a program to print sum of digits of given number by usin g for loop?

#n=int(input("enter any number:"))
#r=0
#s=0
#while(n!=0):                          # >>> output:-525=5+2+5=12
#    r=n%10                       
#    s+=r
#    n=n//10
#print("sum of digits of given number is",s)


# Q.)write a program to print sum of digits of given number by usin g for loop?

#n=int(input("enter any number:"))
#r=1
#p=1
#while(n!=0):                        #  >>> output:-525=5*2*5=50
#    r=n%10
#    p*=r
#    n=n//10
#print("The product of digits of given number is",p)


#Q.) write a program to print numbers left side triangle pattern?
#rows=int(input("enetr no.of rows:"))     #>>>1
#for num in range(rows+1):                    22
#    for i in range(num):                     333
#        print(num,end=" ")                   4444
#    print(" ")                               55555



rows=int(input("enter rows:"))               >>> *****
for i in range(rows+1):                          ****
    for j in range(rows-i):                      ***
        print("*",end=' ')                       **
    print()                                      *


S













