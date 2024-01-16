from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base= declarative_base()

class User(Base):
    __tablename__="user"
    id= Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name=Column (String(50))
    age= Column(Integer)

engine= create_engine("sqlite:///:memory:", echo= True)
Base.metadata.create_all(bind=engine)
Session=sessionmaker (bind=engine)
session= Session()
person1= User( name="Python", age=30)
person2= User(name="Java", age= 50)
session.add_all([person1, person2])
session.commit()
people= session.query(User).all()
for person in people:
    print(f"The person is {person.id}, the name is {person.name} and the age is {person.age}")
INSERT INTO  people
VALUES (person3 =User( name="Scratch", age=40 ))


session.commit()
