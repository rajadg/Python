'''
Created on 04-Feb-2014

@author: dgraja
'''
from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from tables import *
import random

# An Engine, which the Session will use for connection
# resources
some_engine = create_engine('sqlite:///D:\\Temp\\Python\\employees.db')

# Create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# Create a Session
session = Session()

# Create two sample records
for i in range(1,11) :
    user = User(id=2000+i, name='Test%d' % i, phone='1234567890', email='test%d@example.com' % i)
    for j in range(1, random.randrange(1,5)+1) :
        address = Address('local street %d %d' % (i, j), 'load information  %d %d' % (i, j), 'near city center  %d %d' % (i, j), 'bangalore', 560000)
        address.user = user
        session.add(address)

# commit the changes to the DB
session.commit()

