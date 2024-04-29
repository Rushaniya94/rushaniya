#Сумма введенных чисел
"""n=int(input())
sum=0
for i in range(n):
    x=int(input())
    sum+=x
print(sum)"""

#Четные числа от 0 до введенного
"""n=int(input("Enter the number:"))
for b in range(1,n+1):
    rez=b%2
    if rez==0:
        print(f'{b}')"""

#Четные числа от 0 до 20
'''print()
for i in range(0,20):
    if i%2==0:
        print(i)'''

#таблица умножения
'''for i in range(1,5):
    print('i:', i)
    for a in range (1,5):
        print(f'{i*a:4}', end=' ')
    print()'''

#таблица умножения для заданного числа
'''n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,'x',i,'=',n*i)'''

#каждая буква в слова Пайтон
'''a=('Python')
for i in a:
    print(i)'''

#сумма всех нечетных чисел
'''number=int(1)
sum=int(0)
while number<101:
    rez=number%2
    if rez!=0:
        for number in range(1,100):    
                print(f' ={sum+number}')'''
#пирамида из звездочек
'''n=int(input("TREE'S WIDTH"))
number=(2*n)-2
for i in range (0,n):
    for j in range (0,number):
        print(end=" ")
    number= number-1
    for j in range (0,i+1):
        print("*",end=" ")
    print(" ")'''

#простое число
'''n=int(input("Enter the number:"))
for i in range (2,n):
    if n%n==1:
        if n%1==n:
            print("Prime number")
else:
    print("This number is not prime")'''


