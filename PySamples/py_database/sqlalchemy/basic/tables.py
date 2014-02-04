'''
Created on 04-Feb-2014

@author: dgraja
'''

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

# Definition of the class that is mapped to a table named 'Point'
# This table should already exist in the database
class User(Base):
    '''
    This class corresponds to the Users table in the database
    '''
    __tablename__ = 'User'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(50))
    phone = Column('phone', String(16))
    email = Column('email', String(64))
    def __init__(self, id, name, phone='', email=''):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
    def __str__(self):
        return str((self.id,self.name,self.phone))
    
class Address(Base):
    '''
    This class corresponds to the address table in the database
    '''
    __tablename__='Address'
    id = Column(Integer, primary_key=True)
    street1 = Column('street1', String(64))
    street2 = Column('street2', String(64))
    landmark = Column('landmark', String(32))
    city = Column('city', String(64))
    pin = Column('pin', Integer)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship("User", backref=backref('addresses', order_by=id))
    
    def __init__(self, street1='', street2='', landmark='', city='', pin=0):
        '''
        Constructor for the address table
        '''
        self.street1 = street1
        self.street2 = street2
        self.landmark = landmark
        self.city = city
        self.pin = pin
        
    def __str__(self):
        '''
        String representation of the address table
        '''
        return str((self.user_id, self.street1, self.street2, self.landmark, self.city, self.pin))
    
        