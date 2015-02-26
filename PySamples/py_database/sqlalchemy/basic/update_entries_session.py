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

some_engine.execute("ALTER TABLE User ADD COLUMN count INTEGER")

exit()

# Create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# Create a Session
session = Session()

# Create two sample records
users = session.query(User).all()

for user in users :
    addresses = session.query(Address).filter(Address.user_id == user.id).all()
    print "User :" + str(user)
    for j in range(1, random.randrange(1,5)+1) :
        address = Address('local street updated %d %d' % (user.id, j), \
                          'load information updated  %d %d' % (user.id, j), \
                          'near city center updated %d %d' % (user.id, j), 'mangalore', 560000)
        address.user = user
        session.add(address)


# commit the changes to the DB
session.commit()