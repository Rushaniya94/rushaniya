import sqlite3
from sqlalchemy.exc import SQLAlchemyError
Base= declarative_base()
class User(Base):
    __tablename__='users'
    id=Column(Integer,Sequence('user_id_seq'), primary_key=True)
    name=Column(String(50))
    age=Column(Integer)

engine=create_ingine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

try:
    session.begin()
    new_unser=User(name='John Doe', age=30)
    session.add(new_user)
    duplicate_user=User(name='John Doe', age=25)
    session.add(duplicate_user)
    session.commit()

except SQLAlchemyError as e:
    print(f"Error during the transaction {e}")
    session.rollback()
    session.close()