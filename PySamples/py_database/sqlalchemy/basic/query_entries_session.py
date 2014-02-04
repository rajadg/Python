'''
Created on 04-Feb-2014

@author: dgraja
'''
from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from tables import *

# An Engine, which the Session will use for connection
# resources
some_engine = create_engine('sqlite:///D:\\Temp\\Python\\employees.db')

# Create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# Create a Session
session = Session()

# Create two sample records
users = session.query(User).all()

for user in users :
    addresses = session.query(Address).filter(Address.user_id == user.id).all()
    print "User :" + str(user)
    for addr in addresses :
        print "----------------" + str(addr)
