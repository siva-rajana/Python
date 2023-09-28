#2.>>> Operators:-
             #An operator is special character (or) Symbol used to caluculate (or) operate a specific task on variables is called "Operators".operators are classified into 6 types,they are...
    #1.arthimatic operators.
    #2.Assignment operators.
    #3.Relational operators.
    #4.Logical operators.
    #5.Bitwise operators.
    #6.Membership operators.


  #1.)Arthimatic Operators:-
        #>>Arthimatic operators are Addition(+),Substraction(-),Multiplication(*),Division(/),Modulus(%).let us do some excercise problems on arthimatic operators......

#x=100
#y=25
#print(x+y)
#print(x-y)
#print(x*y)
#print(x/y)
#print(x%y)


   #2.)Assignment operators:-
            #Assignment operators are used to increase or decrease the variablke values.these are created by arthimatic operators.(+=,-=,*=,/=,%=)


#(x=100
#x+=10
#print(x)

#x=100
#x-=10
#print(x)

#x=100
#x*=10
#print(x)

#x=100
#x/=10
#print(x)

#x=100
#x%=10
#print(x)


   #3.)Relational Operators:-
            #these operators are used to conditons,,,, these also called as coparission operators.(>=,<=,<,>,!=,==)
                        # 1.<  --less than
                        # 2.>  -- greater than
                        # 3.<=  -- less than or equals to
                        # 4.>=  -- greater than or equals to
                        # 5.!=  -- not equals to
                        # 6.==  -- Equals to Equals to.
        # let us do some excerice operation on relational operators.......

#x=50
#y=30
#z=75
#print(x<y) >> false
#print(x>y) >> true
#print(x<z) >> true
#print(z>y) >> true


        #4.)Logical operators:-
        #               Logical operators are used to combine two or more conditions.it includes 3 operators,they are:and,or,not........
                                #1.and:-if all the conditions are true then only output is true, otherwise false.t-t=t,t-f=f,f-t=f,f-f=f
                                #2.or:-If all the conditions are false then output is false,otherwise true..t-t=t,t-f=t,f-t=t,f-f=f..
                                #s3.not:-if the input is false,then only the output is true,if the input is true,then output is false..

#
#x=50
#y=30
#z=75
#print((x<y)and(x<z)and(z>x)) >> false
#print((x>y)or(x<z)or(z<y))   >> true

        #5.)Bitwise operators:-
                        #The bitwise operators are used to manipulate bit operations means(0 and 1)...The main Bitwise operators are and(&),or(|),ex_or(^),left_shift(<<),Right_shift(>>)..

       #i.)and(&):-0-0>>0, 1-0>>0, 0-1>>0, 1-1>>1..
       #ii.)or(|):-0-0>>0, 0-1>>1, 1-0>>1, 1-1>>1...
       #iii.)ex_or(^):-0-0>>0,1-0>>1, 0-1>>1, 1-1>>1..

    #Binary conversion:-it includes only o and 1....
        #ex:-78  >> 64 32 16 8 4 2 1                                                        note:-any number can easily convert into binary codes by this logic---
        #(64+8+4+2)- 1  0  0 1 1 1 0---this is the binary conversion of 78                          
        #ex:2.) >>  1 0  1  1 1 0 1  --binary conversion                                              previous no double 1028 512 256 128 64 32 16 8 4 2 1
        #          64 32 16 8 4 2 1  -- Decimal conversion of 93
        #           64+16+8+4+1=93(only 1's add)...


 #let us do some excerice problems on bitwise operators:-

#x=100
#y=77
#print(x&y) >> 68
#print(x|y) >> 109
#print(x^y) >> 41


        #iv.)left_shift operator(<<):- ex=1.x=<<3           64  32  16  8  4  2  1
        #                                                    1   1   0  0  1  1  1         x=103
        #                                     1    1    0    0   1   1  1  0  0  0
        #                                    512   256  128  64 32   16 8  4  2  1
        
        #                                x<<3=512+256+32+16+8=824


        #v.)Right _Shift(>>):-  ex=x>>4                       128  64  32  16  8  4  2  1
        #                                                      1    0   0   1  0  0  0  0
        #                                                       0   0   0   0  1  0  0  1   0   0   0    0
        #                                                     128   64  32  16 8   4 2  1

        #                                                       8+1=9 ---x>>4,,,x=144
                                                           
#x=103
#print(x<<3) ---824

#x=144
#print(x>>4)  --- 9







