'''
Created on 30-Jul-2016

@author: dgraja
'''
import json
from elasticsearch import Elasticsearch
from time import time
from datetime import datetime
from test.calls import __server_addr__
from _ctypes import ArgumentError



index_name = "test_%s" % datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

def display(name, data):
    line = "-" * 80
    print line 
    print "%s: %s" % (name, json.dumps(data, indent=2))
    print line + "\n\n"


def create_index(es):
    '''
        create a new index 
        uses HTTP PUT like this:
            curl -XPUT -i 'http://localhost:9200/<index-name>'
    '''
    es.indices.create(index_name)


def delete_index(es, name):
    '''
        delete an index by name
        Delete the index using HTTP DELETE like this:
            curl -XDELETE 'http://localhost:9200/<index-name>/'
    '''
    if name and (isinstance(name, str) or isinstance(name, unicode)):
        '''
            Check if index exists using HTTP HEAD like this:
            curl -XHEAD -i 'http://localhost:9200/<index-name>'
        '''
        if es.indices.exists(name):
            print "deleting index " + name
            print es.indices.delete(name)
        else:
            print "index not found: %s" % name
    else:
        raise ValueError(name)
    return


def find_index(es, pattern=None):
    '''
        Find an index with given name pattern
        like this:
            curl -XGET 'http://localhost:9200/<pattern>/'
    '''
    if pattern:
        indices = es.indices.get(index=pattern, format='json', expand_wildcards="all")
        display("index search by pattern: %r" % pattern, indices.keys())
        return indices.keys(), indices
    return


def close_index(es, name=None):
    '''
        Close an index so that it becomes inactive
        like this:
            curl -XPOST 'localhost:9200/<index-name>/_close'
    '''
    if name and (isinstance(name, str) or isinstance(name, unicode)):
        es.indices.close(index = name)


def open_index(es, name=None):
    '''
        Opens an index (previous inactive) so that it becomes active
        like this:
            curl -XPOST 'localhost:9200/<index-name>/_open'
    '''
    if name and (isinstance(name, str) or isinstance(name, unicode)):
        es.indices.open(index = name)


def add_items(es):
    '''
        Add a custom item to the existing index
        like this:
            curl -XPOST 'localhost:9200/<index-name>/<doc_name>?op_type=create' -d '<content-data>'
    '''
    data = {'time': datetime.utcnow(),
            'type': 'warning',
            'thread': 234234,
            'pid': 1001,
            'location': 'sample.test',
            'message': 'test message at ...',
            'traceback': None}
    print es.create(index=index_name, doc_type='log', body=data)


def main():
    es = Elasticsearch([__server_addr__,])
    print "Cleaning up already existing indices ... "
    result, _ = find_index(es, pattern='test_*')
    for item in result:
        delete_index(es, name=item)
        
    print "New index : %s" % index_name
    create_index(es)
    add_items(es)
    result, _ = find_index(es, pattern='test_*')
    for item in result:
        close_index(es, name=item)
    
    return


if __name__ == '__main__':
    main()
    pass