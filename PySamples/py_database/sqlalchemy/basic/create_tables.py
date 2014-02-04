'''
Created on 04-Feb-2014

@author: dgraja
'''

from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# An Engine, which the Session will use for connection
# resources
engine = create_engine('sqlite:///D:\\Temp\\Python\\employees.db')

# Define the metadata
metadata = MetaData()
    
# define the user table
users = Table(
    'User', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('phone', String(16)),
    Column('email', String(64))
)

# define the address table
addresses = Table(
    'Address', metadata,
    Column('id', Integer, primary_key=True),
    Column('street1', String(64)),
    Column('street2', String(64)),
    Column('landmark', String(32)),
    Column('city', String(64)),
    Column('pin', Integer),
    Column('user_id', Integer, ForeignKey('User.id'))
)

# create the table using engine
metadata.create_all(engine)




