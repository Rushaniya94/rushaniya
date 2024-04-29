#оценка от 1 до 10
'''x=int(input("Enter your note 1-10:"))
if 1<=x<=3:
    print("Bad")
elif 4<=x<=6:
    print("Satisfactory")
elif 7<=x<=9:
    print("Well done")
else:
    print("Excellent")'''
#Который час
'''x=int(input("What time is it?:"))
if 6<=x<=12:
    print("Good morning")
elif 12<x<=18:
    print("Good afternoon")
elif 18<x<=24:
    print("Good evning")
else:
    print("Good night")'''
#Числа от 1 до введенного, которые делятся на 3
'''x=int(input("Enter the number"))
for i in range (1,x):
    if i%3==0:
        print(i)'''
#среднее арифметическое всех положительных чисел?????????????????????????????
'''number=int(input("Enter the number"))
average=sum(number)
print(average)
if number>=1:
    print('average')'''

#елочка
'''n=int(input("the trees wigth"))
num=(2*n)-2
for i in range (0,n):
    for j in range (0,num):
        print(end=" ")
    num=num-1
    for j in range (0, i+1):
        print("*", end=" ")
    print(" ")'''

#шахматы
array=[]
for i in range (8):
    temp=[]
    for j in range(8):
        if j%2==0:
            temp.append('white')
        else: temp.append('black')
    if i % 2!=0:
        temp.reverse()
    array.append(temp)
for i in array:
    print(i)

