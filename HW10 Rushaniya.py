#авторы
'''authors={
    "Pushkin":{"Evgenii Onegin": " Onegin bla bla bla bla"},
    "Kunanbaev":{"Slova nazidaniya": "Slova bla bla bla bla"}
}

target=input("Enter an author")
for items in authors:
    if target in items:
        print(authors[target])'''

#вложенные списки
'''a=[[2,12,20],[3,13,30],[4,14,40]]
for i in a:
    for x in i:
        x+=100
        print(x,end=' ')
    print(x)'''

#жанры кино
'''films={
    "Fantasy":{"Harry Potter":"H.P. is about the boy who lived. Harry lived when Voldemort was trying to kill him with the Avada Kedavra curse.", 
            "Lord of the ring":"Set in Middle-earth, the story began as a sequel to Tolkien's 1937 children's book The Hobbit.",
            "Witcher":"Geralt of Rivia, a solitary monster hunter, struggles to find his place in a world where people often prove more wicked than beasts."},
    "Horror":{"Scream":" the story of serial killer, who has full faced mask.",
              "It": "It is about the clown-monster",
              "Demon":"the film is about the scary evel from the hell"}   
}
def new(films):
    sting=a
    a=int(input("Enter the genre of films"))
films = input("Enter the genre").lower()

print("I recommend You {}")'''


'''#Словарь студентов с оценками
students = {
    "Max": ["notes" {4, 4, 3, 3}],
    "Ben": ["notes" {4, 5, 5, 4}],
    "Mary": ["notes" {3, 4, 4, 3}],
}

def average_rating(notes):
    if len(notes) == 0:
        return 0 
    sum_notes = sum(notes)
    average_rating = sum(notes)/4
    return average_rating

for students in students.items():
    notes = average_rating(notes)
    print(f"{students} has an average rating : {average_rating}")'''