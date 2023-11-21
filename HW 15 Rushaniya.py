'''class Person ():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age}"
    
person1=Person("Ivan",20)
person2=Person("Sam",25)

greet1=person1.introduce()
greet2=person2.introduce()
print(greet1)
print(greet2)'''

'''class Shop():
    def __init__(self,name, price, description):
        self.name=name
        self.price=price
        self.description=description
     
    def print_info (self):
        print(f"This is {self.name} {self.name}. It is{self.description}. It costs {self.price} tenge.")
    def add_item (self,description ):
        self.description.append(description)
        return len(self.description)
    def change_item(self,description):
        new_description=input(f"Enter the new description of {self.name}")
        self.description=new_description
        print(f"Atteention! The description of {self.name} have changed.Now it is:{new_description}")

item1= Shop("Banana","Yellow",200)
item2= Shop("Kiwi","green",150)
item3= Shop("Pear","Yellow",300)
item4= Shop("Apple","Red",250)'''

'''class Book:

    def __init__(self, title, author, publication_year, is_available=True):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = is_available
        
    def chekout(self):
        self.is_available = False
        print("The book is not available")
    
    def checkin(self):
        self.is_available = True
        print("The book is available")
        
    def display_info(self):
        print(f"Title - {self.title}, Author - {self.author}, Publication year - {self.publication_year}, Is available - {self.is_available}")
        
        
my_book1 = Book("Harry Potter and the philosophers stone", "J.K.Rowling", 2002, "True")
my_book2 = Book("Harry Potter and the Chamber of Secrets", "J.K.Rowling", 2004, "True")
my_book3 = Book("Harry Potter and the prisoner of Azkaban", "J.K.Rowling", 2006, "True")
my_book1.display_info()
my_book1.chekout()
my_book1.display_info()'''