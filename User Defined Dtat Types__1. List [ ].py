#                                                 ********USER DEFINED DATA TYPES*******

#               There are 4 types of user defined data types in python are:1.List,
#                                                                           2.Tuple
#                                                                           3.Set
#                                                                           4.Dictionar


#                                                    ******LIST[]******



# 1.)LIST:- A list is a user defined data type.it is used to store multiple values of different data types.It is represented by square braces[].
#           A list can be store multiple values with multiple data types.List elemets are seperated by comma..it is stored in index base(0,1,2,3,4,5,6)
               #-6 -5 -4 -3 -2 -1            
#   example:-l=[10,20,30,40,50,60]      2.l=[10,'siva',20,'rajana',30,'si'40]
#                0  1  2  3  4  6              0   1    2    3      4   5  6


# LIIST OPERATIONS:-1.Indexing
#                    2.Concatenation
#                    3.Slicing
#                    4.Replication

#1.)Indexing:-    Indexing is the process to print a specified elements in a list.

#ex:- to print list elemts by an indexing method?
#l=[10,20,30,40,50,60]
#print(l[2])
#print(l[3])
#print(l[4])
#print(l[5])
#print(l[0])

# 2.)Concatenation:-Joining of two or more List elements into a single list is called concatenation.

#ex:-Write a program to print joining of two or more elements?
#l1=[10,20,30]
#l2=[40,50,60]
#l3=[70,80,90]
#print(l1+l2+l3)

#3.)Slicing:-  Slicing is the process of printing list elements in specific pattern is known as slicing.
#                  [s:e-1]>>>s=star index(0),,,,e=end index-1
#Ex:- Write a program to print slicng the values in the lsi elements?
#l=[10,20,30,40,50,60,70,80,90]
#print(l[ :6])
#print(l[4: ])
#print(l[ : ])
#print(l[1:8])


#4.)Replication:- To print the list required no.of time is known as replication.
#Ex:-
#l=[10,20,30]
#print(l*3)
#print(l*5)

#                                                        insert()
# there are three methods in liust they are:-1.Insert()--append()
#                                                        Extend()
#                                            2.Update()
#                                            3.Delete()--pop()
#                                                        remove(_)


#1.Insert():-
# i.Append():- This method is used to add and element at the end of the list
#ani=['dog','cat','cow','lion']
#ani.append('elephent')                      #>>>output:-['dog','cat','cow','lion','elephent']
#print(ani)

# ii.Insert():- This methosd is used to add an element at required position in the given list.
#ani=['dog','cat','cow','lion']
#ani.insert(3,'elephent')
#print(ani)

#iii.Extend():- This method is used to add 2 or more elements in the end of the list
#ani=['dog','cat','cow','lion']
#ani.extend(["elephent","tiger","cheetha"])
#print(ani)


#2.Update():- This method is used to Update (or) Change an element
#ani=['dog','cat','cow','lion']
#ani[3]='pig'
#print(ani)

#3.Delete():-
#i.Pop():-this method is used to remove an element in a list which is at last
#ani=['dog','cat','cow','lion']
#ani.pop()
#print(ani)

#ani=['dog','cat','cow','lion']
#ani.pop(2)
#print(ani)

#Remove():-This method is used to remove an element by its name.
#ani=['dog','cat','cow','lion']
#ani.remove("cow")
#print(ani)

#ani=['dog','cat','cow','lion']
#ani.remove("cat")
#print(ani)


#********Special Methods in List******

#ani=['dog','cat','cow','lion','tiger','elephent','goat']
#l=[10,20,30,40,50,60,70,80,90]
#print(len(ani))
#print()
#print(len(l))
#print()
#print(max(ani))
#print()
#print(max(l))
#print()
#print(min(ani))
#print()
#ani.sort()
#print(ani)
#print()
#ani.reverse()
#print(ani)





















