import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_from_id= Column(Integer, ForeignKey('user.id'))
    user_to_id= Column(Integer, ForeignKey('user.id'))
    # user_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    user_name = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), unique=True)
  
    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    
class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id= Column(Integer, ForeignKey('post.id'))

    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    # person = relationship(Person)


class Comment(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, unique=True)
    comment_text= Column(String(250))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
