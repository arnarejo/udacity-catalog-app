from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

categories = ["Soccer", "Basketball", "Baseball", "Frisbee", "Snowboarding", "Rock Climbing", "Foosball", "Skating", "Hockey"]

for category in categories:
    session.add(Category(name=category))
    session.commit()

user1 = User(name="Rasheed", email='alpha@gmail.com')
session.add(user1)
session.commit()

item1 = Item(name="Stick", description='Stick description ..', category_name="Hockey", user_id=1)
session.add(item1)
session.commit()
