'''
Created on 30-Jul-2016

@author: dgraja
'''
import json
from elasticsearch import Elasticsearch
from time import time
from datetime import datetime


index_name = "test_%d" % time()

def display(name, data):
    line = "-" * 80
    print line 
    print "%s: %s" % (name, json.dumps(data, indent=2))
    print line + "\n\n"


def create_index(es):
    '''
        create a new index
    '''
    es.indices.create(index_name)


def add_items(es):
    data = {'time': datetime.utcnow(),
            'type': 'warning',
            'thread': 234234,
            'pid': 1001,
            'location': 'sample.test',
            'message': 'test message at ...',
            'traceback': None}
    print es.create(index=index_name, doc_type='log', body=data)

def main():
    es = Elasticsearch(["127.0.0.1:9200",])
    create_index(es)
    add_items(es)
    return


if __name__ == '__main__':
    main()
    pass