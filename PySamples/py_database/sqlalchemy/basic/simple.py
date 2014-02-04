'''
Created on 04-Feb-2014

@author: dgraja
'''
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
import os


#help ('sqlalchemy')
#dir ('sqlalchemy')

working_directory = 'D:\\Temp\\Python'
os.chdir(working_directory)
db_path =  os.path.join("D:\\Temp\\Python", "test01.db")
print db_path

engine = create_engine('sqlite:///' +db_path)

metadata = MetaData()
 
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(512), nullable=False),
    Column('email', String(512), nullable=True)
)

metadata.create_all(engine)

# Connect to the actual database
conn = engine.connect()

def record(i):
    return ('User ' + str(i), "user" + str(i) + "@example.com")

for i in range(10) :
    rec = record(i)
    # Create an INSERT expression
    insert_expression = users.insert().values(username=rec[0], email=rec[1])
    print str(insert_expression)
    # execute the insert query
    result = conn.execute(insert_expression)
    # print the result
    print (result.inserted_primary_key)

