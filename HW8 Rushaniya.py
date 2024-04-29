#список четных чисел
'''numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
avg= sum(numbers)/len(numbers)
print(avg)

sum=sum(numbers)
print(sum)'''

#кортеж с информацией о сотрудниках

'''student1=("Harry", "Gryffindor", 20)
student2=("Malfoy", "Slytherin", 20)
student3=("Jo", "Ravenclaw", 21)
student4=("Cedric", "Hufflepuff", 22)
for student in (student1,student2,student3,student4):
    print("names"," ",student[0])
    print("faculties"," ",student[1])
    print("age"," ",student[2])
    print()'''

#удаление элементов из списка
'''list=["London","Paris","Berlin","Almaty"]
list.pop(3)
print(list)'''

#фрукты , длина которых больше ????
'''fruit=["apple","banana","orange","papaya","kiwi","mango"]
fruit.clear= if len(fruit)>=5:
print(fruit)'''

#студенты и оценки
'''student1=("Ruslan",2)
student2=("Ratmir",10)
student3=("Rushaniya",8)
student4=("Ricardo",5)
student5=("Richar",4)
for student in (student1,student2,student3,student4):
    print("The name is"," ",student[0])
    print("The note is"," ",student[1])
    print()'''
#четные числа
'''even_number=[]
for i in range(0,21):
    if i%2==0:
        even_number.append(i)
print(even_number)'''


#сумма квадратов всех чисел
'''numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
square=[i**2 for i in numbers ]
sum_square=sum(square)
print(square)
print(sum_square)'''

#двухмерные массивы ?????
a=[1,2,3,4], [5,6], [7,8,9,10]
for i in range(len(a)):
    for b in range (len(a[i])):
        print(a[i][b], end=' ')
    print()