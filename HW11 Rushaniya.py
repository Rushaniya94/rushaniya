#генерация чисел 2
'''import random

rand_number=random.randint(1,6)
target_num=int(input("Whats your number"))
if target_num== rand_number:
    print("The random number is ", rand_number)
    print("Congradulations!You win!")
else:
    print("The random number is ", rand_number)
    print("You will win next time!")'''

#день недели от заданной даты
'''import datetime
today=datetime.date.today()
print(today)

weekday=datetime.date.weekday(today)
print(weekday)'''

#генерация имен ????
'''import random, string

digits=random.randint(1,100)
alphabet=string.ascii_letters('q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m')
string.join([random.choice(alphabet+digits)]) 
for i in range(10):
    print(random.choice)'''

#программа победителя из списка
'''import random
list=['Nataly', 'Peter', 'Max', 'Paxton', 'Fred', 'Mary', 'Jessy','Josh']
winner=random.choice(list)
print('The winner is',winner)'''

#текущее время по секундам??????
'''import datetime
datetime.now().second
print()'''

#площадь круга
'''import math
radius=float(input("Enter the radius of the circle"))
area=math.pi*radius**2
print(f'The area is',' ',area)'''

#является ли число простым
'''x=int(input("Enter the number"))
y=2
while y<x:
    if x%y==0:
        y+=1
    print("The number is prime")
else:
    print("The number is composite")'''

#площадь треугольника 
'''import math
a=int(input("Enter the length"))
h=int(input("Enter the height"))
print("S="," ",(a*h)/2)'''

#дата от текущей даты через 7 дней
'''import datetime
today=datetime.date.today()
end_date=today+datetime.timedelta(days=7)
print("Today is", today, "and it will be",end_date,"in 7 days")'''

#количество дней между датами
'''import datetime
now_date=datetime.datetime(2023,11,16,12,12)
some_date=datetime.datetime(2023,12,31,12,12)
x=some_date-now_date
print(x)'''

#рандом по часам
'''import datetime, time,  random
a=random.randint(0,12)
b=random.randint(0,60)
c=random.randint(0,60)
random_time= datetime.time(a,b,c)
print (random_time)'''

#функция часы в формате эй эм пи эm???????????
import datetime
datetime=datetime.datetime.strftime("%I:%M:%S %p")
def time_conversion(s):
    if s[0:12]=="AM":
        print(s,"AM")
    else:
        print(s,"PM")
