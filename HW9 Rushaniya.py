#Создание словаря со студентами
'''dictionary={1:"Max", 2:"Pat", 3:"Sam", 4:"Kim", 5: "Bim"}
del dictionary[Bim]
print(dictionary)'''

#Товар в магазине ????????
'''list_a={1:"car",2:"ball",3:"train",4:"pistole",5:"knife"}
list_b={"10 pieces","20 pieces","30 pieces","40 pieces","50 pieces"}
list_c={"1 euro/1 piece","2 euro/ 1 piece", "3 euro/ 1 piece","4 euro/ 1 piece","5 euro/ 1 piece"}
items=list(zip(list_a,list_b,list_c))
print(items)
'''

        
#множество
'''my_set1={1,2,3,4,5,20,30,40}
my_set2={6,7,8,9,10,20,30,40}
print("Differencial",my_set1.difference(my_set2))
print("Common",my_set1.union(my_set2))'''

#множество из списка элементов
'''set1={1,2,3,4,5,6,13,15,16}
set2={7,8,9,10,11,12,15,16}
intersection=set1&set2
print(intersection)
pipe=set1|set2
print(pipe)'''

#списки городов и стран ???????
dict={Kazakhstan:'Astana', Germany:'Berlin', France:'Paris', Spain:'Madrid', Russia:'Moscow'}

print(f'Current List {dict}') 
f = input("Please enter a city:\n") 
dict.append(f) 
print(f'Updated List {dict}')



