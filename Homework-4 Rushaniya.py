"""x=int(input("Enter the number:"))
if x>0:
    print("Positive number")
elif x==0:
    print("Zero")
else:
    print("Negative number")"""

"""x= int(input("Enter your age:"))
if x> 18:
    print("You can drive a car.")
else:
    print("Unfortunately You can't drive a car")"""

"""number=int(input("What's the number?"))
if 9>number>21:
    print("True.The number is in the range")
else:
    print("The number is out of range")"""

"""number=input("Write your note:")

if number=="5":
    print("excellent")
elif number=="4":
    print("well")
elif number=="3":
    print("sufficient")
elif "number>6":
    print("You entered the wrong number")
else:
    print("Unsatisfactory")"""

"""age=int(input("How old are You?:"))
if  age<=2:
    print("Infant")
elif 3<=age<=12:
    print("Kid")
elif 12>=age<=18:
    print("Teenager")
elif 19>=age<=35:
    print("Young adult")
elif 36>=age<=60:
    print("Adult")
else :
    print("Senior")"""

"""number=int(input("What's a number?"))
if number==1:
    print("The first quarter")
elif number==2:
    print("The second quarter")
elif number==3:
    print("The third quarter")
elif number== 4:
    print("The fourth quarter")
else:
    print("You entered the wrong number")"""

"""number=int(input("Enter the number"))
if number>0:
    print("The number is positive")
if number%2==0:
       print("The number is even")
elif number<0:
    print ("Negative number")
else:
    print("The odd number")"""

"""year=int(input("Enter the year"))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap year")
else:
     print("Common year")"""
'''
age=int(input("How old are You?"))
health=(input("Do You have any serious illnesses?"))
if age>=18 and age<=45:    
    if health=='No' or health == 'no':
        print("You can visit the football match")
    else:
       print("You are not allowed to visit the football match")
else:
    print("The information is incorrect. Try again.")
'''
'''
print("Our delivery service costs 5 Euro per 1 kg and  100 km")
weight= int(input("Enter the weight in kg"))
distance= int(input("Enter the distance to delivery point"))
print('Itll costs', (weight*5)+((distance/100)*5))
'''



