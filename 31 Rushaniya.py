import csv
data=[
['Name','Age','City']
['Max',30,'Munich']
['Betty',20,'Berlin']
['Uta',35,'Frankfurt']
['Sam',25,'Dresden']
]
def filters_csv(csv_file_path):
    with  open (csv_file_path,'r', newline=' ') as file:
        csv_reader=csv.DictReader(file)
        for row in csv_reader:
            if row(['Name']).startwith('A'):
                print(row)
csv_file_path='data.csv'
filters_csv(csv_file_path

import csv


def read_books():
    books = []
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            books.append(row)
    return books


def add_book(books, title, author, year):
    new_book = [title, author, year]
    books.append(new_book)


def save_books(books):
    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(books)


existing_books = read_books()


print("The books we have:")
for book in existing_books:
    print(book)


add_book(existing_books, "The new book", "The new author", "2022")

save_books(existing_books)

print("The updated list:")
for book in existing_books:
    print(book)
