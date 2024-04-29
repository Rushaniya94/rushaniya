#Квадрат числа
'''def square(x):
    print("Perfect square",x,"=",x**2)
square(15)

for i in range(1,5):
    square(i)'''
#вычисление факториала числа
'''def fac(n):
    if n==1:
        return 1
    return fac(n-1)*n
print(fac(7))'''

#НОК
'''def gsd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return a*b//gsd(a,b)

a= int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("LCM",a,"and",b,"is",lcm(a,b))'''

#из Цельсия в Фаренгейт ???????
'''def temperatureC(n):
    if temperatureF:=((n*9)/5)+32:
       print(temperatureF)
       return temperatureC==[((temperatureF-32)*5)/9]
    print (temperatureC(''))
temperatureC(0)'''

#палиндром
'''def palindrome(number):
    return number==number[::-1]
print (palindrome('1221'))'''

# расчет по кредиту?????
def credit(sum, period, percent):
    if credit==sum*(period+percent)

sum== int(input("Enter the sum"))
period== int(input("Enter the period in months"))
percent== int(input("Enter the percent"))

print(credit)
    