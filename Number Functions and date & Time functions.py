#                                   *****Numbers Functions(Mathematical Functions)*****

#there are different types of number functions methods, they are:-1.abs()    -- used to print absolute values(only + not - values) of given number
#                                                                  2.floor()  -- used to remove the decimal values(10.23==10)
#                                                                  3.ceil()   -- used to remove the decimal values og given number by adding 1(10.23==11)
#                                                                  4.pow()    -- used to print power of given number(3**3=27)
#                                                                  5.exp()    -- used to print expontial of given number(e=2.7182)
#                                                                  6.factorial()-used to print factoprial of given number(4=4*3*2*1=24)
#                                                                  7.sqrt()    -- used to print square root of a given n umber(sqrt4=2)
#                                                                  8.sin()     
#                                                                  9.cos()      } these are used to print the trignomatric ratios of__
#                                                                  10.tan()        sin,cos,tan values in radains(pai/180) not in degrees



#Q.) Write a simple program on number fucntions by using their methods?

#import math
#x=76.254
#a=-9
#print(abs(a))
#print()
#print(math.floor(x))
#print()
#print(math.ceil(x))
#print()
#print(math.pow(x,2))
#print()
#print(math.exp(x))
#print()
#print(math.sqrt(x))
#print()
#print(math.sin(120))
#print()
#print(math.cos(180))
#print()
#print(math.tan(210))




#                                                       ******Random Functions******
# Random Functions are used to generate random Values for variable list.These are mainly used to generate atm pin,and games designing.

#import random
#x=random.randrange(1,100)               #>>> output:-10 or 90 or 80 or any number print in between 100
#print(x)




#                                     ********Date and time functions**********

# They are 3 types of Date and time and functions in Python are:-1.)time.time()
#                                                                 2.)time.localtime(time.time())
#                                                                 3.)time.asctime(time.localtime(time.time()))
#


#1.)time.time():- this method is used to print the time upto the time when the program is exicuted

#let us see the some example on it
#import time
#t=time.time()     #>>> output:-16158974.2301456
#print(t)

#2.)2.)time.local time(time.time()):- This method is used to print the time structure at a particular time zone

#let us see the some example on it

#import time
#t=time.localtime(time.time())   #>>>time.struct_time(tm_year=2023, tm_mon=8, tm_mday=12, tm_hour=15, tm_min=19, tm_sec=57, tm_wday=5, tm_yday=224, tm_isdst=0)
#print(t)


#3.)time.asctime(time.local time(time.time()):- This metyhod is used to print the local time.

import time
t=time.asctime(time.localtime(time.time()))                 #>>> output:-Sat Aug 12 15:22:07 2023
print(t)






#                                                    *******Calender*******

# Calender:- Calender is used to find out the date and weeks for a particular month a specific year.

#import time
#import calendar
#d=calender.month(2023, 8)
#print(d)








   























