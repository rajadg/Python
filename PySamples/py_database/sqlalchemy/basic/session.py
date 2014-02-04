'''
Created on 04-Feb-2014

@author: dgraja
'''
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# An Engine, which the Session will use for connection
# resources
some_engine = create_engine('sqlite:///D:\\Temp\\Python\\sess.db')

# Create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# Create a Session
session = Session()
Base = declarative_base()

# Definition of the class that is mapped to a table named 'Point'
# This table should already exist in the database
class Point(Base):
    __tablename__ = 'Point'
    x = Column('x', Integer, primary_key=True)
    y = Column('y', Integer)
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

# Work with Session
point = Point(3,4)

print point

session.add(point)
session.commit()

