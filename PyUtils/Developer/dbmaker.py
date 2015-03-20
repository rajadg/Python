'''
Created on 20-Mar-2015

@author: dgraja
'''

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class Db(object):
    def __init__(self, dbname='sampledb', dbhost='localhost', dbport='5432', dbuser='postgres', dbpwd='postgres', create_db=True, drop_existing=True):
        '''
            Constructor
        '''
        self.dbname = dbname
        self.dbhost = dbhost
        self.dbport = dbport
        self.dbuser = dbuser
        self.dbpwd = dbpwd
        if create_db:
            try:
                self.create(drop_existing=drop_existing)
            except Exception, e:
                print e
    
    def create(self, db_name=None, drop_existing=True):
        '''
            Create a database with given name. If the database already exists it can be dropped or recreated, or re-used
            @param drop_existing: True to force recreation. False to use existing databaes if it exists 
        '''
        if not db_name:
            db_name = self.dbname
        with psycopg2.connect(host=self.dbhost, port=self.dbport, database='postgres', user=self.dbuser, password=self.dbpwd) as con:
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            create_db = False
            if self.exists(db_name):
                print "database %s already exists" % db_name
                if not drop_existing:
                    return
                cur.execute('DROP DATABASE IF EXISTS "%s"' % db_name)
                print "%s %s" % (cur.statusmessage, db_name)
            cur.execute("CREATE DATABASE \"%s\" with owner=postgres encoding='utf-8' tablespace=pg_default lc_collate='C' lc_ctype='C' connection limit = -1;" % db_name)
            print "%s %s" % (cur.statusmessage, db_name)
        return

    def exists(self, db_name=None):
        '''
            Check if database exists
            @return: True if database already exists. False otherwise
        '''
        if not db_name:
            db_name = self.dbname
        with psycopg2.connect(host=self.dbhost, port=self.dbport, database='postgres', user=self.dbuser, password=self.dbpwd) as con:
            cur = con.cursor()
            cur.execute("SELECT 1 from pg_database WHERE datname='%s';" % db_name)
            return cur.rowcount == 1
        
    def drop(self, db_name=None):
        '''
            Drops the database
            @return: True if database already exists. False otherwise
        '''
        if not db_name:
            db_name = self.dbname
        with psycopg2.connect(host=self.dbhost, port=self.dbport, database='postgres', user=self.dbuser, password=self.dbpwd) as con:
            con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = con.cursor()
            cur.execute('DROP DATABASE IF EXISTS "%s"' % db_name)
            print "%s %s" % (cur.statusmessage, db_name)

if __name__ == '__main__':
    print "This class is a utility class to create / drop postgresql database"
    pass