#                                                             ****** Sets ******

# Setes:- A set is user defined data type used to unindened data,without reapeating the elements.it is represented by flower braces { }.
#       >> The mainly sets are used to solve mathematical caluculation,it does not follow order by printing the elements.

#Ex:-
#s={10,20,30,40,50,60,70,80,90}                        #>>output:-{20,40,90,80,10,30,50}   means it does not follow the order print all values in set
#print(s)                                                   (or){10,30,60,70,80,40,50,90}

# There are four main sets in set:  1. a|b   -- a union b
#                                   2. a&b   -- a intersection b
#                                   3.a-b    -- a difference in b
#                                   4.b-a    -- b difference in a

#Write a code on sets?

#a={10,20,30,40}
#b={15,10,18,16}
#c={16,15,18,20,14}
#print(a|b)   #>> {10,20,40,15,18,30,16}
#rint(a&b)   #>> {10}
#print(a-b)   #>> {40,20,30}
#print(b-c)   #>> {10}


#Q.)Write a program on combined set operations?

#a={10,20,30,40}
#b={15,10,18,16}
#c={16,15,18,20,14}

#print((a|b) & (a|c))
#print((b|c) | (a&c))
#print((c&b) - (a-c))




#                                                               ********* Dictionary **********

#Dictionary:-   A dictionary is user defined data type useed to store apair of values named as key and values.it is represented by flower braces{} 
#             >> A dictionary can store pair of values knowns as keys and values,every pair is seperated by comma(,) & assign values colon(:)
#             >> A Dictionary is mutable and immutable data type. In Thhis keys are immutable(can't change) and Values are mutable (change)
             
#ex:- k  v    keys  values  item(k&v)     k     v
#d={'id':100,'name':'Siva','Roll no':381,'clg':'acet'}

#print(d)          #>>{'id':100,'name':'Siva','Roll no':381,'clg':'acet'}
#print(d.keys())   #>>dict_keys(['id', 'name', 'Roll no', 'clg'])
#print(d.values()) #>>dict_values([100, 'Siva', 381, 'acet'])
#print(d.items())  #>>dict_items([('id', 100), ('name', 'Siva'), ('Roll no', 381), ('clg', 'acet')])



# Insert() and Update() method in dictionary
#d={'id':381,'name':'Siva','marks':70,'clg':'acet'}

#d['surname']="Rajana"   #>> Insert()
#d['marks']=67.84         #>> update()       {'id': 381, 'name': 'Siva', 'marks': 67.84, 'clg': 'acet', 'surname': 'Rajana'}
#print(d)


#Q>) To create fully dynamic dictionary by using key list and values list
#key_list=[]
#n=int(input("enter the key list elements size:"))
#for i in range(n):
#    s=input("eneter the key list:")
#    key_list.append(s)
    
#values_list=[]
#m=int(input("enter the values:"))
#for j in range(m):
#    s=input("enter the values list:")
#    values_list.append(s)
#dic=dict(zip(key_list,values_list))
#print(dic)




































