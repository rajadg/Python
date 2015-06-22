'''
Created on 20-Mar-2015

@author: dgraja
'''

import platform
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

LC_CTYPE="English_United States.1252"

if str(platform.system()).lower() == 'darwin':
    LC_CTYPE = 'C'

def create_database(db_name, port=5432):
    with psycopg2.connect(host='localhost', database='postgres', user='postgres', password='postgres', port=port) as con:
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute("CREATE DATABASE %s with owner=postgres encoding='utf-8' tablespace=pg_default connection limit = -1;" % db_name)
        return cur.statusmessage

def check_db_exists(db_name, port=5432):  
    with psycopg2.connect(host='localhost', database='postgres', user='postgres', password='postgres') as con:
        cur = con.cursor()
        cur.execute("SELECT 1 from pg_database WHERE datname='%s';" % db_name)
        return cur.rowcount == 1

def drop_database(db_name, port=5432):
    with psycopg2.connect(host='localhost', database='postgres', user='postgres', password='postgres') as con:
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute('DROP DATABASE IF EXISTS "%s"' % db_name)
        return cur.rowcount == 1
    

if __name__ == '__main__':
    
    print create_database('sampleDBs', port=5433)
    
    print "This class is a utility class"
    pass